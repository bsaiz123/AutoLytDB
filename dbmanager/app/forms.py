import csv
from io import TextIOWrapper

from django import forms

from .models import Sequences, Domains


class SequenceInputForm(forms.Form):
    CHOICES = [('domain', 'Domain File'),
               ('sequences', 'Sequences File')]
    file_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    file = forms.FileField(required=False)

    def __init__(self,*args,**kwargs):
        super(SequenceInputForm, self).__init__(*args, **kwargs)
        self.initial['file_type'] = 'domain'

    def clean_file(self):
        value = self.cleaned_data["file"]
        print("clean_file value: %s" % value)
        return value

    def save(self):
        f = self.cleaned_data["file"]
        file_type = self.cleaned_data["file_type"]
        f = TextIOWrapper(self.cleaned_data["file"].file, encoding='utf-8')
        # print(f)
        records = csv.reader(f)
        # print(records)
        count = 0
        for line in records:
            if line[0].isdigit():
                count +=1
                if count % 1000 == 0:
                    print('Processed %s rows so far.'%count)
                if file_type == 'sequences':
                    input_data,created = Sequences.objects.get_or_create(id=line[0])
                    # input_data.id = line[0]
                    input_data.accession_number = line[1]
                    input_data.genus = line[2]
                    input_data.protein_desc = line[3]
                    input_data.sequence = line[4]
                    input_data.save()
                else:
                    input_data,created = Domains.objects.get_or_create(id=line[0])
                    # input_data.id = line[0]
                    input_data.accession_number = line[1]
                    input_data.genus = line[2]
                    input_data.domain_model= line[3]
                    input_data.domain_description= line[4]
                    # print(line[5])
                    input_data.independent_eval= line[5]
                    input_data.first= line[6]
                    input_data.last= line[7]
                    input_data.save()
