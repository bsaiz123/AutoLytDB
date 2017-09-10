from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from .models import *
from .forms import SequenceInputForm
# Create your views here.

def home(request):
    return render_to_response('index.html')

def sequences(request):
    seq_objs = Sequences.objects.all()
    seq_data = [x.serialize for x in seq_objs]
    data = {'data':seq_data,'recordsTotal':len(seq_data),'recordsFiltered':len(seq_data)}
    return JsonResponse(data)

def domains(request):
    search = request.GET.get('search[value]')
    if search:

        domain_objs = Domains.objects.filter( Q(accession_number__icontains=search)
                                            | Q(genus__icontains=search) | Q(domain_model__icontains=search)
                                            | Q(domain_description__icontains=search)
                                            )
        if search.isdigit():
            domain_objs = domain_objs.filter(Q(id__like=search) | Q(independent_eval__like=search)| Q(first__like=search)| Q(last__like=search))
        domain_objs = domain_objs.all()
    else:
        domain_objs = Domains.objects.all()
    domain_data = [x.serialize for x in domain_objs]
    data = {'data':domain_data,'recordsTotal':len(domain_data),'recordsFiltered':len(domain_data)}
    return JsonResponse(data)

def import_seq(request):
    print(request.POST)
    if request.method == 'POST':
        form = SequenceInputForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            return render(request, 'import.html', {'seq_form': form})
    else:
        return render(request,'import.html',{'seq_form':SequenceInputForm(request.POST or None)})