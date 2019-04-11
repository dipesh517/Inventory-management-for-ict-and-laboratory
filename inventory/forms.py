from django import forms
from django.forms import ModelForm
from .models import Item,Room,Floor,Categorie


class addCategoryForm(forms.Form):
    categoryName = forms.CharField(max_length=30)
    extraField1 = forms.CharField(max_length=30, required=False)
    extraField2 = forms.CharField(max_length=30, required=False)
    extraField3 = forms.CharField(max_length=30, required=False)


class addItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.extra_fields_dict = kwargs.pop('extra_fields_dict')
        super().__init__(*args, **kwargs)
        for key, value in self.extra_fields_dict.items():
            self.fields[value] = forms.CharField(required=False)
        for field in self.Meta.Notrequired:
            self.fields[field].required = False


    class Meta:
        model = Item
        fields = ['name', 'model', 'cost_per_item', 'room',
                  'date_of_acquire', 'working', 'in_maintenance', 'out_of_order']
        Notrequired = ['room','cost_per_item']


class addExistingForm(forms.Form):
    quantity = forms.IntegerField(required=True)


class allocateForm(ModelForm):
    working = forms.IntegerField(required=False)
    out_of_order = forms.IntegerField(required=False)
    in_maintenance = forms.IntegerField(required=False)

    class Meta:
        model = Item
        fields = ['room']

class addRoomForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.Meta.Notrequired:
            self.fields[field].required = False
    class Meta:
        model = Room
        fields = '__all__'
        Notrequired = ['room_name']

class addFloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = '__all__'

class categoryEditForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['category_name']
