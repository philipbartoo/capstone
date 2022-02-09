from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,FormView,View
from .models import Disasters, Enrichment, Projects,Csvs
from .forms import RegisterForm,NewEnrichmentForm,EditEnrichmentForm
from django.http.response import HttpResponseRedirect
from .filters import DisasterFilter,ProjectFilter
#from django_filters.views import FilterView
#from tablib import Dataset
#from .resources import DisasterResource
#import csv
#from django.views.generic.edit import FormView


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    LOGIN_REDIRECT_URL = ''

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    

class HomeView(LoginRequiredMixin, ListView):
    model = Disasters
    template_name = 'home.html'
    #ordering = ['-date_created']
    login_url = "login"



class DisastersDetailView(LoginRequiredMixin, DetailView):
    model = Disasters
    template_name = 'disastersdetails.html'
    login_url = "login"

class DisastersListView(LoginRequiredMixin, ListView):
    model = Disasters
    template_name = 'disasterslist.html'
    login_url = "login"



class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Projects
    template_name = 'projectdetails.html'
    login_url = "login"

class ProjectListView(LoginRequiredMixin, ListView):
    model = Projects
    template_name = 'projectlist.html'
    login_url = "login"

class EnrichmentListView(LoginRequiredMixin, ListView):
    model = Enrichment
    template_name = 'enrichment_list.html'
    login_url = 'login'

class EnrichmentAddView(CreateView):
    form_class = NewEnrichmentForm
    template_name = 'enrichment_add.html'
    login_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EnrichmentDetailView(LoginRequiredMixin,DetailView):
    model = Enrichment
    template_name = 'enrichment_detail.html'
    login_url = 'login'

class EnrichmentEditView(LoginRequiredMixin,UpdateView):
    model = Enrichment
    form_class = EditEnrichmentForm
    template_name = 'enrichment_edit.html'
    login_url = 'login'

class EnrichmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrichment
    template_name = 'enrichment_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

def disaster_search_view(request):
    disaster_list=Disasters.objects.all()
    state_filter=DisasterFilter(request.GET,queryset=disaster_list)
    disaster_number_filter=DisasterFilter(request.GET,queryset=disaster_list)
    disaster_filter=DisasterFilter(request.GET,queryset=disaster_list)
    return render(request,'disasterfilter.html',{'state_filter':state_filter,'disaster_number_filter':disaster_number_filter,'filter':disaster_filter})

def home_search_view(request):
    disaster_list=Disasters.objects.all()
    state_filter=DisasterFilter(request.GET,queryset=disaster_list)
    disaster_number_filter=DisasterFilter(request.GET,queryset=disaster_list)
    disaster_filter=DisasterFilter(request.GET,queryset=disaster_list)
    return render(request,'home.html',{'state_filter':state_filter,'disaster_number_filter':disaster_number_filter,'filter':disaster_filter})

def project_search_view(request):
    project_list=Projects.objects.all()
    state=ProjectFilter(request.GET,queryset=project_list)
    disaster_number=ProjectFilter(request.GET,queryset=project_list)
    project_identifier=ProjectFilter(request.GET,queryset=project_list)
    project_title=ProjectFilter(request.GET,queryset=project_list)
    type=ProjectFilter(request.GET,queryset=project_list)
    county=ProjectFilter(request.GET,queryset=project_list)
    subgrantee=ProjectFilter(request.GET,queryset=project_list)
    project_filter=ProjectFilter(request.GET,queryset=project_list)
    return render(request,'projectlist.html',{'state':state,'disaster_number':disaster_number,'project_identifier':project_identifier,'project_title':project_title,'type':type,'county':county,'subgrantee':subgrantee,'project_filter':project_filter})


def upload_disaster_file(request):
    disasters_file=request.FILES['disaster_file']
    model=Csvs(disaster_file=disasters_file)
    model.save()
    

'''class UploadView(CreateView):
    model=Csvs
    fields=['disaster_file']
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context


def upload_disaster_file(request):
    if request.method == 'POST':
        form = UploadDisasterForm(request.POST,request.FILES)
        form.save()
    else:
        form=UploadDisasterForm()
        context={
            'form':form
        }
    return render(request,'upload.html',context)'''

'''disaster_file = request.FILES['disaster_file']
    model = Csvs(..., disaster_file=disaster_file)
    model.save()'''

'''def upload_file_view(request):
    form=CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvModelForm()
        obj=Csvs.objects.get(activated=False)
        Disasters.objects.all().delete()
        #disasters=Disasters()
        #form=ImportForm(request.POST or None, request.FILES or None)
        #file=request.FILES['test4.csv']
        
        with open(obj.file_name.path,'r',encoding='utf-8-sig') as csv_file:
            csv_reader=csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                disasters=Disasters()
                disasters.disaster_number=row["Disaster Number"]
                disasters.state=row["State"]
                print(row)
                disasters.save()
            obj.activated=True
            obj.save()
    
    return render(request, 'upload.html')'''


'''disaster_resource = DisasterResource()
        data_set = Dataset()
        if form.is_valid():
            file = request.FILES['test3.csv']
            imported_data = data_set.load(file.read())
            result = disaster_resource.import_data(data_set, dry_run=True)  # Test the data import

            if not result.has_errors():
                disaster_resource.import_data(data_set, dry_run=False)  # Actually import now

        else:
            form = ImportForm()'''
        


'''def upload_disaster_file(request):
    #form=CsvModelForm(request.POST, request.FILES)
    #form.save()
    #form=CsvModelForm()
    disaster_resource = DisasterResource()
    dataset = Dataset()
    new_disasters = request.FILES["test3.csv"]
    dataset.load(new_disasters.read().decode("utf-8"), format="csv")
    result = disaster_resource.import_data(dataset, dry_run=True, raise_errors=True)
    

    return render(request,'upload.html',{'form':form})'''


'''Disasters.objects.all().delete()
    new_disasters = request.FILES['test3.csv']
    with new_disasters as csv_file:
        csv_reader=csv.DictReader(csv_file,delimiter=",")
        for row in csv_reader:
            disasters=Disasters()
            disasters.disaster_number=row["Disaster Number"]
            disasters.state=row["State"]
            print(row)
            disasters.save()
   
    return render(request, 'upload.html')'''


'''class CustomCSVView(FormView):
    template_name = "upload.html"
    form_class = CSVUploadForm

    def handle(self, *args, **kwargs):
        Disasters.objects.all().delete()
        with open('test3.csv', encoding='utf-8-sig') as csv_file:
            csv_reader=csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                disasters=Disasters()
                disasters.disaster_number=row["Disaster Number"]
                disasters.state=row["State"]
                print(row)
                disasters.save()
                
                disasters_resource = DisasterResource()
    dataset=Dataset()'''


