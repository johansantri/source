# Generated by Django 4.2.7 on 2023-11-30 04:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='mk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='course.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='section_id_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
