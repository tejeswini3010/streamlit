import streamlit as st
st.title("Hi AIML E")
st.write("hello DS")
st.header("worldCup")
st.subheader("India")
st.text_input("Enter a name")
st.number_input("Enter ur age",step=1)
st.slider("Age",0,100)
st.checkbox("i agree terms and conditions")
st.markdown("# heading1") # to include HTML tags
st.markdown("## heading2")
st.markdown("### heading3")
st.markdown("***World cup***") # bold letters
st.code(print("Hello World"))
st.radio("Choose an option", ["Option 1","Option 2","Option 3"])

st.sidebar.title("sidebar")
st.sidebar.write("this is sidebar")
st.sidebar.text_input("enter ur email")
st.sidebar.slider("select ur marks",0,100)
st.file_uploader("Upload the file")