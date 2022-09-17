import streamlit as st
import streamlit.components.v1 as components

import os

_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        "textarea_autosize",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "textarea_autosize", path=build_dir)


def textarea_autosize(
        label="",
        value="",
        key=None,
        max_height=None,
        min_height=None,
        rows="1",
        text_area_class="",
        label_class="",
        placeholder="",
        submit_form=False
):
    component_value = _component_func(
        label=label,
        value=value,
        key=key,
        maxHeight=max_height,
        minHeight=min_height,
        rows=rows,
        textAreaClass=text_area_class,
        labelClass=label_class,
        placeholder=placeholder,
        submitForm=submit_form if key is not None else False
    )
    return component_value

# Keep in mind that form submition won't work in development mode
# because of different origins between streamlit backend and nodejs frontend
if not _RELEASE:
    value1 = textarea_autosize("Simple autosize input", "", key="simple_textarea")
    st.write(value1)

    with st.form("text-form"):
        content = textarea_autosize(
            "Input inside a form",
            "",
            key="textarea",
            text_area_class="",
            placeholder="Type here",
            max_height=80,
            min_height=38,
            submit_form=True
        )

        text1 = st.text_area("Form input", "")
        st.write(f"Form: {content}")
        st.write(f"Form: {text1}")

        generate_button = st.form_submit_button("Generate")
