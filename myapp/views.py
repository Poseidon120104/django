from django.shortcuts import render
from django.http import HttpResponse
from .models import Features
# Create your views here.
def index(request):
    feature1=Features()
    feature1.id = 0
    feature1.name='Fast'
    feature1.details='Our Service is very quick'
    feature1.isbool = True

    feature2=Features()
    feature2.id = 0
    feature2.name='Fast'
    feature2.details='Our Service is very reliable'
    feature2.isbool = False

    feature3=Features()
    feature3.id = 0
    feature3.name='Fast'
    feature3.details='Our Service is easy to use'
    feature3.isbool = False

    feature4=Features()
    feature4.id = 0
    feature4.name='Fast'
    feature4.details='Our Service is very affordable'
    feature4.isbool = True

    features=[feature1,feature2,feature3,feature4]

    # return render(request,'index.html',{'feature1':feature1, 'feature2':feature2, 'feature3':feature3, 'feature4':feature4})
    return render(request,'index.html',{'features':features})

def counter(request):
    text = request.POST['text']

    amount_of_words = len(text.split())
    return render(request, 'counter.html',{'amount':amount_of_words} )