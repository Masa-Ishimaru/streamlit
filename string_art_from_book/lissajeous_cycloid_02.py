import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.write('# Draw Lissajeous curves with cycloids ver2')
st.write('Just select parameters you prefer from the left area. \
         R = radius of large gear, r = radius of small gear, a = hole position in the small gear, \
         p: coefficient of periodicity for x (cosine curve), q: coefficient of periodicity for y (sine curve)\n')
# st.write('時間がある時にスピログラフを描きましょう！左のエリアでパラメータを選ぶだけです。\n')

# preparing variables in radians
x = np.arange(0, 54000, 0.1)
theta = x * (np.pi / 180.0)

colors = ['darkgreen', 'maroon', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    d_type = st.sidebar.selectbox('select your favorite type', ['Hypocycloid', 'Epicycloid'])
    c = st.sidebar.selectbox('select your favorite color', colors)
    
    R = st.sidebar.slider("value of R", 1, 300, 201, key = "one")
    r = st.sidebar.slider("value of r", 1, 200, 151, key = "two")
    a = st.sidebar.slider("value of a", 2, 100, 33, key = "three")
    p = st.sidebar.slider("value of p", 1, 20, 3, key = "four")
    q = st.sidebar.slider("value of q", 1, 20, 2, key = "five")
    
    return d_type, R, r, a, c, p, q

# formula
def hypo_formula(R, r, a, p, q):
    xi = ((R - r) * np.cos((r / R) * theta * p) + a * np.cos(((R - r) / R) * theta))
    yi = ((R - r) * np.sin((r / R) * theta * q) - a * np.sin(((R - r) / R) * theta))

    return xi, yi

def epi_formula(R, r, a, p, q):
    xi = ((R + r) * np.cos((r / R) * theta * p) - a * np.cos(((R + r) / R) * theta))
    yi = ((R + r) * np.sin((r / R) * theta * q) - a * np.sin(((R + r) / R) * theta))

    return xi, yi

def formula(d_type, R, r, a, p, q):
    if d_type == 'Hypocycloid':
        xi, yi = hypo_formula(R, r, a, p, q)
    if d_type == 'Epicycloid':
        xi, yi = epi_formula(R, r, a, p, q)

    return xi, yi

# drawing
def drawing(xi, yi, c):
    fig, ax = plt.subplots(figsize = (8, 8))
    ax.scatter(xi, yi, marker = '.', color = c, s = 0.2, alpha = 0.8)
    ax.axis('off')
    
    return fig

# display graphs
st.sidebar.write('Change parameters')
d_type, R, r, a, c, p, q = fix_params()
xi, yi = formula(d_type, R, r, a, p, q)
fig = drawing(xi, yi, c)
st.pyplot(fig)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose : ', d_type, ' R = ', R, ' r = ', r, ' a = ', a, ' p = ', p, ' q = ', q)


