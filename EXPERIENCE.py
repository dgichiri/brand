# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random


st.write("""
 
# THE CA DREAM TEAM 
        
         """)

msgs = [ "Hey there, top cat! Hoping your day is as groovy as a roller disco. ",
         "Greetings, retro rockstar! Ready to make the most of today? ",
         "Morning, my rad friend! Let's seize the day like it's 1982. ",
         "Hi there, cool customer! The 80s called, they're proud of your style. ",
         "Hello, decade darling! Fired up for a far-out day? ",
         "Aloha, 80s aficionado! May your day be as bright as neon lights. ",
         "Bonjour, retro enthusiast! Ready to make today a total blast? ",
         "Howdy, 80s fan! Here's to a day as cool as a polaroid picture. ",
         "Hey, time traveler! Let's make the 80s proud today. ",
         "Hi, retro guru! May your day be as legendary as the 80s. ",
         "Greetings, 80s guru! Ready to rock this day like a power ballad? ",
         "Hello, 80s devotee! Let's make today as memorable as a mixtape. ",
         "Hey, 80s champion! Here's to a day as epic as a blockbuster movie. ",
         "Hi there, 80s legend! May your day be as vibrant as a Rubik's cube. ",
         "Aloha, 80s maverick! Ready to navigate today like a compass? ",
         "Bonjour, 80s trendsetter! May your day be as bright as a sunset cruise. ",
         "Howdy, 80s hero! Here's to a day as bold as a synth-pop beat. ",
         "Hey, 80s whiz! Let's make today as exciting as a video game. ",
         "Hi, 80s ace! May your day be as thrilling as a high-speed chase. ",
         "Greetings, 80s star! Here's to a day as dazzling as a music video. ",

                     
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,CAribu 1. "+msg)
