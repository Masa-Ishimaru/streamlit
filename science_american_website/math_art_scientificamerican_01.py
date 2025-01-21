import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write('# Draw math art from the scientific american website')
st.write('Just select parameters you prefer from the left area.\
N: number of circles, a, b: determine the positions of the centers of circles, r: determines radius of circles.\n')
st.write('Source : https://www.scientificamerican.com/blog/guest-blog/making-mathematical-art/')

colors = ['green', 'maroon', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():
    c = st.sidebar.selectbox('select your favorite color', colors)    
    N = st.sidebar.slider("value of N", 1000, 3000, 2500, key = "one")
    a = st.sidebar.slider("value of a", 5, 20, 18, key = "two")
    b = st.sidebar.slider("value of b", 5, 20, 10, key = "three")
    r = st.sidebar.slider("value of r", 30, 60, 52, key = "four")
    
    return c, N, a, b, r

# formula
def draw_math_art(N, a, b, r):
    theta = np.linspace(0, 4*np.pi, 361)

    fig, ax = plt.subplots(figsize = (8, 8))
    for k in range(1, N + 1):
        X = 2 * np.cos(a * np.pi * (k / N)) * (1 - (1/2) * (np.cos(b * np.pi * (k / N)))**2)
        Y = 2 * np.sin(a * np.pi * (k / N)) * (1 - (1/2) * (np.cos(b * np.pi * (k / N)))**2)
        R = (1 / 200) + (1 / 10) * (np.sin(r * np.pi * k / N))**4

        x = R * np.cos(theta) + X
        y = R * np.sin(theta) + Y

        # plt.axis('off')
        plt.plot(x, y, color = c, linewidth = 0.2)
        ax.axis('off')

    st.pyplot(fig)

# display graphs
st.sidebar.write('Change parameters')
c, N, a, b, r = fix_params()
draw_math_art(N, a, b, r)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose : N = ', N, ' a = ', a, ' b = ', b, ' r = ', r)


