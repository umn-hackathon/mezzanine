from django import forms

from .models import Proyek, Step1, Step2


class ProyekForm(forms.ModelForm):
    class Meta:
        model = Proyek
        fields = ('nama_proyek',)

class Step1Form(forms.ModelForm):
    class Meta:
        model = Step1
        exclude = ('proyek',)

class Step2Form(forms.ModelForm):
    class Meta:
        model = Step2
        exclude = ('proyek',)