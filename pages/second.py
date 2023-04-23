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

st.markdown("# Page 2 🎉")
st.sidebar.markdown("# Page 2 🎉")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

