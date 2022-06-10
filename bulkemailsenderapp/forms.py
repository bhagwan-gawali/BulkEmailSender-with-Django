from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    to_email_list = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))



