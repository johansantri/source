# Generated by Django 3.2.4 on 2023-11-27 06:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_subsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='sub_id_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]
