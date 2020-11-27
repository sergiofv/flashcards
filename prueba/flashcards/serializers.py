from rest_framework import serializers
from .models import Flashcard, Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = "__all__"


class FlashcardSerializer(serializers.ModelSerializer):
    #deck = DeckSerializer(many=False, read_only=True)
    deck_name = serializers.SerializerMethodField(read_only=True)

    def get_deck_name(self, obj):
        return obj.deck.name

    class Meta:
        model = Flashcard
        fields = ["front_side", "back_side", "deck", "deck_name"]

