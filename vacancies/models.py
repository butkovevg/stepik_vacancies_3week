from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name='название')
    location = models.CharField(max_length=64)
    # logo = models.CharField(max_length=64) #Планируем использовать потом
    description = models.CharField(max_length=640)
    employee_count = models.IntegerField()

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=24)
    title = models.CharField(max_length=24)

    # picture = models.CharField(max_length=64) #Планируем использовать потом
    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = 'специализации'
        ordering = ['title']

    def __str__(self) -> str:
        return f'{self.title} [{self.code}]'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name="vacancies")
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="vacancies")
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=640)
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
