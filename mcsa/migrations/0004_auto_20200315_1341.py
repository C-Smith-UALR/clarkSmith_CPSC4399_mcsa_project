# Generated by Django 3.0.3 on 2020-03-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcsa', '0003_auto_20200315_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermonthyear',
            name='userYear',
            field=models.IntegerField(choices=[(2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030')], default=2020, verbose_name='Year'),
        ),
    ]
