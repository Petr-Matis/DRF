from django.urls import path
from rest_framework import routers

from course.apps import CourseConfig
from course.serializers import LessonSerializer
from course.views import LessonListAPIView, LessonDetailAPIView, LessonCreateAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView, CourseViewSet, PaymentsViewSet

app_name = CourseConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view()),
                  path('lesson/<int:pk>/', LessonDetailAPIView.as_view()),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view()),
                  path('lesson/create/', LessonCreateAPIView.as_view()),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view()),
              ] + router.urls
