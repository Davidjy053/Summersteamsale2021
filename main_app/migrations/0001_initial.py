# Generated by Django 3.2.4 on 2021-07-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ogprice', models.IntegerField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
                ('afprice', models.IntegerField()),
            ],
        ),
    ]
