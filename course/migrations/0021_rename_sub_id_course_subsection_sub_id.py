# Generated by Django 3.2.4 on 2023-11-27 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_subsection_sub_section_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsection',
            old_name='sub_id_course',
            new_name='sub_id',
        ),
    ]