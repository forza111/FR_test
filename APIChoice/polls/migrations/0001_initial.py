# Generated by Django 2.2.10 on 2021-05-15 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название опроса')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('begining_date', models.DateTimeField(verbose_name='Начало опроса')),
                ('completion_date', models.DateTimeField(verbose_name='Окончание опроса')),
            ],
        ),
        migrations.CreateModel(
            name='TypeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Текст вопроса')),
                ('number_question', models.PositiveSmallIntegerField(verbose_name='Номер вопроса')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Survey', verbose_name='Опрос')),
                ('type_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.TypeQuestion', verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='Ответ')),
                ('number_choice', models.PositiveSmallIntegerField(verbose_name='Номер ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='Выберите вопрос')),
            ],
        ),
    ]
