from django.db import models

class Survey(models.Model):
    title = models.CharField("Название опроса", max_length=100)
    description = models.CharField("Описание", max_length=200)
    begining_date = models.DateTimeField("Начало опроса")
    completion_date = models.DateTimeField("Окончание опроса")

    def str(self):
        return self.title



class TypeQuestion(models.Model):
    title = models.CharField("Тип вопроса", max_length=100)

    def str(self):
        return self.title



class Question(models.Model):
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        verbose_name="Опрос")
    question_text = models.CharField("Текст вопроса",max_length=200)
    number_question = models.PositiveSmallIntegerField("Номер вопроса")
    type_question = models.ForeignKey(
        TypeQuestion,
        verbose_name="Тип вопроса",
        on_delete=models.CASCADE)

    def str(self):
        return f"{self.question_text} к опросу {self.survey}"



class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Выберите вопрос")
    choice_text = models.CharField("Ответ",max_length=200)
    number_choice = models.PositiveSmallIntegerField("Номер ответа")

    def str(self):
        return self.choice_text