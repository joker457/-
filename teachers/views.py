from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Schedule, Appointment, CustomUser
from .serializers import TeacherSerializer, ScheduleSerializer, AppointmentSerializer, CustomUserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

@api_view(['GET'])
def get_root_token(request):
    User = get_user_model()
    try:
        user = User.objects.get(username='root')
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=404)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
