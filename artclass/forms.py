from django import forms
from .models import Booking

class ArtClassBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number']