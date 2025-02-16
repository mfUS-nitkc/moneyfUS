<template>
  <div class="pa-5">
    <FormTextfield v-model="one" />
    <FormTextfield v-model="two" label="LABEL" />
    <FormTextfield v-model="three" label="REQUIRED" :rules="[(v:any) => v !== '' || 'required!']" />
    <FormTextfield v-model="email" label="Email" :rules="[(v:string) => /.+@.+/.test(v) || 'Invalid Email address' ]"/>
  </div>
</template>

<script lang="ts" setup>
const one = ref('')
const two = ref('')
const three = ref('')
const email = ref('')
</script>