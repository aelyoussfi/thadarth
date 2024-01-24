from .models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set label for 'content' field to an empty string
        self.fields['content'].label = ''


