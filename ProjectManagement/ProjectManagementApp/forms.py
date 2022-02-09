from django import forms
#from django.forms import ModelForm
from .models import Enrichment,Csvs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from django.core.validators import FileExtensionValidator

class NewEnrichmentForm(forms.ModelForm):
    class Meta:
        model = Enrichment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class EditEnrichmentForm(forms.ModelForm):
    class Meta:
        model = Enrichment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

            
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
    
'''class UploadDisasterForm(forms.ModelForm):
    class Meta:
        model=Csvs'''
        

'''class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csvs
        fields = ('disaster_file',)

class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")'''