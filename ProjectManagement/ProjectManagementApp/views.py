
from encodings import utf_8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,FormView,View
from .models import Disasters, Enrichment, Projects,Csvs
from .forms import RegisterForm,NewEnrichmentForm,EditEnrichmentForm
from django.http.response import HttpResponseRedirect
from .filters import DisasterFilter,ProjectFilter
#from django_filters.views import FilterView
#from tablib import Dataset
#from .resources import DisasterResource
import csv
#from django.views.generic.edit import FormView
from datetime import datetime
#from dateutil import parser
import pandas as pd
import numpy as np
import re



class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

class UserEditView(UpdateView):
    form_class=UserChangeForm
    template_name="profile.html"
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user


class HomeView(LoginRequiredMixin,ListView):
    model = Disasters
    template_name = 'home.html'
    ordering = ['-disaster_number']
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        return HttpResponse("User Profile View")




class DisastersDetailView(DetailView):
    model = Disasters
    template_name = 'disastersdetails.html'
    login_required=True
    redirect_field_name = 'redirect_to'
    

class DisastersListView(ListView):
    model = Disasters
    template_name = 'disasterslist.html'
    login_required=True


    


class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'projectdetails.html'
    

class ProjectListView(ListView):
    model = Projects
    template_name = 'projectlist.html'
    

class EnrichmentListView(ListView):
    model = Enrichment
    template_name = 'enrichment_list.html'
    

class EnrichmentAddView(CreateView):
    form_class = NewEnrichmentForm
    template_name = 'enrichment_add.html'
    success_url=reverse_lazy('ProjectManagementApp:home')
    

    '''def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())'''

class EnrichmentDetailView(DetailView):
    model = Enrichment
    template_name = 'enrichment_detail.html'
    

class EnrichmentEditView(UpdateView):
    model = Enrichment
    form_class = EditEnrichmentForm
    template_name = 'enrichment_edit.html'
    success_url = reverse_lazy('ProjectManagementApp:home')
    

class EnrichmentDeleteView(DeleteView):
    model = Enrichment
    template_name = 'enrichment_delete.html'
    success_url = reverse_lazy('ProjectManagementApp:home')

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
    
    if request.method=='POST':
        print(request.FILES)
        disasters_file=request.FILES['disaster_file'].file
        Disasters.objects.all().delete()
            
        lines=disasters_file.readlines()
        count=0
        for line in lines:
            if count==0:
                print(line)
                count+=1
                continue
            line=line.decode("utf-8")
            line=str(line)
            field=line.split(",")


            disasters=Disasters()
            disasters.disaster_number=str(field[0]).strip('"')

            disasters.state=str(field[1]).strip('"')
            disasters.number_of_projects=str(field[2]).strip('"')

            data=str(field[3]).strip('"')
            if data=='':
                data='0.00'
            disasters.twelve_month_lock_in_amount=float(data)

            data=str(field[4]).strip('"')
            if data=='':
                data='0.00'
            disasters.locked_in_ceiling_amount=float(data)
           
            data=str(field[5]).strip('"')
            if data=='':
                data='0.00'
            disasters.mt_project_dollars_available=float(data)

            data=str(field[6]).strip('"')
            if data=='':
                data='0.00'
            disasters.mt_federal_share_obligated=float(data)
           
            data=str(field[7]).strip('"')
            if data=='':
                data='0.00'
            disasters.mt_dollars_available=float(data)

            data=str(field[8]).strip('"')
            if data=='':
                data='0.00'
            disasters.allocated_total_amount=float(data)

            disasters.number_of_approved_projects=str(field[9]).strip('"')
            disasters.number_of_pending_projects=str(field[10]).strip('"')
            
            data=str(field[11]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            print(f'Disaster Declaration: {data}')
            disasters.declaration_date=data

            data=str(field[12]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
                #print(f'PoP End: {data}')
            disasters.disaster_period_of_performance_end_date=data

            data=str(field[13]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
                #print(f'Due Date for New Apps: {data}')
            disasters.disaster_due_date_for_new_apps=data

            data=str(field[14]).strip('"')
            if data=='':
                data='0.00'
            disasters.available_recipient_management_costs=float(data)
            
            data=str(field[15]).strip('"')
            if data=='':
                data='0.00'
            disasters.available_subrecipient_management_costs=float(data)
            
            data=str(field[16]).strip('"')
            if data=='':
                data='0.00'
            disasters.projected_recipient_management_costs=float(data)
            
            data=str(field[17]).strip('"')
            if data=='':
                data='0.00'
            disasters.projected_subrecipient_management_costs=float(data)
            
            data=str(field[18]).strip('"')
            if data=='':
                data='0.00'
            disasters.available_initiative_amount=float(data)
            
            data=str(field[19]).strip('"')
            if data=='':
                data='0.00'
            disasters.available_planning_amount=float(data)
            
            data=str(field[20]).strip('"')
            if data=='':
                data='0.00'
            disasters.projected_initiative_amount=float(data)
            
            data=str(field[21]).strip('"')
            if data=='':
                data='0.00'
            disasters.projected_regular_amount=float(data)
            
            data=str(field[22]).strip('"')
            if data=='':
                data='0.00'
            disasters.projected_planning_amount=float(data)
            
            #disasters.disaster_closeout_status=str(field[23]).strip('"')
            
            data=str(field[23]).strip('"')
            data=data.strip()
            disasters.disaster_closeout_status=data.rstrip('"')

            data=str(field[24]).strip('"')
            data=data.strip()
            disasters.hmgp_closeout_status=data.rstrip('"')
            
            #disasters.disaster_number=line[1]
            #disasters.state=line[2]
            disasters.save()
            count+=1

        return HttpResponseRedirect(reverse_lazy('ProjectManagementApp:home'))
            
    elif request.method=='GET':
        return render (request, 'upload_disaster.html')
    
def upload_project_file(request):
    if request.method=='POST':
        print(request.FILES)
        projects_file=request.FILES['project_file'].file
        Projects.objects.all().delete()
        
            
        lines=projects_file.readlines()
        count=0
        for line in lines:
            if count==0:
                count+=1
                continue
            
            
            line=line.decode("utf-8")
            line=str(line)
            
            #line=line.replace('\r','')
            #line=line.replace('\n','')
            #line=line.replace('\b','')
            field=line.split('","')
           
            projects=Projects()
            disaster_number=str(field[0]).strip('"')
            #print(disaster_number)
            projects.assigned_disaster_number=Disasters.objects.get(disaster_number=disaster_number)
            #print(projects.assigned_disaster_number)
            
            projects.county=str(field[2]).strip()
            #print(f'Project County: {projects.county}')
            
            projects.program_area=str(field[3]).strip('"')

            projects.project_identifier=str(field[4]).strip('"')
            #print(f'Project Identifier: {projects.project_identifier}')
            projects.application_id=str(field[5]).strip('"')
            projects.primary_hazard=str(field[6]).strip('"')
            #print(projects.primary_hazard)

            projects.type=str(field[7]).strip('"')
            #print(f'Project type: {projects.type}')
            projects.project_title=str(field[8])
            #print(f'Project title: {projects.project_title}')
            projects.project_counties=str(field[9]).strip('"')
            projects.status=str(field[10]).strip('"')
            projects.subgrantee=str(field[11]).strip('"')
            
            data=str(field[12]).strip('"')
            if data=='':
                data='0.00'
            data=data.rstrip('%')
            projects.cost_share_percent=float(data)

            data=str(field[13]).strip('"')
            if data=='':
                data='0.00'
            data=data.lstrip('$')
            #print(f'Fed share proposed: {data}')
            projects.federal_share_proposed=float(data)

            data=str(field[14]).strip('"')
            data=data.lstrip('$')
            if data=='':
                data='0.00'
            data=data.lstrip('$')
            #print(f'Project amt: {data}')
            projects.project_amount=data

            data=str(field[15]).strip('"')
            data=data.lstrip('$')
            if data=='':
                data='0.00'
            #print(f'Fed share obligated: {data}')
            projects.federal_share_obligated=float(data)
            
            data=str(field[16]).strip('"')
            if data=='':
                data='0.00'
            projects.non_federal_share=float(data)

            data=str(field[17]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            #print(f'Disaster Declaration: {data}')
            projects.date_initially_approved=data

            data=str(field[18]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            #print(f'PoP End: {data}')
            projects.date_awarded=data

            data=str(field[19]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            #print(f'Disaster Declaration: {data}')
            projects.date_approved=data

            data=str(field[20]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            #print(f'Disaster Declaration: {data}')
            projects.date_closed=data

            #projects.subgrantee_tribal_indicator=str(field[21]).strip('"')
            #projects.phased_project=str(field[22]).strip('"')

            data=str(field[23]).strip('"')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            #print(f'Disaster Declaration: {data}')
            projects.date_received=data

            data=str(field[24]).strip('"')
            #print(f'date_submitted: {data}')
            data=pd.to_datetime(data)
            data=str(data.date())
            if data=='NaT':
                data=None
            projects.date_submitted=data

            projects.environmental_document_type=str(field[25]).strip('"')
            #print(f'environmental_document_type: {projects.environmental_document_type}')

            projects.save()
            count+=1
            #print(count)

        return HttpResponseRedirect(reverse_lazy('ProjectManagementApp:projectlist'))

    elif request.method=='GET':
        return render (request, 'upload_project.html')


def admin_view(request):
    
    return render(request,'administration.html')
