# Generated by Django 3.0.4 on 2020-09-18 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('course', models.TextField()),
                ('institution', models.CharField(max_length=200)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('address_type', models.CharField(blank=True, choices=[('Current', 'Current'), ('Permanent', 'Permanent')], max_length=12)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='AwardsAndHonour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
    ]
