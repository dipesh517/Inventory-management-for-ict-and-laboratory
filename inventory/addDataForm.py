from django.forms import ModelForm
from .models import Computer,Laptop,NetworkSwitch,Printer,AdditionalItem
from django import forms

# Create the form class.
class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'model', 'cost', 'room','date_of_acquire','status']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'model':forms.TextInput(attrs={'class':'form-control'}),
        }

        def save(self,commit=True):
            obj = super(ComputerForm,self).save(commit =False)
            obj.name = self.cleaned_data['name']
            obj.model = self.cleaned_data['model']
            obj.cost = self.cleaned_data['cost']
            obj.room = self.cleaned_data['room']
            obj.date_of_acquire = self.cleaned_data['date_of_acquire']
            obj.status = self.cleaned_data['status']

            if commit:
                obj.save()
            return obj




class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'model', 'cost', 'room','date_of_acquire','status']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'model':forms.TextInput(attrs={'class':'form-control'}),
        }
        def save(self,commit=True):
            obj = super(LaptopForm,self).save(commit =False)
            obj.name = self.cleaned_data['name']
            obj.model = self.cleaned_data['model']
            obj.cost = self.cleaned_data['cost']
            obj.room = self.cleaned_data['room']
            obj.date_of_acquire = self.cleaned_data['date_of_acquire']
            obj.status = self.cleaned_data['status']

            if commit:
                obj.save()
            return obj



class NetworkSwitchForm(ModelForm):
    class Meta:
        model = NetworkSwitch
        fields = ['name', 'model', 'cost', 'room','date_of_acquire','status','no_of_ports','no_of_SFP_ports']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'model':forms.TextInput(attrs={'class':'form-control'}),
        }

        def save(self,commit=True):
            obj = super(NetworkSwitchForm,self).save(commit =False)
            obj.name = self.cleaned_data['name']
            obj.model = self.cleaned_data['model']
            obj.cost = self.cleaned_data['cost']
            obj.room = self.cleaned_data['room']
            obj.date_of_acquire = self.cleaned_data['date_of_acquire']
            obj.status = self.cleaned_data['status']
            obj.no_of_ports = self.cleaned_data['no_of_ports']
            obj.no_of_SFP_ports = self.cleaned_data['no_of_SFP_ports']

            if commit:
                obj.save()
            return obj

class AdditionalItemForm(ModelForm):
    class Meta:
        model = AdditionalItem
        fields = ['name', 'model', 'cost', 'room','date_of_acquire','status']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'model':forms.TextInput(attrs={'class':'form-control'}),
        }
        def save(self,commit=True):
            obj = super(AdditionalItemForm,self).save(commit =False)
            obj.name = self.cleaned_data['name']
            obj.model = self.cleaned_data['model']
            obj.cost = self.cleaned_data['cost']
            obj.room = self.cleaned_data['room']
            obj.date_of_acquire = self.cleaned_data['date_of_acquire']
            obj.status = self.cleaned_data['status']

            if commit:
                obj.save()
            return obj

class PrinterForm(ModelForm):
    class Meta:
        model = Printer
        fields = ['name', 'model', 'cost', 'room','date_of_acquire','status','ip_address']
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'model':forms.TextInput(attrs={'class':'form-control'}),
        }
        def save(self,commit=True):
            obj = super(PrinterForm,self).save(commit =False)
            obj.name = self.cleaned_data['name']
            obj.model = self.cleaned_data['model']
            obj.cost = self.cleaned_data['cost']
            obj.room = self.cleaned_data['room']
            obj.date_of_acquire = self.cleaned_data['date_of_acquire']
            obj.status = self.cleaned_data['status']
            obj.ip_address = self.cleaned_data['ip_address']

            if commit:
                obj.save()
            return obj
