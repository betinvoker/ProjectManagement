from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Главная страница гостя
def index(request):
    projects = Project.objects.all().order_by('id')
    return render(request, 'Guest/homePage.html', {"projects": projects})


# Информация о сайте
def information(request):
    return render(request, 'Guest/information.html')


# Регистрация
def registration(request):
    if request.method == "POST":
        userform = UserForm(instance=request.user)
        if userform.is_valid():
            userform.save()
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm(instance=request.user)
    return render(request, 'Guest/registration.html', {"userform": userform})


# Список работников
def workers(request):
    workers = Worker.objects.all().order_by('id')
    return render(request, 'Guest/workers.html', context={"workers": workers})


# Просмотр информации о выбраном сотруднике
def workerPage(request, user):
    user = Worker.objects.get(id=user)
    return render(request, 'Guest/workerPage.html', context={"user": user})


# Главная страница Директора
def PageDirector(request):
    projects = Project.objects.all().order_by('id')
    return render(request, 'Director/homePageDirector.html', {"projects": projects})


# Информация о сайте
def informationDirector(request):
    return render(request, 'Director/informationDirector.html')


# Список Заказчиков и добавление новых Заказчиков
def viewCustomers(request):
    customerform = CustomerForm(request.POST)
    if request.method == "POST":
        if customerform.is_valid():
            customerform.save()
            customerform = CustomerForm()
        else:
            return HttpResponse("Invalid data")
    customers = Customer.objects.all().order_by('id')
    return render(request, 'Director/viewCustomers.html',
                  context={"customers": customers, "customerform": customerform})


# Список Договоров и добовление новых Договоров
def viewContracts(request):
    contractform = ContractForm(request.POST)
    if request.method == "POST":
        if contractform.is_valid():
            contractform.save()
            contractform = ContractForm()
        else:
            return HttpResponse("Invalid data")
    contracts = Contract.objects.all().order_by('id')
    return render(request, 'Director/viewContracts.html', {"contracts": contracts, "contractform": contractform})


# Список проектов и сортировка проектов
def projectsSorting(request):
    projects = Project.objects.all().order_by('id')
    return render(request, 'Director/projectsSorting.html', context={"projects": projects})


# Список проектов по договору и добавление новый проектов
def viewProjects(request, contract):
    cur_contract = Contract.objects.get(id=contract)
    projects = Project.objects.filter(id_contract=cur_contract)
    projectform = ProjectForm(request.POST)
    if request.method == "POST":
        if projectform.is_valid():
            item = projectform.save(commit=False)
            item.id_contract = cur_contract
            item.save()
            projectform = ProjectForm()
    return render(request, 'Director/viewProjects.html',
                  context={"contract": cur_contract, "projects": projects, "projectform": projectform})


# Список задач по проекту и добавление новых задач в проект
def problemProject(request, project):
    cur_project = Project.objects.get(id=project)
    problems = Problem.objects.filter(id_project=cur_project)
    problemform = ProblemForm(request.POST)
    if request.method == "POST":
        if problemform.is_valid():
            item = problemform.save(commit=False)
            item.id_project = cur_project
            item.save()
            problemform = ProblemForm()
    return render(request, 'Director/problemProject.html',
                  context={"project": cur_project, "problems": problems, "problemform": problemform})


# Список работников
def workersDirector(request):
    workers = Worker.objects.all().order_by('id')
    return render(request, 'Director/workersDirector.html', context={"workers": workers})


# Просмотр информации о выбраном сотруднике
def userPage(request, user):
    user = Worker.objects.get(id=user)
    return render(request, 'Director/userPage.html', context={"user": user})


# Список участников проекта и добавление новый участников
def projectParticipant(request, project):
    cur_project = Project.objects.get(id=project)
    workers = Worker.objects.all().order_by('id')
    participants = Project_participant.objects.filter(id_project=cur_project)
    project_participantForm = Project_participantForm(request.POST)
    if request.method == "POST":
        if project_participantForm.is_valid():
            item = project_participantForm.save(commit=False)
            item.id_project = cur_project
            item.save()
            project_participantForm = Project_participantForm()
        else:
            return HttpResponse("Invalid data")
    return render(request, 'Director/Project_participant.html',
                  context={"participants": participants, "workers": workers, "project": cur_project,
                           "participantForm": project_participantForm})


# ------Изменение------
# Изменение информации о выбраном заказчике
def updateCustomer(request, customer):
    cur_customer = Customer.objects.get(id=customer)
    if request.method == "POST":
        customerform = CustomerForm(request.POST, instance=cur_customer)
        if customerform.is_valid():
            item = customerform.save(commit=False)
            item.save()
    else:
        customerform = CustomerForm(instance=cur_customer)
    return render(request, 'Director/updateCustomer.html',
                  context={"cur_customer": cur_customer, "customerform": customerform})


# Изменение информации о выбраном договоре
def updateContract(request, contract):
    cur_contract = Contract.objects.get(id=contract)
    if request.method == "POST":
        contractform = ContractForm(request.POST, instance=cur_contract)
        if contractform.is_valid():
            item = contractform.save(commit=False)
            item.save()
    else:
        contractform = ContractForm(instance=cur_contract)
    return render(request, 'Director/updateContract.html',
                  context={"cur_contract": cur_contract, "contractform": contractform})


# Изменение информации о выбраном проекте
def updateProject(request, project):
    cur_project = Project.objects.get(id=project)
    if request.method == "POST":
        projectform = ProjectForm(request.POST, instance=cur_project)
        if projectform.is_valid():
            item = projectform.save(commit=False)
            item.save()
    else:
        projectform = ProjectForm(instance=cur_project)
    return render(request, 'Director/updateProject.html',
                  context={"cur_project": cur_project, "projectform": projectform})


# Изменение информации о выбраной задаче
def updateProblem(request, problem):
    cur_problem = Problem.objects.get(id=problem)
    if request.method == "POST":
        problemform = ProblemForm(request.POST, instance=cur_problem)
        if problemform.is_valid():
            item = problemform.save(commit=False)
            item.save()
    else:
        problemform = ProblemForm(instance=cur_problem)
    return render(request, 'Director/updateProblem.html',
                  context={"cur_problem": cur_problem, "problemform": problemform})
