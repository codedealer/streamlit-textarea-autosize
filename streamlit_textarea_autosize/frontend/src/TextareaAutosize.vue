<template>
  <div class="textarea-autosize-container" :style="rootStyles" :id="args.key">
    <label
      v-if="args.label"
      :class="args.labelClass"
      class="cd-textarea-label"
    >{{ args.label }}</label>
    <textarea
      @change="onChange"
      @focus="onChange"
      @keydown.enter="onSubmit"
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
import {computed, nextTick, onMounted, ref, watch} from "vue";

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

onMounted(() => {
  textarea.value!.style.height = Number(props.args.minHeight) > 0
                                ? `${Number(props.args.minHeight)}px`
                                : `30px`;
  Streamlit.setFrameHeight()
})

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
const onSubmit = (e: KeyboardEvent) => {
  if (!props.args.submitForm) return true;

  // just add new line on CTRL+ENTER
  if (e.ctrlKey || e.shiftKey) {
    v.value += "\n";
    return true;
  }

  e.preventDefault();
  Streamlit.setComponentValue(v.value);

  // we need to wait a bit for the message to reach streamlit server
  setTimeout(() => {
    // trigger submit of the closest form button
    let rootDoc = null;
    try {
      rootDoc = window.parent.document;
    } catch (e) {
      console.error(e);
      console.error("Couldn't escape the iframe. Automatic submit is impossible");
      return false;
    }

    for (let i = 0, iframes = Array.from(rootDoc.querySelectorAll('iframe'));
         i < iframes.length; i++) {
      const body = iframes[i].contentDocument?.body;
      if (!body) throw new Error("Failed to access the iframe. Automatic submit is impossible");

      const el = body.querySelector(`#${props.args.key}`);
      if (!el) continue;

      const form = iframes[i].closest(`[data-testid="stForm"]`);
      if (!form) throw new Error(`Couldn't find form for ${props.args.key}`);

      const button = form.querySelector('button[kind="formSubmit"]');
      if (!button) throw new Error("Couldn't find a submit button in a form");

      (button as HTMLButtonElement).click();
    }
  }, 500);
}

const resize = () => {
  nextTick(() => {
    textarea.value!.style.height = `auto`;
    const scrollHeight = textarea.value!.scrollHeight;

    if (Number(props.args.minHeight) > 0 && scrollHeight < props.args.minHeight) {
      textarea.value!.style.height = `${Number(props.args.minHeight)}px`;
    } else if (Number(props.args.maxHeight) > 0) {
      if (scrollHeight > Number(props.args.maxHeight)) {
        textarea.value!.style.height = `${Number(props.args.maxHeight)}px`;
        isScrollEnabled.value = true;
      } else {
        isScrollEnabled.value = false;
        textarea.value!.style.height = `${Number(scrollHeight)}px`;
      }
    } else {
      textarea.value!.style.height = `${Number(scrollHeight)}px`;
    }

    Streamlit.setFrameHeight()
  })
}

watch(v, resize)
</script>

<style scoped>
  p { margin-block: 0 20px;}
  .textarea-autosize-container {
    font-family: var(--font);
    box-sizing: border-box;
  }
  .cd-textarea-label {
    display: inline-block;
    margin-bottom: var(--padding);
    font-size: 14px;
  }
  .cd-textarea {
    display: block;
    box-sizing: border-box;
    width: 100%;
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
