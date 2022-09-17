<template>
  <div class="textarea-autosize-container" :style="rootStyles">
    <label
      v-if="args.label"
      :class="args.labelClass"
      class="cd-textarea-label"
    >{{ args.label }}</label>
    <textarea
      @change="onChange"
      @focus="onChange"
      v-model="v"
      :style="styles"
      :rows="args.rows"
      :class="args.textAreaClass"
      class="cd-textarea"
      :placeholder="args.placeholder"
      :disabled="disabled"
      ref="textarea"
      wrap="hard"
    ></textarea>
  </div>
</template>

<script setup lang="ts">
import { Streamlit, Theme } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"
import { computed, nextTick, ref, watch } from "vue";

interface IProps {
  args: any;
  disabled: boolean;
  theme: Theme;
}

useStreamlit(); // lifecycle hooks for automatic Streamlit resize
const props = defineProps<IProps>();

const v = ref('');
v.value = props.args.value as string;
const textarea = ref<HTMLTextAreaElement | null>(null); // html element
const height = Number(props.args.minHeight) > 0
               ? ref(`${Number(props.args.minHeight)}px`)
               : ref(`30px`)
const isScrollEnabled = ref(false);
const paddingValue = 8;

const styles = computed(() => ({
  'overflow-y': `${isScrollEnabled.value ? "scroll" : "hidden"}`,
}))
const rootStyles = computed(() => ({
  '--color': props.theme.primaryColor,
  '--text-color': props.theme.textColor,
  '--background-color': props.theme.base === 'light' ? '#f0f2f6' : '#262730',
  '--secondary-background-color': props.theme.secondaryBackgroundColor,
  '--font': props.theme.font,
  '--padding': `${paddingValue}px`,
}))

const onChange = () => {
  Streamlit.setComponentValue(v.value)
}
const resize = () => {
  nextTick(() => {
    textarea.value!.style.height = `auto`;
    const scrollHeight = textarea.value!.scrollHeight;
    textarea.value!.style.height = `${Number(scrollHeight)}px`;

    if (Number(props.args.minHeight) > 0 && scrollHeight < props.args.minHeight) {
      textarea.value!.style.height = `${Number(props.args.minHeight)}px`;
    } else if (Number(props.args.maxHeight) > 0) {
      if (scrollHeight > Number(props.args.maxHeight)) {
        textarea.value!.style.height = `${Number(props.args.maxHeight)}px`;
        //isScrollEnabled.value = true;
      } else {
        //isScrollEnabled.value = false;
      }
    }

    Streamlit.setFrameHeight()
  })
}

watch(v, resize)
onChange() // init value
</script>

<style scoped>
  p { margin-block: 0 20px;}
  .textarea-autosize-container {
    /*margin: 4px;*/
    font-family: var(--font);
    box-sizing: border-box;
    /*display: flex;*/
    /*flex-direction: column;*/
  }
  .cd-textarea-label {
    /*flex: 0 0 auto;*/
    display: inline-block;
    margin-bottom: var(--padding);
    font-size: 14px;
  }
  .cd-textarea {
    display: block;
    box-sizing: border-box;
    width: 100%;
    /*flex: 1 0 100%;*/
    font-family: var(--font);
    background-color: var(--background-color);
    color: var(--text-color);
    padding: var(--padding);
    border: none;
    border-radius: 4px;
    resize: none;
    font-size: 16px;
    transition: border-color .4s ease;
    border: 1px solid transparent;
    outline: none;
  }
  .cd-textarea:focus,
  .cd-textarea:focus-within {
    outline: none;
    border-color: var(--color);
  }
</style>
