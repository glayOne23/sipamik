# Generated by Django 4.1 on 2024-02-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lembaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniid', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('namasingkat', models.CharField(blank=True, max_length=255, null=True)),
                ('superunit', models.CharField(max_length=255)),
                ('namasuper', models.CharField(max_length=255)),
                ('jenis_id', models.IntegerField(blank=True, null=True)),
                ('jenis', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
