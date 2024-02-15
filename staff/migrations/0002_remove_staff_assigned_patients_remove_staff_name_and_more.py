# Generated by Django 4.0.4 on 2024-02-15 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='assigned_patients',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.AddField(
            model_name='staff',
            name='availability_status',
            field=models.CharField(choices=[('available', 'Available'), ('busy', 'Busy'), ('on_leave', 'On Leave')], default='available', max_length=20),
        ),
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateTimeField()),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
    ]
