# Generated by Django 3.0 on 2019-12-09 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=30)),
                ('jabatan', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=200)),
                ('jadwal_mulai', models.CharField(max_length=30)),
                ('jadwal_akhir', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=30)),
                ('nomor', models.IntegerField(max_length=5)),
                ('nilai_rata', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=30)),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_live_code', models.CharField(max_length=200)),
                ('banyak_soal', models.IntegerField(max_length=5)),
                ('bobot_nilai', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tanggal_pelaksanaan', models.DateTimeField(verbose_name='Jadwal_Ujian')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=200)),
                ('banyak_soal', models.IntegerField(max_length=5)),
                ('bobot_nilai', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
    ]
