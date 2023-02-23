from .models import MyModel, MyModelDate
from django.forms import ModelForm

class VariaveisForm(ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

class VariaveisForm(ModelForm):
    class Meta:
        model = MyModelDate
        fields = '__all__'
