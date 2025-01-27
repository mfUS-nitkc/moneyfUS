<template>
  <div class="number-input-wrapper">
    <input
      type="text"
      v-model="inputValue"
      @input="validateNumber"
      class="number-input"
      placeholder="Enter a number"
    />
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "NumberInput",
  data() {
    return {
      inputValue: "",
      errorMessage: "",
    };
  },
  methods: {
    validateNumber() {
      // Check if input is a number
      if (!/^\d*$/.test(this.inputValue)) {
        this.errorMessage = "Only numbers are allowed!";
        this.inputValue = this.inputValue.replace(/\D/g, "");
      } else {
        this.errorMessage = "";
      }
    },
  },
};
</script>

<style>
.number-input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 200px;
  margin: auto;
}

.number-input {
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

.error-message {
  color: red;
  font-size: 12px;
  margin: 0;
}
</style>
