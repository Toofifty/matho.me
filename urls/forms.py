from django import forms

class URLForm(forms.Form):
    short_url = forms.CharField(max_length=20)
    long_url = forms.CharField()