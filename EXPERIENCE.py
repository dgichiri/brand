# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random


st.write("""
 
# GROW WITH SAFARICOM BUSINESS - MT KENYA EDITION. 
        
         """)

msgs = [ "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The only way to do great work is to love what you do.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't be afraid to give up the good to go for the great.",
    "I find that the harder I work, the more luck I seem to have.",
    "Success is not in what you have, but who you are.",
    "The road to success and the road to failure are almost exactly the same.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Success is not the absence of failure; it's the persistence through failure.",
    "The only limit to our realization of tomorrow is our doubts of today.",


                     
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Karibu. "+msg)
