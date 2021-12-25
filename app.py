import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import easyocr
from PIL import ImageDraw

try:
    st.title('Extract text from PDF')
    path = st.text_input('Specify the path to PDF')
    page_no = st.number_input('Specify the page number', min_value=1, step=1)

    images = convert_from_path(path)

    reader = easyocr.Reader(['en'])
    page_index = int(page_no)-1
    output = reader.readtext(np.array(images[page_index]))

    def draw_boxes(image):
        draw = ImageDraw.Draw(image)
        for bound in output:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0,*p1,*p2,*p3,*p0], fill='red', width=2)
        return image
    st.image(draw_boxes(images[page_index]))
except:
    pass


if st.button('Extract the texts'):
    try:
        final = [text[-2] for text in output]
        st.write(final)
    except:
        st.error('Please make sure that you enter valid inputs.')



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            footer:after {
	            content:'Made by Nilavo Boral'; 
	            visibility: visible;
	            display: block;
	            position: relative;
	            #background-color: red;
	            padding: 5px;
	            top: 2px;
                color: tomato;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)