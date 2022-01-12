# tweet/urls.py
from django.urls import path
from .views import dashboard, profile_list, profile, delete_tweet

app_name = "tweet"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profiles/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("tweet/<int:pk>/delete", delete_tweet, name="delete")
]