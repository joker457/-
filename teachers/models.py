# teachers/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    research = models.CharField(max_length=200)
    contact = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.time_slot}"


class Appointment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=100)
    status = models.CharField(max_length=50,
                              choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"{self.student_name} - {self.appointment_date} - {self.status}"
