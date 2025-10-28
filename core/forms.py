from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Donor, BloodBank, BloodRequest, Donation

class UserRegisterForm(UserCreationForm):
    is_donor = forms.BooleanField(required=False, label='Register as a Donor')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('is_donor', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_donor']:
            user.is_donor = True
        else:
            user.is_admin = True  # Default to admin if not donor
        if commit:
            user.save()
            if user.is_donor:
                Donor.objects.create(user=user)
        return user


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'date_of_birth', 'last_donation_date', 'phone_number', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BloodBankForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name', 'location', 'contact_number', 'email']


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_group', 'units_required', 'urgency']


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor', 'blood_bank', 'blood_group', 'units_donated', 'status']
