from rest_framework import serializers
from .models import User, Subject, UserSubject, Question, Score


class UserSerializer(serializers.ModelSerializer):
    subject_choice = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'password', 'subject_choice']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Criação de usuário com senha criptografada
        user = User.objects.create_user(**validated_data)
        return user


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubject
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Criação de usuário com senha criptografada
        user = User.objects.create_user(
            name=validated_data['name'],
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
