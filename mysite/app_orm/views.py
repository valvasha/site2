from typing import List

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import Avg, Min, Max, Count

from .forms import AbcModelForm
from .models import AbcModel

# Create your views here.


def abc_model_form(request: HttpRequest) -> HttpResponse:
    # Формируем форму
    form = AbcModelForm()
    context = {
        'form': form,
        'fields_name': None,
        'attrs': None,
    }
    if request.method == 'POST':
        # Полученные данных из формы;
        form = AbcModelForm(request.POST)
        if form.is_valid():
            # Сохранение данных в таблице базы;
            form.save()
            # Получение данных из таблицы базы, необходимые вычисления и представление данных и результатов решения в таблицеподобном виде;
            model_object: AbcModel = form.instance
            model_object.result = model_object.get_result()
            # Сохранение результата
            model_object.save()
            context['fields_name'] = [
                field.verbose_name for field in AbcModel._meta.get_fields()
            ]
            values = list(model_object.__dict__.values())
            values.pop(0)
            context['values'] = values
    return render(request=request, template_name='app_orm/index.html', context=context)


def show_table(request: HttpRequest) -> HttpResponse:
    context: dict = {
        'fields_verbose_name': None,
        'objects_values_list': None,
        'statistic': None,
    }
    # Формируем список имён полей
    fields = AbcModel._meta.get_fields()
    fields_name = [field.name for field in fields]
    fields_verbose_name = [field.verbose_name for field in fields]
    context['fields_verbose_name'] = fields_verbose_name
    # Получаем список объектов из базы данных
    objects_values_list = AbcModel.objects.values_list(*fields_name)
    context['objects_values_list'] = objects_values_list
    if objects_values_list:
        # Формируем статистику по полю "m"
        statistic_values = list(objects_values_list.aggregate(
            Count('m'), Avg('m'), Min('m'), Max('m')
        ).values())
        statistic = {
            'Общее Количество записей': statistic_values[0],
            'Среднее значение объёма': round(statistic_values[1], 2),
            'Минимальное значение объёма': statistic_values[2],
            'Максимальное значение объёма': statistic_values[3],
        }
        context['statistic'] = statistic
    return render(request=request, template_name='app_orm/show-table.html', context=context)


def show_table_last10(request: HttpRequest) -> HttpResponse:
    context: dict = {}
    # Формируем список имён полей
    fields: List = AbcModel._meta.get_fields()
    fields_name = [field.name for field in fields]
    fields_verbose_name = [field.verbose_name for field in fields]
    context['fields_verbose_name'] = fields_verbose_name
    # Получаем список объектов из базы данных
    objects_values_list = AbcModel.objects.values_list(*fields_name)
    if objects_values_list:
        # Фильтруем объекты, выводим последние n записей и сортируем по убыванию id
        last_id = AbcModel.objects.latest('id').pk
        n = 5
        id_gt = last_id - n
        # Фильтруем
        objects_values_list = objects_values_list.filter(id__gt=id_gt)
        # Сортируем
        objects_values_list = objects_values_list.order_by('-id')
    context['objects_values_list'] = objects_values_list
    return render(request=request, template_name='app_orm/show-table-las10.html', context=context)
