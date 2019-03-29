from django.http import HttpResponse
from django.shortcuts import render

from .forms import BmiForm


def hello(request):
    return HttpResponse('Hello World')


# http://127.0.0.1:8000/bmi/?h=100&w=50
def bmi(request):
    form = BmiForm(request.POST or None)
    if form.is_valid():
        h = form.cleaned_data['h']
        w = form.cleaned_data['w']
        bmi = w / ((h / 100) ** 2)
        return render(request, 'bmi.html', {'bmi': bmi})

    return render(request, 'bmi-input.html', {'form': form})
