from django.contrib.auth.models import AbstractUser
from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=10)

    def __str__(self):
        return self.subject

class User(AbstractUser):
    name = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subject_choice = models.CharField(max_length=10, blank=True, null=True)

    # Define o campo utilizado como identificador único (username)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS deve incluir todos os campos obrigatórios ao criar um superusuário, exceto o USERNAME_FIELD e o password
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.subject.subject}'

class Question(models.Model):
    question_text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject.subject}: {self.question_text}'

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.subject.subject}: {self.score} pontos'
