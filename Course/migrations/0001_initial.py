# Generated by Django 4.0.4 on 2022-05-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=300, null=True)),
                ('examName1', models.CharField(max_length=100, null=True)),
                ('examName2', models.CharField(max_length=100, null=True)),
                ('examName3', models.CharField(max_length=100, null=True)),
                ('examName4', models.CharField(max_length=100, null=True)),
                ('examName5', models.CharField(max_length=100, null=True)),
                ('examName6', models.CharField(max_length=100, null=True)),
                ('examName7', models.CharField(max_length=100, null=True)),
                ('examName8', models.CharField(max_length=100, null=True)),
                ('examName9', models.CharField(max_length=100, null=True)),
                ('examName10', models.CharField(max_length=100, null=True)),
                ('subjectName1', models.CharField(max_length=200, null=True)),
                ('subjectName2', models.CharField(max_length=200, null=True)),
                ('subjectName3', models.CharField(max_length=200, null=True)),
                ('subjectName4', models.CharField(max_length=200, null=True)),
                ('subjectName5', models.CharField(max_length=200, null=True)),
                ('subjectName6', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
