# Generated by Django 3.2.7 on 2022-02-06 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagementApp', '0004_alter_enrichment_date_assigned_to_program_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrichment',
            name='project_deliverable_number',
            field=models.CharField(default=1, help_text='Enter unique tracking number', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enrichment',
            name='project_deliverable_title',
            field=models.CharField(default='1', help_text='Enter a Title', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='additional_environmental_attachments',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='amount_deobligated',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='archaeological_monitoring_required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='awaiting_rfi_response',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='award_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='catex',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='clean_water_act_coordination_required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='closeout_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='complexity',
            field=models.CharField(blank=True, choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('E', 'Extreme')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='date_assigned_to_ehp_reviewer',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='date_assigned_to_program_reviewer',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='deobligation_required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='ehp_final_review_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='ehp_review_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='ehp_reviewer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='ehp_triage_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='eo_11988_90',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='financial_specialist_final_review',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='hma_review_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='hmtap_contractor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='initial_review_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='lead_federal_agency',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='lpn_needed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='mitigation_coorespondence_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='nepa_level',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='nfms_no_effect',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='non_compliance_memo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='phased_project',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='program_final_review_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='program_reviewer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='project_category',
            field=models.CharField(blank=True, choices=[('R', 'Regular'), ('I', 'Initiative'), ('P', 'Planning'), ('AA', 'Advanced Assistance'), ('MC', 'Management Costs')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='rec_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='rfi_required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='submitted_off_waitlist',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='tribal_monitoring_required',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='usfws_no_effect',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
