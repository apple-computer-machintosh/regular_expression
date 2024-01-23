from django import forms
class RegexForm(forms.Form):
    name = forms.CharField(label="名前を入力")
    age = forms.CharField(label="年齢を入力")
    zip_code = forms.CharField(label="郵便番号を入力")
    cell_phone = forms.CharField(label="電話番号を入力")
