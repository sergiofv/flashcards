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
        <br>
        <div class="field">
          <label class="label">Backside</label>
          <div class="control">
            <input class="input" type="text" v-model="back_side" />
          </div>
        </div>
        <br>
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
        <br>       
        <div class="field">
          <div class="control">
            <button class="button is-link">Add</button>
          </div>
        </div>
      </form>
    </div>

    <div class="flashcards">
      <div
        class="card"
        v-for="(flashcard, index) in flashcards"
        :key="flashcard.id"
      >
        <vue-flashcard
          headerFront=""
          headerBack=""
          :footerFront="String(flashcard.deck_name)"
          :footerBack="String(flashcard.deck_name)"
          :front="flashcard.front_side"
          :back="flashcard.back_side"
        >
        </vue-flashcard>
        <div class="delete-flashcard">
          <button v-on:click="cardToEdit = cardToEdit === index ? -1 : index">
            Edit
          </button>
          &nbsp; &nbsp;
          <button @click="deleteFlashcard(flashcard.id)" class="delete">
            Delete
          </button>
        </div>

        <form
          @submit.prevent="editFlashcard(flashcard.id)"
          v-if="cardToEdit === index"
        >
          <br />
          <br />
          <div class="field">
            <label class="label">Edit frontside</label>
            <div class="control">
              <input class="input" type="text" v-model="new_front_side" />
            </div>
          </div>

          <div class="field">
            <label class="label">Edit backside</label>
            <div class="control">
              <input class="input" type="text" v-model="new_back_side" />
            </div>
          </div>

          <div class="field">
            <label class="label">Edit deck</label>
            <div class="control">
              <select class="select" v-model="newSelectedDeck">
                <option v-for="deck in decks" :key="deck.id" :value="deck.id">
                  {{ deck.name }}
                </option>
              </select>
            </div>
          </div>
          <br />
          <div class="field">
            <div class="control">
              <button type="submit" class="button is-link">Update</button>
            </div>
          </div>
        </form>
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
      newSelectedDeck: -1,
      decks: [],
      cardToEdit: -1,
      new_back_side: "",
      new_front_side: "",

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

          this.getFlashcards(); 
        })
        .catch((error) => {
          console.log(error);
        });
    },

    editFlashcard(id) {
      axios
        .put("http://127.0.0.1:8000/flashcards/" + id, {
          front_side: this.new_front_side,
          back_side: this.new_back_side,
          deck: this.newSelectedDeck,
        })
        .then(this.getFlashcards);
    },

    deleteFlashcard(id) {
      axios
        .delete("http://127.0.0.1:8000/flashcards/" + id)
        .then(this.getFlashcards);
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
  height: fit-content;
}


</style>
