from .models import MyModel, MyModelDate, MyModelDateHj
from django.forms import ModelForm


class VariaveisForm(ModelForm):
    class Meta:
        model = MyModelDateHj
        fields = '__all__'
