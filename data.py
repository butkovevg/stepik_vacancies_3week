from datetime import datetime

from vacancies.models import Company, Specialty, Vacancy

""" Вакансии """
jobs = [

    {"title": "Разработчик на Python",
     "cat": "backend",
     "company": "staffingsmarter",
     "salary_from": "100000",
     "salary_to": "150000",
     "posted": "2020-02-11",
     "desc": "Описания нет"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-04-11", "desc": "Описания нет"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Описания нет"},
    {"title": "Мидл программист на Python", "cat": "design", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-05-11", "desc": "Описания нет"},
    {"title": "frontend-разработчик", "cat": "frontend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-12", "desc": "Описания нет"}

]
""" Компании """
companies = [

    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreat h"},
    {"title": "hirey "},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}

]
""" Категории """
specialties = [

    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}

]
Vacancy.objects.all().delete()
Specialty.objects.all().delete()
Company.objects.all().delete()
print('0step -- OK')
for specialty in specialties:
    Specialty.objects.create(
        title=specialty['title'],
        code=specialty['code'],
    )
print('1step -- OK')

for company in companies:
    Company.objects.create(name=company['title'],
                           location='NO_LOCATION',
                           description='NO_description',
                           employee_count=0,
                           )

print('2step -- OK')
for job in jobs:
    specialty = Specialty.objects.get(code=job['cat'])
    company = Company.objects.get(name=job['company'])
    Vacancy.objects.create(
        title=job['title'],
        description=job['desc'],
        salary_min=job['salary_from'],
        salary_max=job['salary_to'],
        published_at=datetime.strptime(job['posted'], '%Y-%m-%d'),
        specialty=specialty,
        company=company)
print('3step -- OK')
print('success')
