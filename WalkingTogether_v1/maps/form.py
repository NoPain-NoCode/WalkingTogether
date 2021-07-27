from django import forms
from django.db.models import fields
from .models import WalkingTrails

class PostForm(forms.ModelForm):

    class Meta:
        model = WalkingTrails
        fields = ('latitude', 'longitude')