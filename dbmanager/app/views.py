from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from .forms import SequenceInputForm
# Create your views here.

def home(request):
    return render_to_response('index.html')

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