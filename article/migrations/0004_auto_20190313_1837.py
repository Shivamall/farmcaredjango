# Generated by Django 2.1.5 on 2019-03-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190313_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xaxis_data',
            name='name',
            field=models.IntegerField(help_text='Enter a Data..'),
        ),
        migrations.AlterField(
            model_name='xaxisdata',
            name='name',
            field=models.IntegerField(help_text='Enter a Data..'),
        ),
        migrations.AlterField(
            model_name='yaxis_data',
            name='name',
            field=models.IntegerField(help_text='Enter a Data..'),
        ),
        migrations.AlterField(
            model_name='yaxisdata',
            name='name',
            field=models.IntegerField(help_text='Enter a Data..'),
        ),
    ]