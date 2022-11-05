# Generated by Django 4.0.5 on 2022-11-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0005_alter_docsearch_end_time_alter_docsearch_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Speciality'},
        ),
        migrations.RemoveField(
            model_name='docsearch',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='docsearch',
            name='day_of_week',
        ),
        migrations.AddField(
            model_name='docsearch',
            name='day_of_week',
            field=models.ManyToManyField(to='doctor_search.dayofweek'),
        ),
        migrations.AlterField(
            model_name='docsearch',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctor_search.doctorgender'),
        ),
    ]
