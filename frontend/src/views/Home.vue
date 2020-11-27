<template>
  <div class="home">
    <h1>FLASHCARDS</h1>

    <div>
      <form @submit.prevent="addFlashcard">
        <h3 class="subtitle">Add new flashcard</h3>

        <div class="field">
          <label class="label">Frontside</label>
          <div class="control">
            <input class="input" type="text" v-model="front_side" />
          </div>
        </div>

        <div class="field">
          <label class="label">Backside</label>
          <div class="control">
            <input class="input" type="text" v-model="back_side" />
          </div>
        </div>

        <div class="field">
          <label class="label">Deck</label>
          <div class="control">
            <select class="select" v-model="selectedDeck">
              <option v-for="deck in decks" :key="deck.id" :value="deck.id">
                {{ deck.name }}
              </option>
            </select>
          </div>
        </div>

        <div class="field">
          <div class="control">
            <button class="button is-link">Submit</button>
          </div>
        </div>
      </form>
    </div>


    <div class="flashcards">
      <div class="card" v-for="flashcard in flashcards" :key="flashcard.id">
        <vue-flashcard
          headerFront=""
          headerBack=""
          :footerFront="String(flashcard.deck.name)"
          :footerBack="String(flashcard.deck.name)"
          :front="flashcard.front_side"
          :back="flashcard.back_side"
        >
        </vue-flashcard>
        <div class="delete-flashcard">
          <button @click="deleteFlashcard(flashcard.id)" class="delete">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vueFlashcard from "vue-flashcard";
export default {
  name: "Flashcards",
  components: { vueFlashcard },
  data() {
    return {
      flashcards: [],
      front_side: "",
      back_side: "",
      selectedDeck: 0,
      decks: [],
    };
  },
  mounted() {
    this.getFlashcards();
    this.getDecks();
  },
  methods: {
    getFlashcards() {
      axios
        .get("http://127.0.0.1:8000/flashcards")
        .then((response) => (this.flashcards = response.data));
    },
    addFlashcard() {
      axios
        .post("http://127.0.0.1:8000/flashcards", {
          front_side: this.front_side,
          back_side: this.back_side,
          deck: this.selectedDeck,
        })
        .then((response) => {
          let newFlashcard = {
            id: response.data.id,
            front_side: this.front_side,
            back_side: this.back_side,
            deck: this.selectedDeck,
          };

          this.flashcards.push(newFlashcard);

          this.front_side = " ";
          this.back_side = " ";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteFlashcard(id) {
      axios
        .delete("http://127.0.0.1:8000/flashcards/"+ id)
        .then((response) =>  {
          console.log(response)
          this.getFlashcards()
        })
      },
    getDecks() {
      axios
        .get("http://127.0.0.1:8000/decks")
        .then((response) => (this.decks = response.data));
    },
  },
};
</script>


<style>
.flashcards {
  display: flex;
  flex-wrap: wrap;
  width: 100%;

}

.card {
  margin: 10px;
  padding: 20px;
  background-color: rgb(177, 253, 209);
  color: #2c3e50;
}
</style>
