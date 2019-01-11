from django.db import models
from django.forms import ModelForm
from .models import *

class DepositForm(ModelForm):
    class Meta:
        model = DepositSlip
        fields = '__all__'

class PledgeForm(ModelForm):
    class Meta:
        model = Pledges
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'

from django import forms


# from https://stackoverflow.com/questions/2770810/multiple-models-in-a-single-django-modelform


        class ConsumerRegistrationForm(CombinedFormBase):
    form_classes = [RegistrationForm, ConsumerProfileForm]

class RegisterView(FormView):
    template_name = "register.html"
    form_class = ConsumerRegistrationForm

    def form_valid(self, form):
        # some actions...
        return redirect(self.get_success_url())











# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)


# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#     birth_date = forms.DateField(required=False)
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
