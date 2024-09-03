# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# GROW WITH SAFARICOM BUSINESS COAST EDITION
        
         """)

msgs = [ 'Karibu sana! Welcome to our vibrant business forum, where Kenyan entrepreneurs connect and grow',
         'A heartfelt welcome to all business owners in Kenya. Let's inspire and learn from each other',
         'Step into our forum with a warm welcome! Excited to have Kenyan business minds together',
         'Kenyan business owners, a warm welcome to you! Share your journey, learn from others',
         'Welcome! Your expertise and insights will enrich our Kenyan business forum',
         'A warm welcome to all visionary business owners in Kenya Let's build a stronger community together',
         'Glad to have you with us, Kenyan business owners! Let's collaborate, learn, and succeed',
         'Welcome to a place of shared knowledge and growth Kenyan business owners, let's thrive!',
         'Heartfelt welcome to our Kenyan business forum! Your presence will make a difference',
         'Welcome, Kenyan entrepreneurs! Your energy and ideas will fuel our forum',
         'A warm welcome to all, as we come together to empower Kenyan businesses',
         'Excited to have you join our Kenyan business community! Let's support each other',
         'Welcome to a space of collaboration and growth Kenyan business owners, let's unlock our potential',
         'A warm welcome to our forum! Kenyan business owners, we're excited to learn from you',
         'Welcome, innovators! Your creativity will inspire our Kenyan business forum',
         'Heartfelt welcome to all Kenyan business owners! Let's work together to create success stories',
         'Welcome to a community that values your expertise, Kenyan entrepreneurs',
         'A warm welcome to our Kenyan business forum! Your voice matters here',
         'Welcome, leaders! Your guidance will steer our Kenyan business community to new heights',

      
        
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Welcome to Grow With Safaricom Business. "+msg)
