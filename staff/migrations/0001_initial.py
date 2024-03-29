# Generated by Django 4.0.4 on 2024-02-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse'), ('administrative', 'Administrative Staff'), ('other', 'Other')], max_length=50)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_patients', models.ManyToManyField(blank=True, related_name='assigned_staff', to='patients.patient')),
            ],
        ),
    ]
