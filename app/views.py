from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def fbv_string(request):
    return HttpResponse('this is fbv string as response')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is cbv string as response')

def fbv_template(request):
    return render(request,'fbv_template.html')

class cbv_template(View):
    def get(self,request):
        return render(request,'cbv_template.html')


def fbv1(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('insertion done successfully!!!!!')
    return render(request,'fbv1.html',d)


class cbv1(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv1.html',d)

    def post(self,request):
        SFD=StudentForm(request.POST)
        SFD.save()
        return HttpResponse('insertion done successfully!!!')

# class temp(TemplateView):
    # template_name='temp.html'