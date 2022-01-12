from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Tweet your thinking...",
                "class": "textarea is-success is-medium",
            },
        ),
        label="",
    )

    class Meta:
        model = Tweet
        exclude = ("user",)
