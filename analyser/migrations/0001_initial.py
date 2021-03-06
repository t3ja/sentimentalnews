# Generated by Django 2.1.7 on 2019-03-13 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=10000)),
                ('country', models.CharField(choices=[('uk', 'UK'), ('us', 'USA'), ('in', 'India')], max_length=2)),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='date published')),
                ('analysed_at', models.DateTimeField(blank=True, verbose_name='date article created')),
                ('label', models.CharField(choices=[('0', 'NEGATIVE'), ('1', 'POSITIVE'), ('2', 'NEUTRAL')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_label', models.CharField(choices=[('0', 'NEGATIVE'), ('1', 'POSITIVE'), ('2', 'NEUTRAL')], max_length=1)),
                ('votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(verbose_name='date article created')),
                ('updated', models.DateTimeField(verbose_name='date article updated')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyser.Article')),
            ],
        ),
    ]
