from django import forms
from django.forms import Textarea

from .models import Machine, Production, User

class MachineForm(forms.ModelForm):
     class Meta:
         model = Machine
         fields = [
             'Code_Name', 'Name','Status',
             'Form_Forms','Current_Shoots','Total_Shoots',]
         labels = {
             'Code_Name':       'numer maszyny            :',
             'Name':            'nazwa maszyny            :',
             'Status':          'status                   :',
             'Form_Forms':      'forma                    :',
             'Current_Shoots':  'aktualna liczba strzałów :',
             'Total_Shoots':    'całkowita liczba strzałów:'
         }

class NowyRaport(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            'shift_date',
            'Machine',
            'Production_Value',
        ]
        labels = {
            'shift_date'        :'data',
            'Machine'           :'nazwa maszyny',
            'Production_Value'  :'wyprodukowano',
        }
class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Personal_Nr',
            'User_Level',
        ]
        labels = {
            'Personal_Nr'   :'numer personalny',
            'User_Level'    :'poziom uprawnień',
        }
        # widgets = {'Personal_Nr': Textarea(attrs={'cols': 8, 'rows': 1})}