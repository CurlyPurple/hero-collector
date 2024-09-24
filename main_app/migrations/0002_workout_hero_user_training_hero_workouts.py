# Generated by Django 4.2.16 on 2024-09-22 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Training Date')),
                ('activity', models.CharField(choices=[('S', 'Save a kitten in Tree'), ('F', 'Fight a villain'), ('T', 'Train')], default='S', max_length=1)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.hero')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='hero',
            name='workouts',
            field=models.ManyToManyField(to='main_app.workout'),
        ),
    ]
