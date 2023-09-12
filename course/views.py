from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson, Payments
from course.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (OrderingFilter, SearchFilter,)
    ordering_fields = ['date_pay']
    search_fields  = ["type_metod", "payment_method"]

