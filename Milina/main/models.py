from django.db import models

class Contacts(models.Model):
    name = models.TextField('name', max_length=50)
    email = models.EmailField('Email', max_length=50)
    phone_number = models.CharField('Phone_number', max_length=12)
    message = models.TextField('Message', max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/index/{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'