from django import forms


class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 50}), max_length=1999960)


class CodeResultForm(forms.Form):
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), max_length=500)
