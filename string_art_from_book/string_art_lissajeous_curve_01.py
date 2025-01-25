import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write('# String art with Lissageous curves')
st.write('Just select parameters you prefer from the left area.\
         p: periodicity for x (cosine curve), q: periodicity for y (sine curve) \
         M: number of divisions to connect, N: pin distance (space) to skip\n')
st.write('Source: アートで魅せる数学の世界 技術評論社 2021\n')

colors = ['maroon', 'green', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    c = st.sidebar.selectbox('select your favorite color', colors)    
    p = st.sidebar.slider("value of p", 1, 10, 1, key = "one")
    q = st.sidebar.slider("value of q", 1, 10, 2, key = "two")
    M = st.sidebar.slider("value of M", 500, 2000, 951, key = "three")
    N = st.sidebar.slider("value of N", 2, 500, 250, key = "four")
    
    return c, p, q, M, N

# formula
def formula(p, q, theta):
    xl = np.cos(p * theta)
    yl = np.sin(q * theta)

    return xl, yl

# drawing
def drawing(p, q, M, N, c):
    x = np.arange(0, M + 1, 1)
    theta = (x * 2 * np.pi * N / M)

    fig, ax = plt.subplots(figsize = (8, 8))
    for i in range(M):
        x1, y1 = formula(p, q, theta[i])
        x2, y2 = formula(p, q, theta[i + 1])

        plt.plot([x1, x2], [y1, y2], color = c, linewidth = 0.3, alpha = 0.8)
        ax.axis('off')
    
    st.pyplot(fig)

# display graphs
st.sidebar.write('Change parameters')
c, p, q, M, N = fix_params()
fig = drawing(p, q, M, N, c)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose :    p = ', p, ' q = ', q, ' M = ', M, ' N = ', N)
