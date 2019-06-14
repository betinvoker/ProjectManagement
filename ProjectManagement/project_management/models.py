from django.db import models


# Таблица - Тип заказчика
class Type_customer(models.Model):
    type_customer = models.CharField(max_length=100, verbose_name='Тип заказчика')

    def __str__(self):
        return self.type_customer or str(self.id)

    class Meta:
        verbose_name = 'Тип заказчика'
        verbose_name_plural = 'Типы заказчика'


# Таблица - Тип проекта
class Type_project(models.Model):
    name_type = models.CharField(max_length=150, verbose_name='Название типа')

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name = 'Тип проекта'
        verbose_name_plural = 'Типы проектов'


# Таблица - Вид задачи
class Task(models.Model):
    name_task = models.CharField(max_length=200, verbose_name='Название вида задачи')

    def __str__(self):
        return self.name_task

    class Meta:
        verbose_name = 'Вид задачи'
        verbose_name_plural = 'Виды задач'


# Таблица - Должность
class Position(models.Model):
    position = models.CharField(max_length=12, verbose_name='Название должности')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


# Таблица - Заказчик
class Customer(models.Model):
    id_type_customer = models.ForeignKey(Type_customer, on_delete=models.CASCADE, verbose_name='Тип заказчика')
    customer = models.CharField(max_length=200, verbose_name='Заказчик')
    phone = models.IntegerField(verbose_name='Номер телефона')
    mail = models.CharField(max_length=50, verbose_name='Email')

    def __str__(self):
        return '%s' % (self.customer,)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


# Таблица - Договоры
class Contract(models.Model):
    num_contract = models.CharField(max_length=10, verbose_name='Номер контракта')
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    comment = models.TextField(max_length=500, verbose_name='Комментарий', blank=True)
    status = models.IntegerField(choices=[(0, 'Не выполнен'), (1, 'Выполняется'), (2, 'Выполнен')],
                                 verbose_name='Статус')
    link_file = models.CharField(max_length=500, verbose_name='Ссылка на файл', blank=True)
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return '%s %s' % (self.num_contract, self.id_customer)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


# Таблица - Сотрудники
class Worker(models.Model):
    link_photo = models.CharField(max_length=500, verbose_name='Ссылка на фото', blank=True)
    surname = models.CharField(max_length=80, verbose_name='Фамилия', blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя', blank=True)
    patronymic = models.CharField(max_length=55, verbose_name='Отчество', blank=True)
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    experience = models.IntegerField(verbose_name='Опыт работы', blank=True)
    gender = models.CharField(max_length=3, verbose_name='Пол', blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения', blank=True)
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True)
    mail = models.CharField(max_length=50, verbose_name='Email', blank=True)

    def __str__(self):
        return '%s %s %s' % (self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


# Таблица - Проекты
class Project(models.Model):
    id_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Номер контракта')
    id_type = models.ForeignKey(Type_project, on_delete=models.CASCADE, verbose_name='Тип проекта')
    project_name = models.CharField(max_length=300, verbose_name='Название проекта')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата конца')

    def __str__(self):
        return '%s %s %s' % (self.id_contract, self.id_type, self.project_name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


# Таблица - Задачи
class Problem(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Вид задачи')
    problem = models.CharField(max_length=300, verbose_name='Название задачи')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    date_start_plan = models.DateField(verbose_name='Дата конца по плану')
    date_end_plan = models.DateField(verbose_name='Дата начала по плану')
    date_start_actual = models.DateField(blank=True, null=True, verbose_name='Дата фактического начала')
    date_end_actual = models.DateField(blank=True, null=True, verbose_name='Дата фактического конца')
    status = models.IntegerField(choices=[(0, 'Не выполнена'), (1, 'Выполняется'), (2, 'Выполнена')],
                                 verbose_name='Статус')

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (
            self.id_project, self.id_task, self.problem, self.description, self.date_start_plan, self.date_end_plan,
            self.date_start_actual, self.date_end_actual, self.status)

    class Meta:
        verbose_name = 'Задач'
        verbose_name_plural = 'Задачи'


# Таблица - Участие
class Project_participant(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Работник')
    status = models.IntegerField(choices=[(0, 'Не выполнена'), (1, 'Выполняется'), (2, 'Выполнена')],
                                 verbose_name='Статус')

    def __str__(self):
        return '%s %s %s' % (self.id_project, self.id_worker, self.status)

    class Meta:
        verbose_name = 'Участие'
        verbose_name_plural = 'Участие'


# Таблица - Исполнители
class Doer(models.Model):
    id_problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name='Задача')
    id_participant = models.ForeignKey(Project_participant, on_delete=models.CASCADE, verbose_name='Участие в проекте')

    def __str__(self):
        return '%s %s' % (self.id_problem, self.id_participant)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
