from django import forms

class ArtClassBookingForm(forms.Form):
    # Add any additional fields you need for the booking form
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone_number = forms.CharField(max_length=15, label='Your Phone Number')