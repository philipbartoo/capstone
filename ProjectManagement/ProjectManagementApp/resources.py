'''from import_export import resources,fields
from .models import Disasters

class DisasterResource(resources.ModelResource):
    class Meta:
        model = Disasters
        fields=('disaster_number','state')'''