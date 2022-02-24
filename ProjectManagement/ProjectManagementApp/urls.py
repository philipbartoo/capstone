from django.urls import path, include
from ProjectManagementApp import views
from .views import DisastersDetailView, DisastersListView,LoginInterfaceView,LogoutInterfaceView, ProjectDetailView,SignupView,EnrichmentListView,EnrichmentAddView,EnrichmentDetailView,EnrichmentEditView,EnrichmentDeleteView,UserEditView,DataView
from . import views
from django.views.generic.base import RedirectView

app_name='ProjectManagementApp'

urlpatterns = [
    path('', RedirectView.as_view(),name='index'),
    #path('home',HomeView.as_view(),name="home"),
    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(), name='logout'),
    path('register', SignupView.as_view(), name='register'),
    path('disaster',DisastersListView.as_view(),name='disasterslist'),
    path('disasters/<int:pk>',DisastersDetailView.as_view(), name='disastersdetails'),
    path('project', views.project_search_view, name='projectlist'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='projectdetail'),
    path('enrichment_list/',EnrichmentListView.as_view(),name='enrichment_list'),
    path('enrichment_add/',EnrichmentAddView.as_view(),name='enrichment_add'), 
    path('enrichment/<int:pk>',EnrichmentDetailView.as_view(), name='enrichment_detail'),
    path('enrichment/<int:pk>/edit',EnrichmentEditView.as_view(), name='enrichment_edit'),
    path('enrichment/<int:pk>/delete',EnrichmentDeleteView.as_view(),name='enrichment_delete'),
    path('disasterfilter',views.disaster_search_view,name='filter'),
    path('home',views.home_search_view,name='home'),
    path('upload_disaster',views.upload_disaster_file, name='upload_disaster'),
    path('upload_project',views.upload_project_file,name='upload_project'),
    path('administration',views.admin_view, name='administration'),
    path('data', DataView.as_view(),name='data')
    

    

]
