# Generated by Django 2.1.5 on 2019-03-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190307_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chartjs',
            fields=[
                ('chart_id', models.AutoField(primary_key=True, serialize=False)),
                ('chart_title', models.CharField(max_length=250)),
                ('xaxis_name', models.CharField(max_length=250)),
                ('yaxis_name', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Xaxis_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Enter a Data..', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Yaxis_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Enter a Data..', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='chartjs',
            name='xaxis_data',
            field=models.ManyToManyField(help_text='Select a Options', to='article.Xaxis_data'),
        ),
        migrations.AddField(
            model_name='chartjs',
            name='yaxis_data',
            field=models.ManyToManyField(help_text='Select a Options', to='article.Yaxis_data'),
        ),
    ]