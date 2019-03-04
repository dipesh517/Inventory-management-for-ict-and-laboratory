from django import forms

class addQuantityForm(forms.Form):
    Quantity=forms.IntegerField()
    Room=forms.IntegerField(required=False)
