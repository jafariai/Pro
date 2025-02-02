from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms
from .models import ProgramRequest


class ProgramRequestForm(forms.ModelForm):
    class Meta:
        model = ProgramRequest
        fields = ['first_name', 'last_name', 'height', 'weight', 'disease_status', 'disease_description', 'waist', 'comments', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        disease_status = cleaned_data.get("disease_status")
        disease_description = cleaned_data.get("disease_description")

        if disease_status == "دارم" and not disease_description:
            self.add_error('disease_description', "لطفاً نوع بیماری را مشخص کنید.")

        return cleaned_data