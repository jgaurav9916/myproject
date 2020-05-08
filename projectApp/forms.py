from django import forms

class ContactForms(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "enter the 6-digit roll number")
    email = forms.EmailField(label = "E-Mail")
    password = forms.CharField(widget = forms.PasswordInput())

