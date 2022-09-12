<template>
  <div>
    <p>Hello, {{ args.name }}! &nbsp;</p>
    <button @click="onClicked(theme)">Click Me!</button>
  </div>
</template>

<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"

export default {
  name: "TextareaAutosize",
  props: ['args', 'theme', 'disabled'], // Arguments passed from Python
  setup () {
    useStreamlit(); // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const onClicked = (o) => {
      numClicks.value++
      Streamlit.setComponentValue(numClicks.value)
      console.log(o);
    }

    return {
      numClicks,
      onClicked,
    }
  }
}
</script>

<style scoped>
  p { margin-block: 0 20px;}
</style>