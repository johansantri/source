# Generated by Django 3.2.4 on 2023-11-17 06:28

from django.db import migrations, models
import django.db.models.deletion
import partner.models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0009_partner_partner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_logo',
            field=models.ImageField(blank=True, null=True, upload_to=partner.models.filepath),
        ),
        migrations.CreateModel(
            name='Qourse_overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=250)),
                ('topic', models.CharField(max_length=250)),
                ('course_overview', models.TextField()),
                ('category', models.CharField(choices=[('tecnologi', 'tecnologi'), ('law', 'law'), ('economic', 'economic'), ('social', 'social'), ('agriculture', 'agriculture'), ('mining', 'mining'), ('management', 'management'), ('program', 'program')], max_length=50)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='durations of the quiz in minutes')),
                ('required_score_to_pas', models.IntegerField(verbose_name='required score in %')),
                ('level', models.CharField(choices=[('basic', 'basic'), ('medium', 'medium'), ('advanced', 'advanced')], max_length=10)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('qurations', 'qurations'), ('publish', 'publish'), ('pending', 'pending')], max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_enrol', models.DateField()),
                ('end_enrol', models.DateField()),
                ('effort', models.CharField(max_length=20)),
                ('lang', models.CharField(choices=[('en', 'english'), ('id', 'indonesia')], max_length=30)),
                ('type_coures', models.CharField(choices=[('self', 'self-paced'), ('instructor', 'instructor-paced')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=partner.models.filepath)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.partner')),
            ],
        ),
    ]
