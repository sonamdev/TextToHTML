from django import forms

class TextToHtmlForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea)
