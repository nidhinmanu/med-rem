# Generated by Django 4.0.5 on 2022-11-05 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0004_alter_docsearch_end_time_alter_docsearch_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsearch',
            name='end_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='doctor_search.availabletime'),
        ),
        migrations.AlterField(
            model_name='docsearch',
            name='start_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='doctor_search.availabletime'),
        ),
    ]