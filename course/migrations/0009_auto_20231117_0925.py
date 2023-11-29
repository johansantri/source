# Generated by Django 3.2.4 on 2023-11-17 09:25

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20231117_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('tecnologi', 'tecnologi'), ('law', 'law'), ('economic', 'economic'), ('social', 'social'), ('agriculture', 'agriculture'), ('mining', 'mining'), ('management', 'management'), ('program', 'program')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_overview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_year',
            field=models.IntegerField(default=course.models.current_year, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='effort',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_enrol',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_course',
            field=models.ImageField(null=True, upload_to=course.models.filepath),
        ),
        migrations.AlterField(
            model_name='course',
            name='lang',
            field=models.CharField(choices=[('en', 'english'), ('id', 'indonesia')], default='id', max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_of_questions',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='required_score_to_pas',
            field=models.IntegerField(null=True, verbose_name='required score in %'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_enrol',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.IntegerField(help_text='durations of the quiz in minutes', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='type_course',
            field=models.CharField(choices=[('self', 'self-paced'), ('instructor', 'instructor-paced')], default='self', max_length=10),
        ),
    ]
