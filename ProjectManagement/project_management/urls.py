from django.conf.urls import include, re_path
from . import views

urlpatterns = [
    # Гость
    re_path(r'^$', views.index, name='index'),
    # ---Регистрация
    re_path(r'^registration$', views.registration, name='registration'),
    # ---Просмотр списка сотрудников
    re_path(r'^workers$', views.workers, name='workers'),
    # ---Просмотр информации о выбраном сотруднике
    re_path(r'^workerPage(?P<user>\d+)$', views.workerPage, name='workerPage'),
    # ---Информация о сайте
    re_path(r'^information$', views.information, name='information'),
    # Директор
    re_path(r'^homePageDirector$', views.PageDirector, name='PageDirector'),
    # ---Информация о сайте
    re_path(r'^informationDirector$', views.informationDirector, name='informationDirector'),
    # ---Просмотр списка контрактов и добавление новых контрактов
    re_path(r'^viewContracts$', views.viewContracts, name='viewContracts'),
    # ---Изменение информации о выбраном договоре
    re_path(r'^updateContract(?P<contract>\d+)$', views.updateContract, name='updateContract'),
    # ---Просмотр списка проектов и сортировка проектов
    re_path(r'^projectsSorting$', views.projectsSorting, name='projectsSorting'),
    # ---Просмотр списка заказчиков и добавление новых заказчиков
    re_path(r'^viewCustomers$', views.viewCustomers, name='viewCustomers'),
    # ---Изменение информации о выбраном заказчике
    re_path(r'^updateCustomer(?P<customer>\d+)$', views.updateCustomer, name='updateCustomer'),
    # ---Просмотр информации о контракте и проектов по контракту, добавление новых проектов
    re_path(r'^viewProjects(?P<contract>\d+)$', views.viewProjects, name='viewProjects'),
    # ---Изменение информации о выбраном проекте
    re_path(r'^updateProject(?P<project>\d+)$', views.updateProject, name='updateProject'),
    # ---Просмотр информации о задачах проекта и добавление новых задач в проект
    re_path(r'^problemProject(?P<project>\d+)$', views.problemProject, name='problemProject'),
    # ---Изменение информации о выбраной задаче
    re_path(r'^updateProblem(?P<problem>\d+)$', views.updateProblem, name='updateProblem'),
    # ---Просмотр списка сотрудников
    re_path(r'^workersDirector$', views.workersDirector, name='workersDirector'),
    # ---Просмотр информации о выбраном сотруднике
    re_path(r'^userPage(?P<user>\d+)$', views.userPage, name='userPage'),
    # ---Просмотр информации о проекте и добавление участников
    re_path(r'^projectParticipant(?P<project>\d+)$', views.projectParticipant, name='projectParticipant'),
]
