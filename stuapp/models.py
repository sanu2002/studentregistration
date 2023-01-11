from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

# def create_superuser():
#     User = get_user_model()
#     admin = User.objects.create_superuser(
#         username='admin',
#         email='admin@example.com',
#         password='secret'
#     )
#     admin.is_staff = True
#     admin.is_superuser = True
#     admin.save()



class City(models.Model):
    City_Name = models.CharField(max_length=500)


    def __str__(self):
        return f'{self.City_Name}'


class Course(models.Model):
    Course_Name = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.Course_Name}'


class Student(models.Model):
    Stud_Name=models.CharField(max_length=500)
    Stud_AGE=models.IntegerField()
    Stud_Phn=models.IntegerField()
    Stud_City=models.ForeignKey(City,on_delete=models.CASCADE)
    Stud_Course=models.ForeignKey(Course,on_delete=models.CASCADE)
