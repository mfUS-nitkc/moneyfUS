<template>
  <div>
    <FormTextfield v-model="inputText" label="名前を入力してください" />
    <p>入力された値: {{ inputText }}</p>
  </div>
</template>

<script>


export default {
  data() {
    return {
      inputText: "",
    };
  },
};
</script>

