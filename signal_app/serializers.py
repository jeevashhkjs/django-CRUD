from rest_framework import serializers
from .models import Users, UserScore


class serializer_user(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = "__all__"
