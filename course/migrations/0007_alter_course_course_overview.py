# Generated by Django 3.2.4 on 2023-11-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_course_course_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_overview',
            field=models.TextField(blank=True),
        ),
    ]
