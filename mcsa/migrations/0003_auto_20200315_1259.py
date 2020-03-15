# Generated by Django 3.0.3 on 2020-03-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcsa', '0002_usermonthyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermonthyear',
            name='userMonth',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='usermonthyear',
            name='userYear',
            field=models.IntegerField(choices=[(0, '2020'), (1, '2021'), (2, '2022'), (3, '2023'), (4, '2024'), (5, '2025'), (6, '2026'), (7, '2027'), (8, '2028'), (9, '2029'), (10, '2030')], default=0, verbose_name='Year'),
        ),
    ]