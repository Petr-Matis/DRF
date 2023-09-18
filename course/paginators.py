
from rest_framework.pagination import PageNumberPagination


class ConditionalCoursePaginator(PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        if queryset.count() <= self.page_size:
            return None
        return super().paginate_queryset(queryset, request, view)


class CoursePaginator(PageNumberPagination):
    page_size = 2
