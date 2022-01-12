from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(
        User,  # relative to
        related_name="tweets",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return (
        #     f"{self.user} ",
        #     f"({self.created_at:%Y-%m-%d %H:%M}): ",
        #     f"{self.body[:30]}..."
        # )
        return self.body[:30]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",  # To
        related_name="followed_by",  # Set the related name
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

# Create Profile for each new user
# post_save.connect(create_profile, sender=User)
