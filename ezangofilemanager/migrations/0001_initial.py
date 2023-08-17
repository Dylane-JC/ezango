# Generated by Django 4.0.6 on 2023-08-17 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('ben_id', models.AutoField(primary_key=True, serialize=False)),
                ('ben_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('ref_id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_dos', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(blank=True, max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('is_connected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('op_id', models.AutoField(primary_key=True, serialize=False)),
                ('op_ref', models.CharField(max_length=6, unique=True)),
                ('op_type', models.CharField(max_length=255)),
                ('op_cli', models.CharField(max_length=255)),
                ('op_benf', models.CharField(max_length=255)),
                ('op_motif', models.TextField()),
                ('op_mtn_dev', models.DecimalField(decimal_places=2, max_digits=12)),
                ('op_date_creation', models.DateField(auto_now_add=True)),
                ('op_date_dpo_ord', models.DateField()),
                ('op_date_dpo_etrf', models.DateField()),
                ('op_date_sort_etrf', models.DateField()),
                ('op_date_sort_sygma', models.DateField()),
                ('op_date_dbi_xaf', models.DateField()),
                ('op_date_crd_awb', models.DateField()),
                ('op_date_mt103', models.DateField()),
                ('op_date_dbi_awb', models.DateField()),
                ('op_dev', models.CharField(max_length=3)),
                ('op_cvxaf', models.IntegerField()),
                ('op_status', models.CharField(max_length=15)),
                ('op_dlai_etrf', models.IntegerField(null=True)),
                ('op_dlai_sygma', models.IntegerField()),
                ('op_dlai_dxaf', models.IntegerField()),
                ('op_dlai_crdi_awb', models.IntegerField()),
                ('op_dlai_mt103', models.IntegerField()),
                ('op_dlai_dbi_awb', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ezangofilemanager.user')),
            ],
        ),
    ]
