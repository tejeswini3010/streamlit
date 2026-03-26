
import streamlit as st
import time
st.title("HEllo aiml e ds")
st.write("heelo aiml e ds")
st.write(1234)
st.write([1,2,3,4,5])
st.header("MAin header")
st.subheader("sub header")
st.text_input("enter text")
st.number_input("enter number",step=1)
st.markdown("# this is a mark down header ")
st.markdown("## this is a mark down subheader ")
st.markdown("### this is a mark down subsubheader ")
st.markdown("** world cup **")
st.markdown("** Italic **")
st.checkbox("check me out")
st.text_area("enter the longer text")
st.radio("choose an option",["option 1","option 2"])
num=st.selectbox("select an option",["option A","option B"])
st.write(f"you selected:{num}")
st.sidebar.write("this is side bar")
st.sidebar.selectbox("menu",["A","B","C"])

#st.image("Image .png",type=["png"],caption="this is dashboard",width=100)
#st.audio()
#st.video()
with st.form("my_form"):
    st.write("Inside the form")
    name=st.text_input("name")
    age=st.number_input("age",step=1)
    password=st.text_input("password",type="password")
    address=st.text_are("additional information")
    submitted=st.form_submit_button("submit")
    if submitted:
        st.write(f"name:{name},age:{age}")
## animations
st.balloons()
st.snow()
## 
st.date_input("enter sate")
st.time_input("enter time")
st.color_picker("select color")
st.latex(r'''E=mc^2''')
col1,col2=st.columns(2)
with col1:
    st.text_input("enter a first name")
with col2:
    st.text_input("enter the last name")
st.slider("select value",0,100)
progress=st.progress(50)
# horizontal lines
st.markdown("---")
with st.spinner("wait"):
    time.sleep(10)
st.write("process completed!")