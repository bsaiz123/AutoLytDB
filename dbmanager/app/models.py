from django.db import models

# Create your models here.


class Domains(models.Model):
    id = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    domain_model = models.CharField(max_length=100)
    domain_description = models.CharField(max_length=2000)
    independent_eval = models.FloatField()
    first = models.IntegerField()
    last = models.IntegerField()


    def __repr__(self):
        return self.accession_number

class Sequences(models.Model):
    id = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    protein_desc = models.CharField(max_length=2000)
    sequence = models.CharField(max_length=5000)

    def __repr__(self):
        return self.accession_number