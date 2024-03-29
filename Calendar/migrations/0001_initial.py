# Generated by Django 5.0.1 on 2024-01-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('color_code', models.CharField(max_length=6)),
                ('location', models.CharField(max_length=100)),
                ('team_img', models.ImageField(upload_to='pictures/')),
            ],
        ),
    ]
