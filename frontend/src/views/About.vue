<template>
  <div class="about">
    <h1>DECKS</h1>
    <div>
      <form v-on:submit.prevent="addDeck">
        <h3 class="subtitle">Add new deck</h3>

        <div class="field">
          <label class="label">Deck name</label>
          <div class="control">
            <input class="input" type="text" v-model="name" />
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

    <div class="decks">
      <div class="deck" v-for="deck in decks" :key="deck.id">{{deck.name}}
        <div class="delete-decks">
            <br>
            <button @click="deleteDecks(deck.id)" class="delete">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";
export default {
  name: "Decks",
  data() {
    return {
      decks: [],
      name: " ",
    };
  },
  mounted() {
    this.getDecks();
  },
  methods: {
    getDecks() {
      axios
        .get("http://127.0.0.1:8000/decks")
        .then((response) => (this.decks = response.data));
    },
    addDeck() {
      axios.post("http://127.0.0.1:8000/decks", { name: this.name })
        .then((response) => {
          let newDeck = {
            id: response.data.id,
            name: this.name,
          };

          this.decks.push(newDeck);

          this.name = " ";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteDecks(id) {
      axios
        .delete("http://127.0.0.1:8000/decks/"+ id)
        .then((response) =>  {
          console.log(response)
          this.getDecks()
        })
    },
  },
};
</script>


<style>
.decks {
  display: flex;
}

.deck {
  margin: 10px;
  padding: 20px;
  background-color: rgb(211, 136, 198);
  color: #2c3e50;
}
</style>
