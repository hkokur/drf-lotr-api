from rest_framework import serializers

from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serilazer of the Character model
    """

    class Meta:
        model = Character
        fields = (
            "id",
            "name",
            "race",
            "birth",
            "gender",
            "death",
            "hair",
            "height",
            "realm",
            "spouse",
        )


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["id", "name", "race"]
