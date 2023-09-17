from rest_framework import serializers

from course.models import Course, Lesson, Payments, Subscription
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='url')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)
    validators = [UrlValidator(field='url')]
    subscription = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def get_lesson_count(self, instance):
        return instance.lesson.all().count()

    def get_subscription(self, instance):
        user = self.request.user
        sub_all = instance.subscription.all()
        for sub in sub_all:
            if sub.subscriber == user:
                return True
        # if not instance.subscription.all():
        #     return False
        return False

    class Meta:
        model = Course
        fields = ['pk', 'name', 'image', 'description', 'owner', 'subscription', 'lesson', 'lesson_count']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
