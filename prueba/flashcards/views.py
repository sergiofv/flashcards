from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Flashcard, Deck
from .serializers import FlashcardSerializer, DeckSerializer


class FlashcardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing flashcards.
    """
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [AllowAny]
    #http_method_names = ['GET', 'POST', 'DELETE', 'PUT']


class DeckViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing decks.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [AllowAny]
