# Generated by Django 3.2.10 on 2024-01-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llenar_quiniela', '0003_auto_20240130_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('prediccion', models.CharField(max_length=255)),
            ],
        ),
    ]