from django.urls import path
from .views import me
urlpatterns = [
    path('<str:url>/', me, name='me')
]
