# Generated by Django 4.1 on 2024-02-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pendampingan', '0002_karyawan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurikulum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('jumlah_sks', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('uniid_pengampu', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kurikulum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendampingan.kurikulum')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
