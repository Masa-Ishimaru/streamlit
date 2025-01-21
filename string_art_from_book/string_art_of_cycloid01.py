import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write('# String art of cycloids')
st.write('Just select parameters you prefer from the left area.\
         R: radius of large circle, r: radius of small circle, \
         M: number of threads, N: pin distance (space) to skip\n')
st.write('Source: アートで魅せる数学の世界 技術評論社 2021\n')

# preparing variables in radians
x = np.arange(0, 90000, 0.2)
theta = x * (np.pi / 180.0)

colors = ['maroon', 'green', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    d_type = st.sidebar.selectbox('select your favorite type', ['Epicycloid', 'Hypocycloid'])
    c = st.sidebar.selectbox('select your favorite color', colors)    
    
    M = st.sidebar.slider("value of M", 200, 1000, 500, key = "one")
    N = st.sidebar.slider("value of N", 200, 800, 307, key = "two")
    R = st.sidebar.slider("value of R", 1, 20, 7, key = "three")
    r = st.sidebar.slider("value of r", 1, 20, 1, key = "four")
    
    return d_type, c, M, N, R, r

# formula
def hypo_formula(R, r, theta):
    xi = ((R - r) * np.cos(theta) + r * np.cos(((R - r) / r) * theta))
    yi = ((R - r) * np.sin(theta) - r * np.sin(((R - r) / r) * theta))

    return xi, yi

def epi_formula(R, r, theta):
    xi = ((R + r) * np.cos(theta) - r * np.cos(((R + r) / r) * theta))
    yi = ((R + r) * np.sin(theta) - r * np.sin(((R + r) / r) * theta))

    return xi, yi

def formula(d_type, R, r, theta):
    if d_type == 'Hypocycloid':
        xi, yi = hypo_formula(R, r, theta)
    if d_type == 'Epicycloid':
        xi, yi = epi_formula(R, r, theta)

    return xi, yi

# drawing
def drawing(M, N, R, r, c):
    x = np.arange(0, M + 1, 1)
    theta = (x * 2 * np.pi * N/M)

    fig, ax = plt.subplots(figsize = (8, 8))
    for i in range(M):
        x1, y1 = formula(d_type, R, r, theta[i])
        x2, y2 = formula(d_type, R, r, theta[i + 1])

        plt.plot([x1, x2], [y1, y2], color = c, linewidth = 0.1, alpha = 0.8)
        ax.axis('off')
    
    st.pyplot(fig)

# display graphs
st.sidebar.write('Change parameters')
d_type, c, M, N, R, r = fix_params()
spg_xi, spg_yi = formula(d_type, R, r, theta)
fig = drawing(M, N, R, r, c)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose : ', d_type, ' M = ', M, ' N = ', N, ' R = ', R, ' r = ', r)


