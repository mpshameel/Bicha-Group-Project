from django.urls import path
from anshaj import views


urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contact',views.contact, name='contact'),
    path('category/',views.category, name='category'),
    path('postjob/',views.postjob, name='postjob'),
    path('search/',views.search, name='search'),
    path('apply/',views.apply, name='apply'),
    path('applying/',views.applying, name='applying'),
    path('impmessage/',views.impmessage, name='impmessage'),
 
]