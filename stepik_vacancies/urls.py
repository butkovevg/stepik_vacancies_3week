"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from vacancies.views import CompanyAllView
from vacancies.views import CompanyView
from vacancies.views import MainView
from vacancies.views import VacanciesCategoryView
from vacancies.views import VacanciesView
from vacancies.views import VacancyView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('companies/', CompanyAllView.as_view(), name='company_all'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:cat_id>/',
         VacanciesCategoryView.as_view(), name='vacancies_category'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
]
