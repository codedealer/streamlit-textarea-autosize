# Textarea with automatic resize for Streamlit

[Check out Streamlit here](https://streamlit.io/)

This component behaves like a simple text_input but automatically resizes when new lines are added.

Additionally it can support **submit in forms** although the use of this feature is discouraged because it goes against Streamlit design paradigm.

## Setup


Currently there is no pip package so install directly from this repo:

```
$ pip install git+https://github.com/codedealer/streamlit-textarea-autosize.git#egg=streamlit_textarea_autosize
```

## Usage

The simple usage is similar to the vanilla component:
```
from streamlit_textarea_autosize import textarea_autosize

value = textarea_autosize("Simple autosize input", "")
```

Full list of arguments:
```
label="",
value="",
key=None,
max_height=None, # integer
min_height=None, # integer
rows="1",
text_area_class="",
label_class="",
placeholder="",
submit_form=False
```

### Styling

The component tries to mimic the default style of Streamlit inputs respecting light/dark themes but you can extend it by providing classes for the label and the textarea: `label_class`, `text_area_class`.

### Form submission

You can include this component inside a form and set `submit_form=True`. The behavior of the textarea will change: it will add a new line on CTRL+ENTER and submit the form on ENTER just as if you clicked submit button. This behavior is achieved by a hack escaping iframe and is **not guaranteed** to work. 
