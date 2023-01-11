from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    userbook = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Пользователь")

    name = models.CharField(max_length=512,verbose_name="Название книги")
    desk = models.TextField(verbose_name="Дескриптор")

    author = models.CharField(max_length=512,verbose_name="Автор книги")
    
    # time_create = models.DateTimeField(verbose_name="Дата создания")
    photo1 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото 1")
    photo2= models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото 2")
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото 3")
    book = models.FileField(upload_to="books/%Y/%m/%d/",verbose_name="Книга")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Когда добавлен")
    likenolike = models.IntegerField(default=0,verbose_name="Сколькам пользователям понравился")#1-понравился 0-не сделал оценку -1-не понравился

    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['id']
