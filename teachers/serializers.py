from rest_framework import serializers
from .models import CustomUser, Teacher, Schedule, Appointment

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_teacher', 'is_student']

class TeacherSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'title', 'research', 'contact', 'bio', 'user_id', 'user']
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
