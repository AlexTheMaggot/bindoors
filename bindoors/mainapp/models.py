from django.db import models

# Create your models here.

class Project(models.Model):
    object = models.CharField(verbose_name='Объект', max_length=200)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    date = models.CharField(verbose_name='Дата монтажа', max_length=200)
    task = models.CharField(verbose_name='Задача', max_length=200)
    jobs = models.CharField(verbose_name='Выполненые работы', max_length=200)
    price = models.CharField(verbose_name='Общая стоимость проекта', max_length=200)
    thumb1 = models.ImageField(verbose_name='Миниатюра 1 (334x500)', upload_to='static/img/project_img/')
    thumb2 = models.ImageField(verbose_name='Миниатюра 2 (334x500)', upload_to='static/img/project_img/')
    thumb3 = models.ImageField(verbose_name='Миниатюра 3 (334x500)', upload_to='static/img/project_img/')
    thumb4 = models.ImageField(verbose_name='Миниатюра 4 (1000x500)', upload_to='static/img/project_img/')
    thumb5 = models.ImageField(verbose_name='Миниатюра 5 (500x1000)', upload_to='static/img/project_img/')
    thumb6 = models.ImageField(verbose_name='Миниатюра 6 (500x1000)', upload_to='static/img/project_img/')
    img1 = models.ImageField(verbose_name='Изображение 1', upload_to='static/img/project_img')
    img2 = models.ImageField(verbose_name='Изображение 2', upload_to='static/img/project_img')
    img3 = models.ImageField(verbose_name='Изображение 3', upload_to='static/img/project_img')
    img4 = models.ImageField(verbose_name='Изображение 4', upload_to='static/img/project_img')
    img5 = models.ImageField(verbose_name='Изображение 5', upload_to='static/img/project_img')
    img6 = models.ImageField(verbose_name='Изображение 6', upload_to='static/img/project_img')

    def __str__(self):
        return self.object

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'