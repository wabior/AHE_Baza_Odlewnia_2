from django.db import models
from django.db.models import Sum
from datetime import datetime

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return self.Project_name
    Project_name    = models.CharField(max_length=60)
    SOP_Date        = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name        = "Projekt"
        verbose_name_plural = "Projekty"

class Type(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=60)
    Type_Id = models.CharField(max_length=60)
    Project_Project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        verbose_name        = "Typ głowicy"
        verbose_name_plural = "Typy głowic"

class Forms(models.Model):
    def __str__(self):
        return self.Code_name
    Code_name = models.CharField(max_length=60)
    Current_Shoots = models.IntegerField()
    Total_Shoots = models.IntegerField()
    Max_Shoots = models.IntegerField()
    Status = models.IntegerField()
    Type_Type = models.ForeignKey(Type,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        verbose_name        = "Forma"
        verbose_name_plural = "Formy"

class Machine(models.Model):
    def __str__(self):
        return self.Name
    Code_Name = models.CharField(max_length=60)
    Name = models.CharField(max_length=60)
    Status = models.IntegerField(blank=True)
    Form_Forms = models.ForeignKey(Forms,on_delete=models.CASCADE,blank=True,null=True)
    Current_Shoots = models.IntegerField(default=0)
    Total_Shoots = models.IntegerField(default=0)
    class Meta:
        verbose_name        = "Maszyna"
        verbose_name_plural = "Maszyny"

class Production(models.Model):
    def __str__(self):
        return ' Maszyna %s Produkcja %i' % (self.Machine, self.Production_Value)
    shift_date = models.DateField(auto_now=False,default=datetime.now)
    Machine = models.ForeignKey(Machine, on_delete=models.CASCADE, blank=False, null=True)
    Production_Value = models.IntegerField(default=0)
    class Meta:
        verbose_name        = "Produkcja"
        verbose_name_plural = "Produkcja"

class User(models.Model):
    def __str__(self):
        return self.Personal_Nr
    Personal_Nr = (models.CharField)(max_length=7)
    USER = 'USR'
    SUPERVISOR = 'SVR'
    MNX = 'MNX'
    ADMIN = 'ADM'
    USER_LEVEL = (
        (USER, 'USER'),
        (MNX, 'MNX'),
        (SUPERVISOR, 'SUPERVISOR'),
        (ADMIN, 'ADMIN'),
    )
    User_Level = models.CharField(
        max_length=3,
        choices=USER_LEVEL,
        default=USER,
    )
    class Meta:
        verbose_name        = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

