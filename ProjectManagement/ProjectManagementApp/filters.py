import django_filters
from .models import Enrichment,Disasters,Projects


class DisasterFilter(django_filters.FilterSet):
    state=django_filters.CharFilter()
    disaster_number=django_filters.CharFilter()
    declaration_date=django_filters.DateFilter()
    class Meta:
        model = Disasters
        fields = ['state','disaster_number','declaration_date']
    
class ProjectFilter(django_filters.FilterSet):
    state=django_filters.CharFilter(field_name='assigned_disaster_number__state',label='State')
    disaster_number=django_filters.CharFilter(field_name='assigned_disaster_number__disaster_number',label='Disaster Number')
    project_identifier=django_filters.CharFilter()
    project_title=django_filters.CharFilter()
    type=django_filters.CharFilter()
    county=django_filters.CharFilter()
    subgrantee=django_filters.CharFilter()
    class Meta:
        model = Projects
        fields = ['state','disaster_number','project_identifier','project_title','type','county','subgrantee']