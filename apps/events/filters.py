import django_filters as df
from .models import Event


class EventFilter(df.FilterSet):
    category = df.NumberFilter(field_name='category__id')
    date_start = df.NumberFilter(field_name='date_start__id')

    class Meta:
        model = Event
        fields = ['category', 'date_start']