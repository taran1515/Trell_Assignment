# Generated by Django 3.1.4 on 2020-12-09 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('duration', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timings', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('ticket', models.IntegerField()),
                ('purchased', models.BooleanField(default=False)),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trell.movie')),
            ],
        ),
    ]
