import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.write('# Draw spirograph')
st.write('Draw spirograph for your fun! Just select parameters you prefer from the left area.\n')
# st.write('時間がある時にスピログラフを描きましょう！左のエリアでパラメータを選ぶだけです。\n')

img = Image.open('hypo_and_epi_cycloids.png')
st.image(img)

# preparing variables in radians
x = np.arange(0, 90000, 0.2)
theta = x * (np.pi / 180.0)

colors = ['maroon', 'green', 'black', 'blue', 'red', 'gray']

# preparing parameters
def fix_params():

    d_type = st.sidebar.selectbox('select your favorite type', ['Hypocycloid', 'Epicycloid'])
    c = st.sidebar.selectbox('select your favorite color', colors)
    
    R = st.sidebar.slider("value of R", 24, 84, 50, key = "one")
    r = st.sidebar.slider("value of r", 24, 84, 40, key = "two")
    a = st.sidebar.slider("value of a", 2, 30, 10, key = "three")
    
    return d_type, R, r, a, c

# formula
def hypo_formula(R, r, a):
    spg_xi = ((R - r) * np.cos((r / R) * theta) + a * np.cos(((R - r) / R) * theta))
    spg_yi = ((R - r) * np.sin((r / R) * theta) - a * np.sin(((R - r) / R) * theta))

    return spg_xi, spg_yi

def epi_formula(R, r, a):
    spg_xi = ((R + r) * np.cos((r / R) * theta) - a * np.cos(((R + r) / R) * theta))
    spg_yi = ((R + r) * np.sin((r / R) * theta) - a * np.sin(((R + r) / R) * theta))

    return spg_xi, spg_yi

def formula(d_type, R, r, a):
    if d_type == 'Hypocycloid':
        spg_xi, spg_yi = hypo_formula(R, r, a)
    if d_type == 'Epicycloid':
        spg_xi, spg_yi = epi_formula(R, r, a)

    return spg_xi, spg_yi

# drawing
def drawing(spg_xi, spg_yi, c):
    fig, ax = plt.subplots(figsize = (8, 8))
    plt.axis('off')
    ax.scatter(spg_xi, spg_yi, marker = '.', color = c, s = 0.1, alpha = 0.7)
    ax.axis('off')
    
    return fig

# display graphs
st.sidebar.write('Change parameters')
d_type, R, r, a, c = fix_params()
spg_xi, spg_yi = formula(d_type, R, r, a)
fig = drawing(spg_xi, spg_yi, c)
st.pyplot(fig)

if st.sidebar.button('Finalized ? if yes, press this button'):
    st.write('You chose : ', d_type, ' R = ', R, ' r = ', r, ' a = ', a)


