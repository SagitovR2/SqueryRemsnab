from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('type.html', views.type, name='type'),
    path('abduction.html', views.abduction, name='abduction'),
    path('applience.html', views.applience, name='applience'),
    path('bringing.html', views.bringing, name='bringing'),
    path('people.html', views.people, name='people'),
    path('repair.html', views.repair, name='repair'),
    path('post_edit.html', views.post_new, name='editor'),
    path('tablet.html', views.applience_new, name='new'),
    path('table.html', views.table, name='new'),
    path('proba.html', views.table, name='ggkgkgfgkfkg'),
]
