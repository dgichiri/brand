# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# SOUL PICNIC WELCOMES YOU
        
         """)

msgs = [ 'Hey there, top cat! Hoping your day is as groovy as a roller disco',
          'Greetings, retro rockstar! Ready to make the most of today?',
          'Morning, my rad friend! Let's seize the day like it's 1982.',
                     
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Welcome to Soul Picnic Edition 1. "+msg)
