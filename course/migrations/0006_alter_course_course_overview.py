# Generated by Django 3.2.4 on 2023-11-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_org_course_org_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_overview',
            field=models.TextField(blank=True, default=None),
        ),
    ]
