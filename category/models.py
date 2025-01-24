from django.db import models
from django.utils.translation import gettext_lazy as _



class category(models.Model):
    category = models.CharField(max_length=100, verbose_name=_("Kategoryani kiriting"))
    
    def __str__(self):
        return self.category
    
    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'category'
        
        
        
class Users(models.Model):
    user_id = models.CharField(unique=True, max_length=35, verbose_name=_("Foydalanuvchi idsi"))
    firstname = models.CharField(max_length=100, verbose_name=_("foydalanuvchi ismi"))
    
    
    def __str__(self):
        return self.firstname
    
    class Meta:
        db_table = 'users'
        verbose_name = 'foydalanuvchi'
        verbose_name_plural = 'foydalanuvchi'