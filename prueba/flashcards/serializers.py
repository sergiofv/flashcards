from rest_framework import serializers
from .models import Flashcard, Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = "__all__"


class FlashcardSerializer(serializers.ModelSerializer):
    deck = DeckSerializer(many=False, read_only=True)

    class Meta:
        model = Flashcard
        fields = "__all__"

