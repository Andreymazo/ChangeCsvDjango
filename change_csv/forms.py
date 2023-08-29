from django import forms

from change_csv.models import Sdelka


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()

from adaptor.model import CsvModel

class MyCSvModel(CsvModel):
    name = forms.CharField()
    
    class Meta:
         delimiter = ","
         dbModel = Sdelka
         
class SdelkaForm(forms.ModelForm):
    class Meta:
        model = Sdelka
        fields = '__all__'
