# Generated by Django 2.1.7 on 2019-03-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodness', models.CharField(max_length=2)),
                ('country', models.CharField(choices=[('uk', 'UK'), ('us', 'USA'), ('in', 'India')], max_length=2)),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='date published')),
            ],
        ),
    ]
