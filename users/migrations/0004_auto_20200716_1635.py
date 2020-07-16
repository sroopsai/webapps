# Generated by Django 3.0.8 on 2020-07-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_webapps_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='webapps',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]