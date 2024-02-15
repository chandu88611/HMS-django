# Generated by Django 4.0.4 on 2024-02-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('staff', '0002_remove_staff_assigned_patients_remove_staff_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='assigned_patients',
            field=models.ManyToManyField(blank=True, related_name='assigned_staff', to='patients.patient'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
