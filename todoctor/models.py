from django.db import models

# Create your models here.
class Physician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birthdate = models.DateFiels()
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    gender = models.ForeignKey("Gender", on_delete=models.CASCADE)
    age = models.ForeignKey("AgeCategory", on_delete=models.CASCADE)

class Gender(models.Model):
    MAN = 'M'
    WOMAN = 'W'
    GENDER_CHOICES = (
        (MAN, 'man'),
        (WOMAN, 'woman'),
    )
    gender_choices = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

class AgeCategory(models.Model):
    NEWBORNS = 'nb'
    CHILDREN = 'ch'
    ADULT = 'ad'
    AGED = 'ag'
    AGE_CHOICES = (
        (NEWBORNS, 'newborns'),
        (CHILDREN, 'children'),
        (ADULT, 'adult'),
        (AGED, 'aged'),
    )
    age_choces = models.CharField(
        max_length=2,
        choices=AGE_CHOICES,
    )
