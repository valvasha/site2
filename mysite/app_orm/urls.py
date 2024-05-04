from django.urls import path
from .views import abc_model_form, show_table, show_table_last10

urlpatterns = [
    path('', abc_model_form, name='abc_form'),
    path('table/', show_table, name='table'),
    path('table/last5/', show_table_last10, name='table-last5'),
]
