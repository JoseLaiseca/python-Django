# Generated by Django 2.2 on 2020-02-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=128)),
                ('talle', models.IntegerField()),
                ('color', models.CharField(max_length=128)),
                ('lisa', models.BooleanField()),
                ('genero', models.IntegerField()),
            ],
        ),
    ]
