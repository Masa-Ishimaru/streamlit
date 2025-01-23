import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write('# String art from spirals')
st.write('Just select parameters you prefer from the left area.\
          M: number of divisions to connect, N: pin distance (space) to skip\n')
st.write('Source: アートで魅せる数学の世界 技術評論社 2021\n')

colors = ['black', 'maroon', 'green', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    d_type = st.sidebar.selectbox('select your favorite type', ["Archimedes's spiral", "Bernoulli's spiral", "Fermat's spiral"])
    c = st.sidebar.selectbox('select your favorite color', colors)        
    M = st.sidebar.slider("value of M", 1, 1000, 814, key = "one")
    N = st.sidebar.slider("value of N", 1, 500, 233, key = "two")
    
    return d_type, c, M, N

# formula
def arc_formula(i, theta):
    xi = i * np.cos(theta)
    yi = i * np.sin(theta)
    return xi, yi

def ber_formula(i, theta):
    xi = np.exp(0.01 * i) * np.cos(theta)
    yi = np.exp(0.01 * i) * np.sin(theta)
    return xi, yi

def fer_formula(i, theta):
    xi = np.sqrt(i) * np.cos(theta)
    yi = np.sqrt(i) * np.sin(theta)
    return xi, yi

def formula(d_type, i, theta):
    if d_type == "Archimedes's spiral":
        xi, yi = arc_formula(i, theta)
    if d_type == "Bernoulli's spiral":
        xi, yi = ber_formula(i, theta)
    if d_type == "Fermat's spiral":
        xi, yi = fer_formula(i, theta)
    return xi, yi

# drawing
def drawing(d_type, M, N, c):
    thead_num = 1000
    x = np.arange(0, thead_num + 1, 1)
    theta = (x * 2 * np.pi * N/M)

    fig, ax = plt.subplots(figsize = (8, 8))
    for i in range(thead_num):
        x1, y1 = formula(d_type, i, theta[i])
        x2, y2 = formula(d_type, i, theta[i + 1])

        plt.plot([x1, x2], [y1, y2], color = c, linewidth = 0.2, alpha = 0.8)
        ax.axis('off')
    
    st.pyplot(fig)

# display graphs
st.sidebar.write('Change parameters')
d_type, c, M, N = fix_params()
fig = drawing(d_type, M, N, c)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose : ', d_type, ' M = ', M, ' N = ', N)
