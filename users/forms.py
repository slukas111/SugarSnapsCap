from django import forms

from users.models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'bio',
            'location'
            ]


