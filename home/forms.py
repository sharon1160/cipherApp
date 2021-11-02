from django import forms

class TextTransForm(forms.Form):
  key = forms.CharField(label='Clave ', max_length=500)
  plain_text = forms.CharField(label='Texto Plano ',widget=forms.Textarea(attrs={'rows':3}))

class TextPlayfairForm(forms.Form):
  key = forms.CharField(label='Clave ', max_length=500)
  text_cipher = forms.CharField(label='Texto Cifrado ',widget=forms.Textarea(attrs={'rows':3}))

class TextCesarForm(forms.Form):
  key = forms.CharField(label='Clave ', max_length=500)
  text_cipher = forms.CharField(label='Texto Cifrado ',widget=forms.Textarea(attrs={'rows':3}))



