from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from .models import *
from .forms import SequenceInputForm
# Create your views here.

import traceback

def home(request):
    return render_to_response('index.html')

def sequences(request):
    length = int(request.GET.get('length','25'))
    start = int(request.GET.get('start','0'))
    filters = None
    order_dir = request.GET.get('order[0][dir]','asc')
    order_dir = '-' if order_dir != 'asc' else ''
    order_col = int(request.GET.get('order[0][column]',0))
    order_col = Sequences._meta.fields[order_col].name
    order = order_dir + order_col
    try:
        for x in range(0,8):
            key = 'columns[%s][search][value]'%x
            value = request.GET.get(key)
            # print('Search value %s for column %s'%(value,x))
            if value and len(value) > 0:
                if x == 0:
                    filters = filters & Q(id=int(value)) if filters else Q(id=int(value))
                elif x == 1:
                    filters = filters & Q(accession_number__icontains=value) if filters else Q(accession_number__icontains=value)
                elif x == 2:
                    filters = filters & Q(genus__icontains=value) if filters else Q(genus__icontains=value)
                elif x == 3:
                    filters = filters & Q(protein_desc__icontains=value) if filters else Q(protein_desc__icontains=value)
                elif x == 4:
                    filters = filters & Q(sequence__icontains=value) if filters else Q(sequence__icontains=value)
    except:
        traceback.print_exc()
    if filters:
        seq_objs = Sequences.objects.filter(filters).order_by(order).all()
    else:
        seq_objs = Sequences.objects.order_by(order).all()
    paginator = Paginator(seq_objs, length)
    print('Start %s, length %s'%(start,length))
    pagenum = max(int(start/length),1)
    # print('Page Num %s'%pagenum)
    page = paginator.page(pagenum)

    seq_data = [x.serialize for x in page]
    data = {'data':seq_data,'recordsTotal':Sequences.objects.all().count()
        ,'recordsFiltered':len(seq_data)}
    return JsonResponse(data)

def domains(request):
    length = int(request.GET.get('length','25'))
    start = int(request.GET.get('start','0'))
    order_dir = request.GET.get('order[0][dir]','asc')
    order_dir = '-' if order_dir != 'asc' else ''
    order_col = int(request.GET.get('order[0][column]',0))
    order_col = Domains._meta.fields[order_col].name
    order = order_dir + order_col
    filters = None
    try:
        for x in range(0,8):
            key = 'columns[%s][search][value]'%x
            value = request.GET.get(key)
            print('Search value %s for column %s'%(value,x))
            if value and len(value) > 0:
                if x == 0:
                    filters = filters & Q(id=int(value)) if filters else Q(id=int(value))
                elif x == 1:
                    filters = filters & Q(accession_number__icontains=value) if filters else Q(accession_number__icontains=value)
                elif x == 2:
                    filters = filters & Q(genus__icontains=value) if filters else Q(genus__icontains=value)
                elif x == 3:
                    filters = filters & Q(domain_model__icontains=value) if filters else Q(domain_model__icontains=value)
                elif x == 4:
                    filters = filters & Q(domain_description__icontains=value) if filters else Q(domain_description__icontains=value)
                elif x == 5:
                    filters = filters & Q(independent_eval=float(value)) if filters else Q(independent_eval=float(value))
                elif x == 6:
                    filters = filters & Q(first__icontains=value) if filters else Q(first__icontains=value)
                elif x == 7:
                    filters = filters & Q(last__icontains=value) if filters else Q(last__icontains=value)
    except:
        traceback.print_exc()
    # print(filters)
    if filters:
        domain_objs = Domains.objects.filter(filters).order_by(order).all()
    else:
        domain_objs = Domains.objects.order_by(order).all()
    paginator = Paginator(domain_objs, length)
    print('Start %s, length %s'%(start,length))
    pagenum = max(int(start/length),1)
    # print('Page Num %s'%pagenum)
    page = paginator.page(pagenum)
    domain_data = [x.serialize for x in page]
    data = {'data':domain_data,'recordsTotal':Domains.objects.all().count(),
            'recordsFiltered':len(domain_data)}
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