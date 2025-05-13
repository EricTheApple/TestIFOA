import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from numpy.random import rand
import plotly.express as px
from numpy.random import rand
from PIL import Image


##MATERIALE PROF
st.title('MIE PROVE E APPUNTI')

st.text("Ciao")

# # # #title
st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')


st.markdown('*Buongiorno*') #corsivo = *
st.markdown('***Buongiorno***') #grassetto = ***



#Button
if st.button("Streamlit Button", help="Clic here"):
    st.write("Hai cliccato")

#CheckBox
if st.checkbox('CheckBox'):
    st.write ('hai checkkato')

st.write ("calcoliamo l'area di un rettangolo")
lato1 = st.slider(label = "lato 1", min_value=0, max_value=50, step = 5)
lato2 = st.slider(label = "lato 2", min_value=0, max_value=50, step = 5)

Area = lato1 * lato2
Perimetro = (lato1+lato2)*2
st.write(f"Area = {Area}")
st.write(f"Perimetro = {Perimetro}")

# immagine = Image.open("C:\Users\Eric\Downloads\meme.png")
# st.image(immagine)
response = requests.get(url="https://akm-img-a-in.tosshub.com/indiatoday/images/story/202106/cover4_new_1200x768.jpeg?size=1200:675")
i = Image.open(BytesIO(response.content))
st.image(i)

fig = plt.figure(figsize=(5,5))
plt.axis([-10,50,-10,50])
x = [0,lato1,lato1,0,0]
y = [0,0,lato2,lato2,0]
plt.plot(x,y)
st.pyplot(fig)


##MATERIALE PROF
st.title('MATERIALE PROF')

st.text("""
        bye 
        bye 
        ciao
        """)

st.text("""bye """)




# # # # # ###################################################
# # markdown
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("### This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^3+y^2}=1$] is a Pythagorean identity. :pencil:")

# # # # # ###################################################
# # # #title
st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')

# # # # # ###################################################
# # #header
st.header('This is a header')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

# # # # # ###################################################
# #subheader
st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

# # # # # ###################################################
# # # #caption
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# # # # # ###################################################
# #code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# # # # # ###################################################
# # #latex
st.latex(r'''
    a + ar + a r^7 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# # # # #######################################################

st.title('La mia prima App in python')

# # # # # #####################################################
# # # # ### the one

#image = Image.open('memeindiano.jpg')
#st.image(image, caption='I am a indian bold guy!!!',width=400)

# # # # # ######################################################

# # # button
if st.button('bottone', help="Clickka qui"):
    st.write('Hai cliccato')

 
# # # check box
if st.checkbox('Check Box'):
    st.write('checckata')
 
# # radio button
lang = st.radio("What's your favorite programming language?",
    ('C++', 'Python','Java'))
if lang == 'C++':
    st.write('You selected C++.')
elif lang == 'Java':
    st.write('You selected Java')
else:
    st.write('You selected Python')
 
# # # slider
x1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 45)
x2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 35)

def area(l1:float,l2:float):
    a = l1*l2
    return a 

st.write("l'area rettangolo è ", area(x1,x2))
 
# # # Using object notation
add_selectbox = st.sidebar.radio(
    "Please choose an option",
    ("Option 1", "Option 2", "Option 3")
)

# # # # # ##################################################
# # # # ############## Plot ############################

fig = plt.figure(figsize=(18,10)) 
plt.scatter([1,2,3,4,5],[1,2,3,4,5])
st.pyplot(fig)

# # # # ####################

rn = st.slider('Please inserisci il numero dei punti da visualizzare', 0, 100, 88)
x = rand(rn)
y = rand(rn)
fig2 = plt.figure(figsize=(18,10)) 
plt.plot(x,y,'or')
st.pyplot(fig2)

# # # # #####################################################

input1 = 'customerID'
input2 = st.text_input("Please write gender",'Female')
input3 = st.text_input("Please write SeniorCitizen",0)
input4 = st.text_input("Please write Partner","Yes")
input5 = st.text_input("Please write Dependents","No")
input6 = st.number_input("insert number",0,20,7,5)
if st.button('result'):
    st.success('setosa')
# # # #########################################################


st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

# # # # # ##############################################
# ### Audio ###################################
# audio_file = open("snoop.mp3", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

# # # # # #############################################
# # ###### CSS BACKGROUND #######################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# # # # #####################
### Footer #########
def show_footer():
    st.markdown("***")
    st.markdown(""" **Do you like this example app?** Follow me on
                [Linkedin](https://www.linkedin.com/in/daniele-grotti-38681146/).""")

show_footer()
