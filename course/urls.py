from django.urls import path
from rest_framework import routers

from course.apps import CourseConfig
from course.serializers import LessonSerializer
from course.views import LessonListAPIView, LessonDetailAPIView, LessonCreateAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView, CourseViewSet

app_name = CourseConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [

                  path('lesson/', LessonListAPIView.as_view()),
                  # path('lesson/', ListAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonDetailAPIView.as_view()),
                  # path('lesson/<int:pk>/', RetrieveAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson-detail'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view()),
                  # path('lesson/<int:pk>/update/', UpdateAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson-update'),
                  path('lesson/create/', LessonCreateAPIView.as_view()),
                  # path('lesson/create/', CreateAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson-create'),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view()),
                  # path('lesson/<int:pk>/delete/', DestroyAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson-delete'),

              ] + router.urls
