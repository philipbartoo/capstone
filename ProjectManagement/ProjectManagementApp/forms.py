from django import forms
from .models import Enrichment,Csvs,Projects
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewEnrichmentForm(forms.ModelForm):

    submitted_off_waitlist_date=forms.DateField(label='Date Submitted Off Waitlist',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    date_assigned_to_program_reviewer=forms.DateField(label='Date Assigned to Program Reviewer',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    initial_review_complete_date=forms.DateField(label='Date Initial Review Complete',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    date_assigned_to_ehp_reviewer=forms.DateField(label='Date Assigned to EHP Reviewer',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_triage_complete_date=forms.DateField(label='Date EHP Triage Complete',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_transmital_date=forms.DateField(label='EHP Transmital Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_application_completeness_date=forms.DateField(label='EHP Application Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_clearance_date=forms.DateField(label='EHP Clearance Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_kickoff_date=forms.DateField(label='EHP Kickoff Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_transmital_date_phase_2=forms.DateField(label='EHP Transmital Date Phase 2',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    eo_inital_public_notice_posted_date=forms.DateField(label='EO Initial Public Notice Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    eo_final_public_notice_posted=forms.DateField(label='EO Final Public Notice Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    sent_to_contractor=forms.DateField(label='Date Sent to Contractor',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_review_complete_date=forms.DateField(label='EHP Review Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    lpn_available_to_obligate_date=forms.DateField(label='LPN Available to Obligate Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    lpn_submitted_date=forms.DateField(label='LPN Submitted Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    spend_plan_date=forms.DateField(label='Spend Plan Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    hma_review_complete_date=forms.DateField(label='HMA Review Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    actual_project_completion_date=forms.DateField(label='Actual Project Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    award_letter_activity_complete_date=forms.DateField(label='Award Letter Activity Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    anticipated_activity_completion_date=forms.DateField(label='Anticipated Activity Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    plan_expiration_date=forms.DateField(label='Plan Expiration Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    award_complete_date=forms.DateField(label='Award Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    actual_activity_completion_date=forms.DateField(label='Actual Activity Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    site_visit_date=forms.DateField(label='Site Visit Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    closeout_submission_date=forms.DateField(label='Closeout Submission Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_final_review_date=forms.DateField(label='EHP Final Review Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    program_final_review_date=forms.DateField(label='Program Final Review Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    closeout_complete_date=forms.DateField(label='Closeout Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    rfi_sent_date=forms.DateField(label='RFI Sent Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    
    assigned_project_identifier=forms.ModelChoiceField(queryset=Projects.objects.all(),label='Project Identifier',widget=forms.Select(attrs={'class': 'form-control'}))

    project_deliverable_number=forms.CharField(max_length=6, required=False,label='Deliverable Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    project_deliverable_title=forms.CharField(max_length=100, required=False,label='Deliverable Title',widget=forms.TextInput(attrs={'class':'form-control'}))
    submitted_off_waitlist=forms.BooleanField(label='Submitted Off Waitlist',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    program_reviewer=forms.CharField(max_length=100,required=False,label='Program Reviewer',widget=forms.TextInput(attrs={'class':'form-control'}))
    ehp_reviewer=forms.CharField(max_length=100,required=False,label='EHP Reviewer',widget=forms.TextInput(attrs={'class':'form-control'}))
    catex=forms.CharField(max_length=100,required=False,label='CATEX',widget=forms.TextInput(attrs={'class':'form-control'}))
    nepa_level=forms.CharField(max_length=100,required=False,label='NEPA Level',widget=forms.TextInput(attrs={'class':'form-control'}))
    lead_federal_agency=forms.CharField(max_length=100,required=False,label='Lead Federal Agency',widget=forms.TextInput(attrs={'class':'form-control'}))
    hmtap_contractor=forms.CharField(max_length=100,required=False,label='HMTAP Contractor',widget=forms.TextInput(attrs={'class':'form-control'}))

    esa_sec_7_notes=forms.CharField(max_length=500,required=False,label='ESA Sec 7 Notes',widget=forms.Textarea(attrs={'class':'form-control'}))
    comments=forms.CharField(max_length=100000,required=False,label='Comments',widget=forms.Textarea(attrs={'class':'form-control'}))
    
    
    phased_project=forms.BooleanField(label='Phased Project',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    initial_review_complete=forms.BooleanField( label='Initial Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_triage_complete=forms.BooleanField( label='EHP Triage Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    archaeological_monitoring_required=forms.BooleanField( label='Archaeological Monitoring Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    clean_water_act_coordination_required=forms.BooleanField( label='Clean Water Act Coordination Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    tribal_monitoring_required=forms.BooleanField( label='Tribal Monitoring Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    nfms_no_effect=forms.BooleanField( label='NFMS No Effect',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    usfws_no_effect=forms.BooleanField( label='USFWS No Effect',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    eo_11988_90=forms.BooleanField( label='EO 11988/90',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    additional_environmental_attachments=forms.BooleanField( label='Additional Environmental Attachments',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    rec_complete=forms.BooleanField( label='Rec Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_review_complete=forms.BooleanField( label='EHP Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    lpn_needed=forms.BooleanField( label='LPN Needed',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    hma_review_complete=forms.BooleanField( label='HMA Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    mitigation_coorespondence_complete=forms.BooleanField( label='Mitigation Coorespondence Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    award_complete=forms.BooleanField( label='Award Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    non_compliance_memo=forms.BooleanField( label='Non-Compliance Memo',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    financial_specialist_final_review=forms.BooleanField( label='Financial Final Review',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    deobligation_required=forms.BooleanField( label='Deobligation Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_final_review_complete=forms.BooleanField( label='EHP Final Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    program_final_review_complete=forms.BooleanField( label='Program Final Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    closeout_complete=forms.BooleanField( label='Closeout Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    rfi_required=forms.BooleanField( label='RFI Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    awaiting_rfi_response=forms.BooleanField( label='RFI Response Received',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))





    class Meta:
        model = Enrichment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class EditEnrichmentForm(forms.ModelForm):
    submitted_off_waitlist_date=forms.DateField(label='Date Submitted Off Waitlist',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    date_assigned_to_program_reviewer=forms.DateField(label='Date Assigned to Program Reviewer',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    initial_review_complete_date=forms.DateField(label='Date Initial Review Complete',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    date_assigned_to_ehp_reviewer=forms.DateField(label='Date Assigned to EHP Reviewer',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_triage_complete_date=forms.DateField(label='Date EHP Triage Complete',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_transmital_date=forms.DateField(label='EHP Transmital Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_application_completeness_date=forms.DateField(label='EHP Application Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_clearance_date=forms.DateField(label='EHP Clearance Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_kickoff_date=forms.DateField(label='EHP Kickoff Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_transmital_date_phase_2=forms.DateField(label='EHP Transmital Date Phase 2',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    eo_inital_public_notice_posted_date=forms.DateField(label='EO Initial Public Notice Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    eo_final_public_notice_posted=forms.DateField(label='EO Final Public Notice Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    sent_to_contractor=forms.DateField(label='Date Sent to Contractor',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_review_complete_date=forms.DateField(label='EHP Review Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    lpn_available_to_obligate_date=forms.DateField(label='LPN Available to Obligate Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    lpn_submitted_date=forms.DateField(label='LPN Submitted Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    spend_plan_date=forms.DateField(label='Spend Plan Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    hma_review_complete_date=forms.DateField(label='HMA Review Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    actual_project_completion_date=forms.DateField(label='Actual Project Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    award_letter_activity_complete_date=forms.DateField(label='Award Letter Activity Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    anticipated_activity_completion_date=forms.DateField(label='Anticipated Activity Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    plan_expiration_date=forms.DateField(label='Plan Expiration Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    award_complete_date=forms.DateField(label='Award Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    actual_activity_completion_date=forms.DateField(label='Actual Activity Completion Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    site_visit_date=forms.DateField(label='Site Visit Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    closeout_submission_date=forms.DateField(label='Closeout Submission Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    ehp_final_review_date=forms.DateField(label='EHP Final Review Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    program_final_review_date=forms.DateField(label='Program Final Review Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    closeout_complete_date=forms.DateField(label='Closeout Complete Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    rfi_sent_date=forms.DateField(label='RFI Sent Date',required=False,widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control'}))
    
    assigned_project_identifier=forms.ModelChoiceField(queryset=Projects.objects.all(),label='Project Identifier',widget=forms.Select(attrs={'class': 'form-control'}))

    project_deliverable_number=forms.CharField(max_length=6, required=False,label='Deliverable Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    project_deliverable_title=forms.CharField(max_length=100, required=False,label='Deliverable Title',widget=forms.TextInput(attrs={'class':'form-control'}))
    submitted_off_waitlist=forms.BooleanField(label='Submitted Off Waitlist',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    program_reviewer=forms.CharField(max_length=100,required=False,label='Program Reviewer',widget=forms.TextInput(attrs={'class':'form-control'}))
    ehp_reviewer=forms.CharField(max_length=100,required=False,label='EHP Reviewer',widget=forms.TextInput(attrs={'class':'form-control'}))
    catex=forms.CharField(max_length=100,required=False,label='CATEX',widget=forms.TextInput(attrs={'class':'form-control'}))
    nepa_level=forms.CharField(max_length=100,required=False,label='NEPA Level',widget=forms.TextInput(attrs={'class':'form-control'}))
    lead_federal_agency=forms.CharField(max_length=100,required=False,label='Lead Federal Agency',widget=forms.TextInput(attrs={'class':'form-control'}))
    hmtap_contractor=forms.CharField(max_length=100,required=False,label='HMTAP Contractor',widget=forms.TextInput(attrs={'class':'form-control'}))

    esa_sec_7_notes=forms.CharField(max_length=500,required=False,label='ESA Sec 7 Notes',widget=forms.Textarea(attrs={'class':'form-control'}))
    comments=forms.CharField(max_length=100000,required=False,label='Comments',widget=forms.Textarea(attrs={'class':'form-control'}))
    
    
    phased_project=forms.BooleanField(label='Phased Project',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    initial_review_complete=forms.BooleanField( label='Initial Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_triage_complete=forms.BooleanField( label='EHP Triage Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    archaeological_monitoring_required=forms.BooleanField( label='Archaeological Monitoring Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    clean_water_act_coordination_required=forms.BooleanField( label='Clean Water Act Coordination Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    tribal_monitoring_required=forms.BooleanField( label='Tribal Monitoring Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    nfms_no_effect=forms.BooleanField( label='NFMS No Effect',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    usfws_no_effect=forms.BooleanField( label='USFWS No Effect',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    eo_11988_90=forms.BooleanField( label='EO 11988/90',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    additional_environmental_attachments=forms.BooleanField( label='Additional Environmental Attachments',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    rec_complete=forms.BooleanField( label='Rec Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_review_complete=forms.BooleanField( label='EHP Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    lpn_needed=forms.BooleanField( label='LPN Needed',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    hma_review_complete=forms.BooleanField( label='HMA Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    mitigation_coorespondence_complete=forms.BooleanField( label='Mitigation Coorespondence Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    award_complete=forms.BooleanField( label='Award Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    non_compliance_memo=forms.BooleanField( label='Non-Compliance Memo',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    financial_specialist_final_review=forms.BooleanField( label='Financial Final Review',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    deobligation_required=forms.BooleanField( label='Deobligation Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    ehp_final_review_complete=forms.BooleanField( label='EHP Final Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    program_final_review_complete=forms.BooleanField( label='Program Final Review Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    closeout_complete=forms.BooleanField( label='Closeout Complete',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    rfi_required=forms.BooleanField( label='RFI Required',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    awaiting_rfi_response=forms.BooleanField( label='RFI Response Received',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','class': 'checkbox-inline'}))
    class Meta:
        model = Enrichment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

            
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
    
