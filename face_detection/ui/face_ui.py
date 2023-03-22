# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:30:13 2023

@author: AYOBAMI SHOYEMI
"""

import streamlit as st
import cv2
from face_app import detect_faces, face_cascade, cap

def main():
    
    st.title('face Detection App')
    
    detect_faces()
    
    
if __name__ == '__main__':
    main()