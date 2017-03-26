from django import forms

from .models import Proyek, Step1


class ProyekForm(forms.ModelForm):
    class Meta:
        model = Proyek
        fields = ('nama_proyek',)

class Step1Form(forms.ModelForm):
    class Meta:
        model = Step1
        exclude = ('proyek',)