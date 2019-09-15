from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('P', 'Paypal'),
    ('S', 'Stripe')
)
class CheckoutForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    zip = forms.CharField()
    same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)