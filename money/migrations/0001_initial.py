# Generated by Django 3.0.6 on 2020-10-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('manage_id', models.AutoField(primary_key=True, serialize=False)),
                ('manage_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Management',
                'verbose_name_plural': 'Chutiya',
            },
        ),
    ]
