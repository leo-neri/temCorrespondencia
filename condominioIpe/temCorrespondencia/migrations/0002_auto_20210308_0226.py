# Generated by Django 3.1.7 on 2021-03-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temCorrespondencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encomenda',
            name='torre',
            field=models.CharField(blank=True, default='', editable=False, max_length=1, null=True),
        ),
    ]