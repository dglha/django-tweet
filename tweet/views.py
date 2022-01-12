from django.shortcuts import render
from django import http
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Profile, Tweet
from .forms import TweetForm


# Create your views here.
@login_required()
def dashboard(request):

    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            # return http.HttpResponseRedirect('/')

    form = TweetForm()
    followed_tweets = Tweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-id')

    return render(request, "tweet/dashboard.html", {"form": form, "tweets": followed_tweets})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "tweet/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(id=pk)

    # Post method for this route
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")

        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "tweet/profile.html", {"profile": profile})


def delete_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if not tweet:
        print("Tweet not found!")
        return http.HttpResponseRedirect(reverse_lazy("tweet:profile_list"))

    elif tweet.user != request.user:
        print("You do not have permission to delete this tweet!")
        return http.HttpResponseRedirect(reverse_lazy("tweet:profile_list"))

    else:
        tweet.delete()
        print("Tweet deleted!")
        return http.HttpResponseRedirect(reverse_lazy("tweet:dashboard"))
