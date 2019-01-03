from django import forms

class NameForm(forms.Form):
	Your_name = forms.CharField(label='Your name', max_length=100)