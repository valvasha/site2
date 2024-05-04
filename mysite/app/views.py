from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import Form

import math


# Create your views here.
# mysite/app/templates/test.html
def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'test.html')


# mysite/app/templates/glavnaya.html
def glavnaya(request: HttpRequest) -> HttpResponse:
    return render(request, 'glavnaya.html')


# mysite/app/templates/disciplina.html
def disciplina(request: HttpRequest) -> HttpResponse:
    return render(request, 'disciplina.html')


# mysite/app/templates/istoria.html
def istoria(request: HttpRequest) -> HttpResponse:
    return render(request, 'istoria.html')


# mysite/app/templates/korzina.html
def korzina(request: HttpRequest) -> HttpResponse:
    return render(request, 'korzina.html')


# mysite/app/templates/info.html
def info(request: HttpRequest) -> HttpResponse:
    context = {
        'me': {
            'name': 'Ширяева Валерия Александровна',
            'photo': 'me.jpg',
            'email': 'vashiryaeva@edu.hse.ru',
            'phone': '+7(950)442-45-69',
        },
        'programm': {
            'name_programm': 'Управление бизнесом',
            'description': 'Целью образовательной программы «Управление бизнесом» является подготовка'
            ' современных специалистов с глубокими междисциплинарными знаниями и практическими навыками'
            ' в области управления бизнесом. Выпускники программы сбалансированно владеют аналитическими,'
            ' IT и организационными инструментами управления, способны принимать проработанные решения'
            ' в ключевых сферах деятельности крупных и средних компаний,'
            ' а также собственных предпринимательских проектах.',
        },
        'supervisor': {
            'name': 'Артемьев Дмитрий Геннадьевич',
            'photo': 'supervisor.jpg',
            'email': 'dartemev@hse.ru',
        },
        'manager': {
            'name': 'Тутынина Ольга Владимировна',
            'photo': 'manager.jpg',
            'email': 'oshibanova@hse.ru',
        },
        'student_1': {
            'name': 'Валеев Эмиль Фидаилович',
            'photo': 'student_1.jpg',
            'email': 'efvaleev@edu.hse.ru',
            'phone': '+7(996)123-62-37',
        },
        'student_2': {
            'name': 'Субботина Полина Андреевна',
            'photo': 'student_2.jpg',
            'email': 'pasubbotina@edu.hse.ru',
            'phone': '+7(919)463-18-88',
        },
    }
    return render(request, 'info.html', context=context)

def tusk_math(m: float, v_cube: float, v_celindr: float):
    answer_dict = {}
    if m <= v_cube and m <= v_celindr:
        answer_dict['answer_all'] = 'Жидкостью обёмом {} нельзя заполнить ни одну из ёмкостей.'.format(m)
    if m >= (v_cube + v_celindr):
        answer_dict['answer_all'] = 'Жидкостью обёмом {} можно заполнить обе ёмкости.'.format(m)
    if m >= v_cube:
        answer_dict['answer_сube'] = 'Жидкостью объёмом {} можно заполнить кубическую ёмкость.'.format(m)
    if m >= v_celindr:
       answer_dict['answer_celindr'] = 'Жидкостью объёмом {} Можно заполнить целиндрическую ёмкость.'.format(m)
    return answer_dict

# mysite/app/templates/tusk.html
def tusk(request: HttpRequest) -> HttpResponse:
    answer = None
    if request.method == "POST":
        a = float(request.POST.get('a'))
        h = float(request.POST.get('h'))
        r = float(request.POST.get('r'))
        m = float(request.POST.get('m'))
        print(a, h, r, m)
        # Объём кубической ёмкости
        v_cube = a ** 2
        # Объём целиндрической плоскостии
        v_celindr = round(math.pi * (r ** 2) * h, 2)
        print(v_cube, v_celindr)
        answer = tusk_math(m, v_cube, v_celindr)
        
    context = {
        'answer': answer,
        'form' : Form(),
    }
    return render(request, 'tusk.html', context=context)