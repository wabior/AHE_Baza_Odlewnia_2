from django import forms

from .models import Machine, Production, User

class MachineForm(forms.ModelForm):
     class Meta:
         model = Machine
         fields = [
             'Code_Name',
             'Name',
             'Status',
             'Form_Forms',
             'Current_Shoots',
             'Total_Shoots',
         ]

class NowyRaport(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            'shift_date',
            'Machine',
            'Production_Value',
        ]

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Personal_Nr',
            'User_Level',
        ]