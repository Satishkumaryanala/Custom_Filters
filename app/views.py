from django.shortcuts import render

# Create your views here.

def Custom_filters(request):
    data1 = 'This is Python class'
    data2 = 'tHIS vERY difficult iF nOT pRACTICE'
    d={'data1':data1,'data2':data2}
    return render(request,'Custom_filters.html',d)