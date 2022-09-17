import setuptools

setuptools.setup(
    name="streamlit_textarea_autosize",
    version="1.0.3",
    author="Thomas Mello",
    author_email="",
    description="Streamlit text input that resizes automatically",
    long_description="Streamlit text input that resizes automatically",
    long_description_content_type="text/plain",
    url="https://github.com/codedealer/streamlit-textarea-autosize",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 1.0",
    ],
)
