# Generated by Django 3.2.4 on 2023-11-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_alter_section_section_id_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_section_name', models.CharField(max_length=250)),
            ],
        ),
    ]
