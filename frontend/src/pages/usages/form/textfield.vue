<template>
  <div class="pa-5">
    <FormTextfield :value="one" @update:value="updateValueOne"/>
    <FormTextfield :value="two" label="LABEL" @update:value="updateValueTwo" />
    <FormTextfield :value="three" label="REQUIRED" :rules="[(v:any) => v !== '' || 'required!']" @update:value="updateValueThree" />
    <FormTextfield :value="email" label="Email" :rules="[(v:string) => /.+@.+/.test(v) || 'Invalid Email address' ]" @update:value="updateValueEmail" />
  </div>
</template>

<script lang="ts" setup>
const one = ref('')
const two = ref('')
const three = ref('')
const email = ref('')

const updateValueOne = (value: string | number) => {
  one.value = value
}

const updateValueTwo = (value: string | number) => {
  two.value = value
}

const updateValueThree = (value: string | number) => {
  three.value = value
}

const updateValueEmail = (value: string) => {
  email.value = value
}
</script>