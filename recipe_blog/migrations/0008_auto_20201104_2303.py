# Generated by Django 3.1.2 on 2020-11-04 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20201103_1235'),
        ('recipe_blog', '0007_auto_20201104_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='recipepost',
            name='slug',
        ),
        migrations.AddField(
            model_name='comment',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='menu.menu'),
        ),
    ]
