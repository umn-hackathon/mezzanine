from django.shortcuts import render

from .forms import Step1Form, Step2Form, Step3Form, Step4Form, Step5Form


def step1(request, template_name):
    form = Step1Form()
    context = {'form': form}
    return render(request, template_name, context)

def step2(request, template_name):
    form = Step2Form()
    context = {'form': form}
    return render(request, template_name, context)

def step3(request, template_name):
    form = Step3Form()
    context = {'form': form}
    return render(request, template_name, context)

def step4(request, template_name):
    form = Step4Form()
    context = {'form': form}
    return render(request, template_name, context)

def step5(request, template_name):
    form = Step5Form()
    context = {'form': form}
    return render(request, template_name, context)