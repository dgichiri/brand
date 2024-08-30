# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to CEO's Appreciation Luncheon
        
         """)

msgs = ['Your tech insights are like hidden gems in the digital finance landscape.',
        'Your determination in tackling tech challenges is truly inspiring',
        'Your dedication to excellence is like a heavenly virtue, infusing our projects with the essence of success and achievement',
        'Your tech skills are like the backbone of our digital infrastructure, providing stability and reliability in an ever-changing landscape',
        'You demonstrates a high level of creativity in developing innovative brand communication strategies',
        'Your tech insights are like guiding stars in the digital universe, illuminating paths to innovation and progress. Keep shining bright and leading the way',
        'Your determination in the face of technical challenges is like a force of nature. Your resilience and tenacity propel us forward, overcoming obstacles and achieving greatness.',
        'Your tech expertise is like a cornerstone, providing stability and strength to our digital endeavors. Keep building and fortifying our technological foundations!',
        'Your tech insights are like a guiding light, illuminating the path to innovation and progress.',
        'Your strategic thinking and problem-solving abilities are invaluable assets to our team. Keep shining bright!',
        'Looking gorgeous as ever! loving the outfit also, we see the glow.',
        'Your bubbly yet grounded approach to everything is a breath of fresh air in this tech space. You are doing well, keep up!',
        'Your warmth and appreciation for people radiates all through',
         'Your skills are like the backbone of our digital infrastructure, providing stability and reliability in an ever-changing landscape. Keep building and fortifying our digital foundation! Keep on Shining ',
'Your tech insighats are like hidden gems in the digital finance landscape – profound, impactful, and always ahead of the curve. We appreciate you! Keep on Shining',
'Like Amelia Earhart's courage in the face of the unknown, your determination in tackling challenges is truly inspiring, keep blazing trails, Keep on Shining.',
'Your dedication to excellence is like a heavenly virtue, infusing our Brand Experiences with the essence of success and achievement! Keep on Shining! ',
'Your tech insights are like hidden gems in the digital finance landscape – profound, impactful, and always ahead of the curve. We appreciate you! Keep on Shining',
'Your tech skills are like the backbone of our digital infrastructure, providing stability and reliability in an ever-changing landscape. Keep building and fortifying our digital foundation’.,
'You demonstrate a high level of creativity in developing innovative brand communication strategies. you have a knack for thinking outside the box, crafting compelling narratives while effectively conveying the brand's message and values.',
'Your digital prowess and keen eye are valuable to the team. Keep it up. Keep on Shining',
'In the realm of technology, you're the architect of innovation. Keep on Shining',
'Your insights are like guiding stars in the digital universe, illuminating paths to innovation and progress. Keep shining bright and leading the way!'',
'Your determination in the face of technical challenges is like a force of nature. Your resilience and tenacity propel us forward, overcoming obstacles and achieving greatness. Keep blazing trails!'',
'In the realm of technology, you're the architect of innovation. Your expertise builds bridges between ideas and reality, propelling us towards a future defined by creativity and progress. Keep on Shining',
Your tech expertise is like a cornerstone, providing stability and strength to our digital endeavours. Keep building and fortifying our technological foundations! Shine On !!',
Your tech insights are like a guiding light, illuminating the path to innovation and progress. Your strategic thinking and problem-solving abilities are invaluable assets to our team. Keep shining bright!'',
'Your bubbly yet grounded approach to everything is a breath of fresh air in this tech space. You are doing well, keep up!',
'Your warmth and appreciation for people radiates all through. Your ambition and get it done attitude gives a pathway to excellence and is what is needed in this fast-paced tech and digital landscape. Keep it up!',
'Tech shaper, digital extraordinaire. You are a natural and have a bright future ahead of you. Keep on keeping on! Shine On ',
'You embody a harmonious approach to issues fostering understanding and connection through cohesive narratives that resonate with audiences. Keep building and inspiring!',
'Conquer new heights and rock on! Your wit shines brighter than the summit',
'Ever gentle and warm as you navigate complexities in the financial landscape. Continue illuminating pathways to success for the team! Keep on Shining ',
'Meticulous attention to detail, this enables you to effectively analyze large datasets and identify meaningful insights. Thankyou for making this happen! Keep on shining girl! ',
'Your prowess is like manna from heaven, Keep doing you and bringing miracles into reality! Keep on shining',
'Your writing skills are like a master painter's brush, bringing vibrant ideas to life. Keep creating wonders and inspiring us with your artistry! Shine On ',
'Your expertise shines brightly, guiding us through the complexities of the digital world with clarity and foresight. Keep leading us forward with your brilliance! Keep on shining',
'Your radiant ideas and energy are valuable to the team and will definitely take us to the next level. Keep on shining',
'Your tech prowess is like a powerful engine driving us towards innovation and progress. Keep fuelling our journey with your expertise and creativity! Shine on!',
'Your strategic thinking and innovative ideas are invaluable to our team. Keep guiding us towards new horizons! Keep on shining! ',
       
        
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" ,Welcome to CEO's Appreciation Luncheon. "+msg)
