from django.forms import ModelForm
from .models import registration


class PostForm(ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
