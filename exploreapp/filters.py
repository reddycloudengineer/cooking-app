import django_filters

from exploreapp.models import Place


class PlaceFilter(django_filters.FilterSet):
    name = django_filters.Filter(name='name', lookup_expr='icontains')
    category = django_filters.Filter(name='category__name', lookup_expr='icontains')
    city = django_filters.Filter(name='city', lookup_expr='iexact')

    class Meta:
        model = Place
        fields = ('name', 'category', 'city',)
