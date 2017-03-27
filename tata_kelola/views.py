from django.shortcuts import render

from .forms import Step1Form


def step1(request, template_name):
    form = Step1Form()
    context = {'form': form}
    return render(request, template_name, context)

def step2(request, template_name):
    form = Step1Form()
    context = {'form': form}
    return render(request, template_name, context)