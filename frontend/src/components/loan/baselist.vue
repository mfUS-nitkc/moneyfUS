<template>
  <v-container fluid>
    <v-card>
      <v-card-title style="font-size: 1rem;">{{ title }}</v-card-title>
      <v-spacer class="px-5" />
      <v-list class="scrollable-list">
        <v-list-item v-for="item in items" :key="item.id">
          <template v-slot:prepend>
            <v-icon>mdi-star-outline</v-icon>
          </template>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle v-if="item.subtitle">{{ item.subtitle }}</v-list-item-subtitle>
          <template v-slot:append>
            <v-btn color="primary" @click="selectItem(item.id)">選択</v-btn>
          </template>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
interface ListItem {
  id: string;
  title: string;
  subtitle: string
}

const props = defineProps<{ 
  title: string;
  items: ListItem[];
  to?: string;
}>();

const emit = defineEmits<{ (e: "select", id: string): void }>();

const selectItem = (id: string) => {
  emit("select", id);
  if (props.to) useRouter().push(props.to)
};
</script>
<style scoped>
.scrollable-list {
  max-height: calc(100vh - 156px - 128px);
  overflow-y: auto;
}
</style>
