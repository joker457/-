# teachers/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TeacherViewSet, ScheduleViewSet, AppointmentViewSet
from .views import get_root_token

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/get-root-token/', get_root_token),
]

