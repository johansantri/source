# Generated by Django 3.2.4 on 2023-11-20 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_rename_course_section_id_section_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='course_id',
            new_name='course_section_id',
        ),
    ]
