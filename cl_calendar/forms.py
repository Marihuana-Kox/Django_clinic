from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from cl_calendar.models import RegistrationDate


class RegistrationDateForm(ModelForm):
    class Meta:
        model = RegistrationDate
        fields = ['phone', 'surname', 'name', 'patronymic', 'dob', 'diagnos']