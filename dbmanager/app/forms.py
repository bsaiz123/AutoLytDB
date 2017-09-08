import csv

from django.forms import forms

from .models import Sequences

class SequenceInputForm(forms.Form):
    file = forms.FileField(required=False)

    def clean_file(self):
        value = self.cleaned_data["file"]
        print("clean_file value: %s" % value)
        return value

    def save(self):
        f = self.cleaned_data["file"]
        print('File %s'%type(f))
        records = csv.reader(self.cleaned_data["file"].read())
        for line in records:
            input_data = Sequences()
            input_data.id = line[0]
            input_data.accession_number = line[1]
            input_data.genus = line[2]
            input_data.protein_desc = line[3]
            input_data.sequence = line[4]
            input_data.save()