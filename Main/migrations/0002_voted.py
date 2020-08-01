# Generated by Django 3.0.8 on 2020-08-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=100, verbose_name='User that has been voting')),
                ('poll_id', models.IntegerField(max_length=100, verbose_name='Poll')),
            ],
        ),
    ]
