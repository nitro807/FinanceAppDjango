# Generated by Django 5.1.5 on 2025-01-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='type',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('income', 'Доход'), ('expense', 'Расход')], default='expense', max_length=7),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(default='Неизвестно', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, default='Неизвестно'),
            preserve_default=False,
        ),
    ]
