# Generated by Django 3.1.2 on 2020-11-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_auto_20201103_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='character',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
