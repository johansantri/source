# Generated by Django 3.2.4 on 2023-11-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_course_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, choices=[('tecnologi', 'tecnologi'), ('law', 'law'), ('economic', 'economic'), ('social', 'social'), ('agriculture', 'agriculture'), ('mining', 'mining'), ('management', 'management'), ('program', 'program')], max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='effort',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='lang',
            field=models.CharField(blank=True, choices=[('en', 'english'), ('id', 'indonesia')], max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_of_questions',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='required_score_to_pas',
            field=models.IntegerField(blank=True, verbose_name='required score in %'),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.IntegerField(blank=True, help_text='durations of the quiz in minutes'),
        ),
        migrations.AlterField(
            model_name='course',
            name='type_course',
            field=models.CharField(blank=True, choices=[('self', 'self-paced'), ('instructor', 'instructor-paced')], max_length=10),
        ),
    ]
