import streamlit as st
import streamlit.components.v1 as components

import os

_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        "st_textarea_autosize",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "st_textarea_autosize", path=build_dir)


def st_textarea_autosize(
        label="",
        value="",
        key=None,
        max_height=None,
        min_height=None,
        rows="1",
        text_area_class="",
        label_class="",
        placeholder=""
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
        placeholder=placeholder
    )
    return component_value


if not _RELEASE:
    content = st_textarea_autosize(
        "Input text",
        "",
        key="textarea",
        text_area_class="",
        placeholder="Type here",
        max_height=80,
        min_height=38
    )
    st.write(content)
