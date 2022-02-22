import django_filters
from .models import Enrichment,Disasters,Projects

JURISDICTION_CHOICES=(
    ('American Samoa','American Samoa'),
    ('Arizona','Arizona'),
    ('California','California'),
    ('Federated States of Micronesia','Federated States of Micronesia'),
    ('Guam','Guam'),
    ('Hawaii','Hawaii'),
    ('Marshall Islands','Marshall Islands'),
    ('Nevada','Nevada'),
    ('Northern Mariana Islands','Northern Mariana Islands'),
    ('Palau','Palau'),
)

CLOSEOUT_STATUS_CHOICES=(
    ('Open','Open'),
    ('Closed','Closed'),
    ('',''),
)

class DisasterFilter(django_filters.FilterSet):
    state=django_filters.ChoiceFilter(choices=JURISDICTION_CHOICES,null_value=None)
    disaster_number=django_filters.CharFilter(label='Disaster Number')
    declaration_date=django_filters.DateFilter(label='Disaster Date')
    disaster_closeout_status=django_filters.ChoiceFilter(label='Disaster Status',choices=CLOSEOUT_STATUS_CHOICES,null_value=None)
    hmgp_closeout_status=django_filters.ChoiceFilter(label='HMGP Status',choices=CLOSEOUT_STATUS_CHOICES,null_value=None)

    class Meta:
        model = Disasters
        fields = ['state','disaster_number','declaration_date','disaster_closeout_status','hmgp_closeout_status']
    
class ProjectFilter(django_filters.FilterSet):
    state=django_filters.ChoiceFilter(field_name='assigned_disaster_number__state',label='State',choices=JURISDICTION_CHOICES,null_value=None)
    disaster_number=django_filters.CharFilter(field_name='assigned_disaster_number__disaster_number',label='Disaster Number')
    project_identifier=django_filters.CharFilter(label='Project Identifier')
    project_title=django_filters.CharFilter(label='Project Title')
    type=django_filters.CharFilter()
    county=django_filters.CharFilter()
    subgrantee=django_filters.CharFilter()
    class Meta:
        model = Projects
        fields = ['state','disaster_number','project_identifier','project_title','type','county','subgrantee']