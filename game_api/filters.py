from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets

from game_api.models import User, Subject, Score, Question, UserSubject
from game_api.serializers import UserSerializer, SubjectSerializer, ScoreSerializer, QuestionSerializer, \
    UserSubjectSerializer

LIKE = 'unaccent__icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
IN = 'in'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']  # Filtros disponíveis


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']  # Filtra por nome do assunto


class UserSubjectViewSet(viewsets.ModelViewSet):
    queryset = UserSubject.objects.all()
    serializer_class = UserSubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'subject']  # Filtra por usuário ou assunto


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']  # Filtra por assunto


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'subject', 'date', 'score']  # Filtros disponíveis
