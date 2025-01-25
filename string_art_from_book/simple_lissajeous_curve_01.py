import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write('# Simple Lissageous curves')
st.write('Just select parameters you prefer from the left area.\
         p: coefficient of periodicity for x (cosine curve), \
         q: coefficient of periodicity for y (sine curve)')
st.write('Source: アートで魅せる数学の世界 技術評論社 2021\n')

colors = ['maroon', 'green', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    c = st.sidebar.selectbox('select your favorite color', colors)    
    p = st.sidebar.slider("value of p", 1, 50, 3, key = "one")
    q = st.sidebar.slider("value of q", 1, 50, 2, key = "two")
    
    return c, p, q

# formula
def formula(p, q, theta):
    xl = np.cos(p * theta)
    yl = np.sin(q * theta)

    return xl, yl

# drawing
def drawing(p, q, c):
    x = np.arange(0, 1800, 0.005)
    theta = x * (np.pi / 180.0)

    xl, yl = formula(p, q, theta)
    fig, ax = plt.subplots(figsize = (8, 8))
    plt.scatter(xl, yl, color = c, marker = '.', s = 0.05, alpha = 0.8)
    ax.axis('off')
    
    st.pyplot(fig)

# display graphs
st.sidebar.write('Change parameters')
c, a, b = fix_params()
fig = drawing(a, b, c)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose :    a = ', a, ' b = ', b)


