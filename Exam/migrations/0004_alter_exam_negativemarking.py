# Generated by Django 4.0.4 on 2022-06-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0003_alter_exam_courseid_alter_exam_negativemarking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='negativeMarking',
            field=models.CharField(max_length=50),
        ),
    ]
