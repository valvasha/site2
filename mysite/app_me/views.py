from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Content

# Create your views here.


def me(request: HttpRequest, url) -> HttpResponse:
    print(f'GET with url = {url}')
    navigation = Content.objects.values_list(
        'url', 'nav_title'
    ).order_by('nav_position')
    context = {
        'content_object': None,
        'navigation': navigation,
    }
    model_object = Content.objects.filter(url=url)
    if not model_object:
        print('NOT URL')
        return render(request=request, template_name='app_me/me.html', context=context)
    context['content_object'] = model_object[0]
    return render(request=request, template_name='app_me/me.html', context=context)
