# Generated by Django 4.1.5 on 2023-01-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=500)),
                ('Stud_AGE', models.IntegerField()),
                ('Stud_Phn', models.IntegerField()),
                ('stud_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.city')),
                ('stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.course')),
            ],
        ),
    ]
