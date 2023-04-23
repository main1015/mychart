#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time: 2023/4/23 2:07 PM
@Author: wangyu
"""

__author__ = "wangyu"
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from itertools import cycle

st.markdown("# Page 2 🎉")
st.sidebar.markdown("# Page 2 🎉")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)



with st.container():

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("this is one")
        st.write("This is inside the container")
    with col2:
        st.header("this is two")
        image = Image.open('static/js.jpg')
        st.image(image)

    with col3:
        st.header("this is three")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

filteredImages = ["js.jpg", "nv1.jpg", "nv2.jpg", "nv3.jpg"]
caption = ["男模", "女星1", "女星2", "女星3"]
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    image = Image.open('static/'+filteredImage)
    img_array = np.array(image)
    st.text(f"{img_array.shape}")
    new_shape = (150, 210, 3)
    img = np.array(Image.fromarray(img_array).resize(new_shape[:2]))
    next(cols).image(img, width=150, caption=caption[idx])
