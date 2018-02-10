from django import forms
from .models import Workshop, Participant, Facilitator

class RegForm(forms.ModelForm):


    class Meta:
        model = Participant
        fields = ('fname', 'lname','email_address', 'institution', 'country', 'Address', 'gender', 'reg_date','workshopid',)