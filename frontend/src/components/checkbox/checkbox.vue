<template>
  <v-container fluid>
    <p>{{ selected }}</p>
    <v-checkbox v-model="selected" label="1" value="1"></v-checkbox>
    <v-checkbox v-model="selected" label="2" value="2"></v-checkbox>
    <v-checkbox v-model="selected" label="3" value="3"></v-checkbox>
    <v-checkbox v-model="selected" label="4" value="4"></v-checkbox>
    <v-checkbox v-model="selected" label="5" value="5"></v-checkbox>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
        selected: ['1'],
      }
    },
  }
</script>