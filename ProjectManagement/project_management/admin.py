from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'id_type_customer', 'phone', 'mail')
    fields = ['id_type_customer', 'customer', ('phone', 'mail')]
    list_filter = ('id_type_customer',)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_contract', 'id_customer', 'comment', 'status', 'link_file', 'date_start', 'date_end')
    fields = ['num_contract', 'id_customer', 'comment', 'status', 'link_file', ('date_start', 'date_end')]
    list_filter = ('status',)


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'surname', 'name', 'patronymic', 'link_photo', 'id_position', 'experience', 'gender',
        'date_birth', 'phone', 'mail')
    fields = [('surname', 'name', 'patronymic'), 'link_photo', ('experience', 'id_position'),
              ('date_birth', 'gender'), ('phone', 'mail')]
    list_filter = ('id_position', 'gender')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'id_contract', 'id_type', 'description', 'date_start', 'date_end')
    fields = ['id_contract', 'id_type', 'project_name', 'description', ('date_start', 'date_end')]
    list_filter = ('id_type',)


class ProblemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_project', 'id_task', 'problem', 'description', 'date_start_plan', 'date_end_plan',
        'date_start_actual', 'date_end_actual', 'status')
    fields = ['id_project', 'id_task', 'problem', 'description', ('date_start_plan', 'date_end_plan'),
              ('date_start_actual', 'date_end_actual'), 'status']
    list_filter = ('id_task', 'status')


class Project_participantAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_project', 'id_worker', 'status')
    list_filter = ('status',)


class DoerAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_problem', 'id_participant')


admin.site.register(Type_customer)
admin.site.register(Type_project)
admin.site.register(Task)
admin.site.register(Position)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Project_participant, Project_participantAdmin)
admin.site.register(Doer, DoerAdmin)
