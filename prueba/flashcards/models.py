from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        This function returns the deck name
        """
        return "{}".format(self.name)


class Flashcard(models.Model):
    front_side = models.CharField(max_length=30)
    back_side = models.CharField(max_length=30)
    deck = models.ForeignKey(Deck, models.CASCADE)

    def __str__(self):
        """
        This function returns the flashcard sides and deck
        """
        # return str(self.front_side) + '' + str(self.back_side) + '' + str(self.deck.name)
        return "{} - {} - {}".format(self.front_side, self.back_side, self.deck.name)
        # return F"{self.front_side} {self.back_side} {self.deck.name}"
