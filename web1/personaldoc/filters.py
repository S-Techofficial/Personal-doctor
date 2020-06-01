import django_filters
from django_filters import DateFilter
from .models import *

class ProblemFilter(django_filters.FilterSet):
    start_date= DateFilter(field_name="date_created",lookup_expr="gte")
    end_date= DateFilter(field_name="date_created",lookup_expr="lte")
    class Meta:
        model = Solutions
        fields = '__all__'
        exclude = ['Patients','date_created','Add_solution']