# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random


st.write("""
 
# SAFARICOM INVESTOR FORUM 2025. 
        
         """)

msgs = [ "Welcome to Mombasa, the vibrant coastal gem of Kenya, where the Indian Ocean meets rich history, culture, and endless possibilities. Over the next two days, we gather not just in the heart of this iconic city but at the crossroads of innovation, collaboration, and purpose. As you explore Mombasa, you’ll encounter its timeless monuments—the majestic Fort Jesus, a testament to resilience and transformation, and the enchanting Old Town, where centuries of trade and connection have shaped a thriving community. These landmarks remind us of the power of vision, perseverance, and the ability to adapt while staying rooted in purpose."

"This forum is more than a meeting; it is a call to connect, engage, and inspire. Together, we will delve into the bold vision of becoming Africa’s leading purpose-driven technology company by 2030. We are not just building a business; we are creating a legacy that empowers communities, drives sustainable growth, and harnesses technology as a force for good. Your presence here signifies a shared belief in this vision. Over the next two days, let us challenge assumptions, spark innovation, and forge partnerships that will redefine what is possible. Let us draw inspiration from Mombasa’s rich history and use it to fuel our journey toward a future where technology serves humanity and Africa leads the way."

"Thank you for joining us. Let’s make these two days transformative."


                     
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Karibu. "+msg)
