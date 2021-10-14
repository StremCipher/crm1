"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # arguments of path first is destination loaction
    # path('', views.index, name='home'),
    # url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'),
    #     name='home'),
    url(r'^admin/', admin.site.urls),
    # the regex ^$ matches empty
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'),
        name='home'),
    # arguments of path first is destination loaction this must prest in views.py file
    path('amit', views.amit, name='this is amit page'),
    path('about', views.about, name='about'),
    path('text_analyzer', views.input_area, name='input'),
    path('analysed_text', views.output_area, name='output')

]
