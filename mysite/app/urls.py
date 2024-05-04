from django.urls import path
from .views import test, glavnaya, disciplina, istoria, korzina, info, tusk

urlpatterns = [
    path('test.html', test, name='test'),
    path('', glavnaya, name='glavnaya'),
    path('glavnaya.html', glavnaya, name='glavnaya'),
    path('disciplina.html', disciplina, name='disciplina'),
    path('istoria.html', istoria, name='istoria'),
    path('korzina.html', korzina, name='korzina'),
    path('info.html', info, name='info'),
    path('tusk.html', tusk, name='tusk'),
]
