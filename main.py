#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time: 2023/4/23 11:11 AM
@Author: wangyu
"""

__author__ = "wangyu"
import streamlit as st
# from loguru import logger
#
#
# @logger.catch
# def div(a, b):
#     c = a / b
#     return c
#
#
# if __name__ == '__main__':
#     div(2, 0)
import streamlit as st
with st.echo():
    st.title('我的Streamlit')

    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

    st.markdown("[![Click me](app/static/js.jpg)](https://www.baidu.com)")
    st.markdown("[![Click me]](https://www.baidu.com)")

