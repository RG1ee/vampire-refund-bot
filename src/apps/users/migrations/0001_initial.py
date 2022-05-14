# Generated by Django 4.0.4 on 2022-05-14 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('telegram_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('current_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.address')),
            ],
            options={
                'verbose_name': 'Пользователь telegram',
                'verbose_name_plural': 'Пользователи telegram',
                'db_table': 'telegram_users',
            },
        ),
    ]