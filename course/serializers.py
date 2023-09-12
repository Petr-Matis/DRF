from rest_framework import serializers

from course.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        return instance.lesson.all().count()

    class Meta:
        model = Course
        fields = ['name', 'image', 'description', 'lesson', 'lesson_count']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
