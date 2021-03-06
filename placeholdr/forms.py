from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from placeholdr.models import UserProfile, Place, Trip


class SubmitPlaceForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=128)
    desc = forms.CharField(required=False, max_length=400, label="Description")

    class Meta:
        model = Place
        fields = ('name', 'desc', 'picLink', 'position')
        labels = {
            'picLink': _('Picture of your Place'),
        }
        widgets = {
            'picLink': forms.FileInput(attrs={'class': 'custom-file', 'id': "customFile"}),
        }


class SubmitTripForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=128)
    desc = forms.CharField(required=False, max_length=400, label="Description")

    class Meta:
        model = Trip
        fields = ('name', 'desc', 'picLink')
        labels = {
            'picLink': _('Picture for your Trip'),
        }
        widgets = {
            'picLink': forms.FileInput(attrs={'class': 'custom-file', 'id': "customFile"}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password',)


class UserProfileForm(forms.ModelForm):
    favPlace = forms.ModelChoiceField(queryset=Place.objects.all(), required=False, label="Favourite Place")
    recommendedTrip = forms.ModelChoiceField(queryset=Trip.objects.all(), required=False, label="Recommended Trip")

    class Meta:
        model = UserProfile
        fields = ('bio', 'livesIn', 'picture', 'favPlace', 'recommendedTrip')
        labels = {
            'bio': _('Tell us about yourself!'),
            'livesIn': _('Where do you live?')
        }
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'custom-file', 'id': "customFile"}),
        }


class ChangeUserForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email')


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password', 'new_password', 'confirm_new_password')
