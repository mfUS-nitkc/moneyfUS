<template>
  <v-btn
    :class="btnClass"
    elevation="0"
    width="100%"
    height="100%"
    tile
    slim
    block
    :to="link"
    nuxt
  >
    <v-row>
      <v-col class="text-center pa-0">
        <v-icon class="icon" size="calc(2rem + ((1vw - 0.01px) * 1.6283))">{{
          icon
        }}</v-icon>
        <div class="text"><slot /></div>
      </v-col>
    </v-row>
  </v-btn>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: {
    type: String,
    required: true,
  },
  link: {
    type: String,
  },
});

const btnClass = computed(() => {
  const classNameAry = ["btn"];
  console.log(props.link)
  if (props.link === useRoute().fullPath) {
    classNameAry.push("selected");
  }
  return classNameAry.join(" ");
});

const emit = defineEmits<{
  click: [undefined];
}>();
</script>

<style scoped>
.btn {
  background-color: #d9d9d9;
  justify-content: center;
  align-items: center;
  aspect-ratio: 1;
  width: 100%;
}

.selected {
  background-color: #7899b1 !important;
}

.icon {
  color: black; /* Black icon color */
}

.text {
  font-size: calc(0.375rem + ((1vw - 0.01px) * 3.1283));
  color: #fff; /* Black text color */
  -webkit-text-stroke: 1px black;
  text-stroke: 1px black;
  line-height: 1.875;
  paint-order: stroke fill;
  letter-spacing: 0px;
  font-weight: 900;
}
</style>
