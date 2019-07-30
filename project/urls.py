from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('', include('apps.pages.urls')), # new  
]