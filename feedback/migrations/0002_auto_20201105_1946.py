# Generated by Django 3.1.2 on 2020-11-05 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20201103_1235'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.menu'),
        ),
    ]