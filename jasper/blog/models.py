from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Universty(models.Model):
    name = models.CharField(max_length =50)
    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=100)
    master = models.CharField(max_length=20,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=200,help_text="در مورد جزوه و یا کتاب خود بنویسید .",blank=True)
    STATUS = (
        ('j', 'جزوه'),
        ('k', 'کتاب'),
    )
    status = models.CharField(max_length=1, choices=STATUS,
                              blank=True
                              , default='j'
                              , help_text='نوع')
    class Meta:
        ordering =["name","price"]

    def __str__(self):
        return '{0}, {1}'.format(self.name,self.price)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True)

    #many to mnay
    university = models.ManyToManyField(Universty, help_text='')


class User(models.Model):
    username=models.CharField(max_length=100 )
    password=models.CharField(max_length=50 )
    email=models.CharField(max_length=50 )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    city= models.CharField(max_length=20,null=True)
    phone_number=models.CharField(null=True,blank=True,max_length=11)
    description=models.CharField(max_length=200,blank=True)

    # many to many
    #book = models.ManyToManyField(Book, help_text='select what you want book to sell ?')

    # one to many
    # field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True)
    # section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering =["last_name","first_name"]

    def __str__(self):
        return '{0}, {1}'.format(self.last_name,self.first_name)






class Field (models.Model):
    name = models.CharField(max_length=100)
    SECTION = (
        ('b', 'کارشناسی'),
        ('m', 'کارشناسی ارشد'),
        ('d', 'دکتری'),
    )
    status = models.CharField(max_length=1, choices=SECTION,
                              blank=True
                              , default='b'
                              , help_text='مقطع مروبطه ی کتاب یا جزوه را انتخاب کنید ')

    def __str__(self):
        return self.name




