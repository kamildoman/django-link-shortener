from django.db.models.base import Model
from django.forms import ModelForm
from .models import URLShortener

class URLForm(ModelForm):
    class Meta:
        model = URLShortener
        fields = ["url"]
        labels = {
            "url": "Your link: ",
        }
    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'class': 'urlclass'})