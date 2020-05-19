from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View

from vacancies.matching_words import matching_words_numerals
from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy


class MainView(View):
    """Класс, отвечающий за наполнение главной странички
    доступ по /"""

    def get(self, request) -> render:
        specialties = Specialty.objects.values('code', 'title') \
            .annotate(count=Count('vacancies')). \
            filter(count__gt=0).order_by('title')
        companies = Company.objects.values('id', 'name'). \
            annotate(count=Count('vacancies')). \
            filter(count__gt=0).order_by('name')
        return render(request, 'index.html', context={
            'specialties': specialties,
            'companies': companies,
        })


class VacanciesView(View):
    """Класс, отвечающий за наполнение раздела всех вакансий
    доступ по vacancies/
    использование vacancies.html  - общего с классом VacanciesCategoryView"""

    def get(self, request) -> render:
        html_header = "Все вакансии"
        vacancies_on_page = Vacancy.objects.values('title',
                                                   'specialty__code',
                                                   'salary_min',
                                                   'salary_max',
                                                   'published_at',
                                                   'description',
                                                   'id', )
        quantity_vacancies = vacancies_on_page.count()
        word_vacancy = matching_words_numerals('вакансия', quantity_vacancies)
        return render(request, 'vacancies.html', context={
            'html_header': html_header,
            'vacancies': vacancies_on_page,
            'quantity_vacancies': f"{quantity_vacancies} {word_vacancy}"
        })


class VacanciesCategoryView(View):
    """Класс, отвечающий за наполнение раздела вакансий по категориям работ
    доступ по vacancies/cat/<str:cat_id>/
    использование vacancies.html  - общего с классом VacanciesView"""

    def get(self, request, cat_id) -> render:
        try:
            Specialty.objects.get(code=cat_id)
        except Specialty.DoesNotExist:
            return render(request, '404.html')
        html_header = Specialty.objects.get(code=cat_id).title
        vacancies_on_page = Vacancy.objects. \
            filter(specialty__code=cat_id). \
            values('title', 'specialty__code', 'salary_min',
                   'salary_max', 'published_at', 'description', 'id', )
        quantity_vacancies = vacancies_on_page.count()
        word_vacancy = matching_words_numerals('вакансия', quantity_vacancies)
        return render(request, 'vacancies.html', context={
            'html_header': html_header,
            'vacancies': vacancies_on_page,
            'quantity_vacancies': f"{quantity_vacancies} {word_vacancy}"
        })


class CompanyAllView(View):
    """Класс, отвечающий за наполнение раздела компании
    доступ по companies/"""

    def get(self, request) -> render:
        companies = Company.objects.values('id', 'name'). \
            annotate(count=Count('vacancies')). \
            filter(count__gt=0).order_by('name')
        return render(request, 'company_all.html', context={
            'companies': companies,
        })


class CompanyView(View):
    """Класс, отвечающий за наполнение раздела вакансий конкретной компании
    доступ по companies/<int:company_id>/"""

    def get(self, request, company_id) -> render:
        try:
            Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return render(request, '404.html')
        html_header = Company.objects.get(id=company_id)
        vacancies_on_page = Vacancy.objects. \
            filter(company__id=company_id). \
            values('title', 'specialty__code', 'salary_min',
                   'salary_max', 'published_at', 'description', 'id', )
        quantity_vacancies = vacancies_on_page.count()
        word_vacancy = matching_words_numerals('вакансия', quantity_vacancies)
        return render(request, 'company.html', context={
            'html_header': html_header,
            'vacancies': vacancies_on_page,
            'quantity_vacancies': f"{quantity_vacancies} {word_vacancy}"
        })


class VacancyView(View):
    """Класс, отвечающий за наполнение информацией по конкретной ваканчии
    доступ по vacancies/<int:vacancy_id>/"""

    def get(self, request, vacancy_id):
        try:
            Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            return render(request, '404.html')
        vacancy_on_page = Vacancy.objects. \
            filter(id=vacancy_id). \
            values('title', 'specialty__code', 'salary_min',
                   'salary_max', 'published_at', 'description', )
        return render(request, 'vacancy.html', context={
            'vacancy': vacancy_on_page.first(),
        })
