from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('patronymic', 'id_position', 'experience', 'gender', 'date_birth', 'phone')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer', 'id_type_customer', 'phone', 'mail')


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('num_contract', 'id_customer', 'comment', 'status', 'link_file', 'date_start', 'date_end')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'id_type', 'description', 'date_start', 'date_end')


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = (
            'problem', 'id_task', 'description', 'date_start_plan', 'date_end_plan', 'date_start_actual',
            'date_end_actual',
            'status')


class Project_participantForm(forms.ModelForm):
    class Meta:
        model = Project_participant
        fields = ('id_project', 'id_worker', 'status')
