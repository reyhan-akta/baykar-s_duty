# Generated by Django 5.0.1 on 2024-01-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihalar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
