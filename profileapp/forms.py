from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
     class Mete:
         model = Profile
         fields = ['image','nickname','message']