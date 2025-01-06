<template>
    <v-text-field
      :label="label"
      v-model="inputValue"
    ></v-text-field>
  </template>
  
  <script>
  export default {
    props: {
      label: {
        type: String,
        required: true,
      },
      modelValue: {
        type: String,
        required: false,
        default: "",
      },
    },
    computed: {
      inputValue: {
        get() {
          return this.modelValue;
        },
        set(value) {
          this.$emit("update:modelValue", value);
        },
      },
    },
  };
  </script>
  