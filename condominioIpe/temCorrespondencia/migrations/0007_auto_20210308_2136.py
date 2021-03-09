# Generated by Django 3.1.7 on 2021-03-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temCorrespondencia', '0006_auto_20210308_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encomenda',
            name='status',
            field=models.CharField(choices=[('naoRetiradoP', 'Não Retirado (P)'), ('naoRetiradoFP', 'Não Retirado (FP)'), ('retirado', 'Retirado'), ('retiradoOP', 'Retirado (outra pessoa)')], default='naoRecebidoP', max_length=30),
        ),
    ]
