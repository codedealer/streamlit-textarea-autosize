<template>
  <WithStreamlitConnection v-slot="{ args, theme, disabled }">
    <TextareaAutosize :args="args" :theme="theme" :disabled="disabled" />
  </WithStreamlitConnection>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TextareaAutosize from './TextareaAutosize.vue'
import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: 'App',
  components: {
    TextareaAutosize,
    WithStreamlitConnection,
  },
})
</script>

<style>
body, html {
  margin: 0;
}
</style>
