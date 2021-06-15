from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import datetime

class Survey(models.Model):
    title = models.CharField("Название опроса", max_length=100)
    description = models.CharField("Описание", max_length=200)
    beginning_date = models.DateTimeField("Начало опроса")
    completion_date = models.DateTimeField("Окончание опроса")

    def save(self, *args, **kwargs):
        date_five_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
        if self.beginning_date.isoformat() < date_five_minutes_ago.isoformat():
            raise AttributeError("Дата начала опроса не должна превышать 5 минутный интервал "
                                 "от текущей даты")
        elif self.beginning_date > self.completion_date:
            raise AttributeError("Дата начала опроса не может быть позже даты завершения.")
        super(Survey, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class TypeQuestion(models.Model):
    title = models.CharField("Тип вопроса", max_length=100)

    def __str__(self):
        return self.title



class Question(models.Model):
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        verbose_name="Опрос",
        related_name="quest")
    question_text = models.CharField("Текст вопроса",max_length=200)
    number_question = models.PositiveSmallIntegerField("Номер вопроса")
    type_question = models.ForeignKey(
        TypeQuestion,
        verbose_name="Тип вопроса",
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_text} к опросу {self.survey}"



class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Выберите вопрос",
        related_name="choices")
    choice_text = models.CharField("Ответ",max_length=200)
    number_choice = models.PositiveSmallIntegerField("Номер ответа")

    def __str__(self):
        return self.choice_text



class Questionnaire(models.Model):
    user_id = models.PositiveIntegerField("ID пользователя")
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        verbose_name="Опрос",
        related_name= "quests")

    def __str__(self):
        return f"({self.survey} пользователя {self.user_id})"


@receiver(pre_save,sender=Questionnaire)
def checkuser(sender, instance, **kwargs):
        q = Questionnaire.objects.filter(
            survey=instance.survey).filter(
            user_id=instance.user_id)
        if q.exists():
            q.delete()

@receiver(post_save, sender=Questionnaire)
def answers(sender, instance, **kwargs):

    answers = Answer.objects.filter(questionnaire=instance.id)
    if answers.exists():
        answers.delete()

    q=instance.survey.quest.all().values_list("id", flat=True)
    for i in q:
        Answer.objects.create(
            questionnaire = Questionnaire.objects.get(pk=instance.id),
            question = Question.objects.get(pk=i)
        )



class Answer(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name="Анкета",
        related_name="ans"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Вопрос"
    )
    answer = models.CharField(
        "Ответ",
        max_length=100,
        null=True,
        blank=True)