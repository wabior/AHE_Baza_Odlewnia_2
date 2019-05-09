from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App_Baza.models import Production, Machine
from django.db.models import Sum
from App_Baza.forms import MachineForm, NowyRaport, NewUser
from datetime import datetime

# Create your views here.

# def index(request):
#     total = Production.objects.all().aggregate(Sum('Production_Value'))['Production_Value__sum']
#     return HttpResponse(total)


# def index(request):
#     total = Production.objects.all().aggregate(Sum('Production_Value'))['Production_Value__sum']
#     context = {'total': total}
#     return render(request, 'index.html', context)

def index(request):
    template = loader.get_template('index.html')
    total = Production.objects.all().aggregate(Sum('Production_Value'))['Production_Value__sum']
    context = {'total': total}
    return HttpResponse(template.render(context, request))

def nowy_raport(request):
    maszyna = Machine.objects.get(pk=1)
    # b = Production(shift_date=datetime.now, Machine=maszyna ,Production_Value=166)
    # b.save()
    return render(request, 'nowy_raport.html',{})

def topbar(request):
    template = loader.get_template('topbar.html')
    return render(request,'topbar.html',{'topbar':topbar})
    #request, 'topbar.html', {'topbar': topbar}

def machine_create_view(request):
    form = MachineForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'machine_create.html',context)

def raport_view(request):
    form = NowyRaport(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'raport.html',context)
NewUser
def NewUser_view(request):
    form = NewUser(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'NewUser.html',context)