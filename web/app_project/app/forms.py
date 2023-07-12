from django.forms import ModelForm, widgets
from .models import Messagelog

class MessageLogForm(ModelForm):
    class Meta: 
        model = Messagelog
        fields = ['yearreg', 'state', 'date_rcv', 'type_doc', 'custom', 'pto', 'declarant_unp']

        widgets = {
            'date_rcv': widgets.DateInput(attrs={'type': 'date', 'placeholder':""})
        }

     