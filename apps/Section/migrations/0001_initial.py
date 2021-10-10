# Generated by Django 3.2.7 on 2021-10-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='C_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('r1', models.FloatField(blank=True, null=True, verbose_name='r1')),
                ('r2', models.FloatField(blank=True, null=True, verbose_name='r2')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': 'C形鋼断面性能',
                'verbose_name_plural': 'C形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='CT_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('r1', models.FloatField(blank=True, null=True, verbose_name='r1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': 'CT形鋼断面性能',
                'verbose_name_plural': 'CT形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='FB_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
            ],
            options={
                'verbose_name': 'FB断面性能',
                'verbose_name_plural': 'FB断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='H_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('r1', models.FloatField(blank=True, null=True, verbose_name='r1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': 'H形鋼断面性能',
                'verbose_name_plural': 'H形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='I_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('r1', models.FloatField(blank=True, null=True, verbose_name='r1')),
                ('r2', models.FloatField(blank=True, null=True, verbose_name='r2')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': 'I形鋼断面性能',
                'verbose_name_plural': 'I形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='L_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('r1', models.FloatField(blank=True, null=True, verbose_name='r1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('Iu', models.FloatField(blank=True, null=True, verbose_name='Iu')),
                ('Iv', models.FloatField(blank=True, null=True, verbose_name='Iv')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('ru', models.FloatField(blank=True, null=True, verbose_name='ru')),
                ('rv', models.FloatField(blank=True, null=True, verbose_name='rv')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': '山形鋼断面性能',
                'verbose_name_plural': '山形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='LH_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('t2', models.FloatField(blank=True, null=True, verbose_name='t2')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': '軽量H形鋼断面性能',
                'verbose_name_plural': '軽量H形鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='O_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
            ],
            options={
                'verbose_name': '鋼管断面性能',
                'verbose_name_plural': '鋼管断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='P_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': '角型鋼管断面性能',
                'verbose_name_plural': '角型鋼管断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='R_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('d', models.FloatField(blank=True, null=True, verbose_name='d')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
            ],
            options={
                'verbose_name': '棒鋼断面性能',
                'verbose_name_plural': '棒鋼断面形状一覧',
            },
        ),
        migrations.CreateModel(
            name='RC_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('H', models.FloatField(blank=True, null=True, verbose_name='H')),
                ('B', models.FloatField(blank=True, null=True, verbose_name='B')),
                ('C', models.FloatField(blank=True, null=True, verbose_name='C')),
                ('t1', models.FloatField(blank=True, null=True, verbose_name='t1')),
                ('A', models.FloatField(blank=True, null=True, verbose_name='A')),
                ('m', models.FloatField(blank=True, null=True, verbose_name='m')),
                ('Ix', models.FloatField(blank=True, null=True, verbose_name='Ix')),
                ('Iy', models.FloatField(blank=True, null=True, verbose_name='Iy')),
                ('rx', models.FloatField(blank=True, null=True, verbose_name='rx')),
                ('ry', models.FloatField(blank=True, null=True, verbose_name='ry')),
                ('Zx', models.FloatField(blank=True, null=True, verbose_name='Zx')),
                ('Zy', models.FloatField(blank=True, null=True, verbose_name='Zy')),
            ],
            options={
                'verbose_name': 'リップ溝形鋼断面性能',
                'verbose_name_plural': 'リップ溝形鋼断面形状一覧',
            },
        ),
    ]
