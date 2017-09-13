from django.db import models

# Create your models here.


class Domains(models.Model):
    id = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    domain_model = models.CharField(max_length=100)
    domain_description = models.CharField(max_length=2000)
    independent_eval = models.FloatField(default=0)
    first = models.CharField(max_length=15)
    last = models.CharField(max_length=15)


    def __repr__(self):
        return self.accession_number

    @property
    def serialize(self):
        return {
            "id":self.id,
            "accession_number":self.accession_number,
            "genus" : self.genus,
            "domain_model" : self.domain_model,
            "domain_description":self.domain_description,
            "independent_eval":self.independent_eval,
            "first":self.first,
            "last":self.last
        }

class Sequences(models.Model):
    id = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    protein_desc = models.CharField(max_length=2000)
    sequence = models.CharField(max_length=5000)

    def __repr__(self):
        return self.accession_number

    @property
    def serialize(self):
        return {
            "id":self.id,
            "accession_number":self.accession_number,
            "genus" : self.genus,
            "protein_desc" : self.protein_desc,
            "sequence":self.sequence,
        }
