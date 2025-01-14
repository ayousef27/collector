from django.forms import ModelForm
from .models import Oil

class OilForm(ModelForm):
  class Meta:
    model = Oil
    fields = ['date', 'type']