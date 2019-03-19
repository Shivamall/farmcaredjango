"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('article', TemplateView.as_view(template_name='index.html')),
    path('vuechart', TemplateView.as_view(template_name='vuechart.html')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('header-nav', TemplateView.as_view(template_name='header-nav.html')),
    path('footer', TemplateView.as_view(template_name='footer.html')),
    path('plants', TemplateView.as_view(template_name='plants.html')),
    path('statics', TemplateView.as_view(template_name='statics.html')),
    path('articles', TemplateView.as_view(template_name='articles.html')),
    path('weather', TemplateView.as_view(template_name='weather.html')),
    path('contact', TemplateView.as_view(template_name='contact.html')),
    path('aboutus', TemplateView.as_view(template_name='aboutus.html')),
    path('profile', TemplateView.as_view(template_name='profile.html')),

]
