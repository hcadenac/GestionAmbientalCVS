# Generated by Django 3.0.7 on 2021-04-08 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondga', '0015_auto_20210327_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Responsable_DGA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestiondga.DGA'),
        ),
    ]
