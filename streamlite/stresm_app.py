import streamlit as st 
st.write("I am learning dtreamlit web framework")
l=[2,3,4,5]
st.write(l)
st.write(':a:')
l2=[3,4,5,6]
import pandas as pd
df=pd.DataFrame({'A':l,'B':l2})
'smile :smile:,:100:'
df
st.write(df)
st.area_chart(df)
#widgets
name=st.text_input("Enter the name")
if name:
    st.write(name)
st.divider()
number=st.number_input("Enter the number",min_value=1,max_value=100,step=2)
st.write(f"number is{number}")

clicked=st.button(label="Click ME")
if clicked:
    st.write(':white_check_mark:'*9)
st.divider()
'CheckBox'
checked=st.checkbox("Show Data")
if checked:
    st.write(df)
st.divider()
'Radio Button'
subjects=["Python","Data science",'Machine Learning','AI'] 
subject=st.radio("Subject are :",subjects,index=0,key='sub')
st.write("Your subject is",subject)
st.write(f"Your subjet is {st.session_state.sub}")

'select option'
subjectSelected=st.selectbox('Your subjetc',subjects,index=1)
st.write(f"your subject is {subjectSelected}")

'For slider bar'
x=st.slider('x',step=5,min_value=23,max_value=200)
st.write(x)
st.divider()
'For file uploder'
df.to_csv('data.csv',index=False)
uploaded_file=st.file_uploader('upload file',type=['csv','txt'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type=='text/csv':
        data=pd.read_csv(uploaded_file)
        st.write(data)
st.divider()


'For camera'
camera_image=st.camera_input('Take a photo')
if camera_image:
    st.image(camera_image)
    import shutil
    with open('image','wb') as f:
        shutil.copyfileobj(camera_image,f)
'SlideBar'
sd=st.sidebar.selectbox("select",subjects)
st.write(sd)
my_sider=st.sidebar.slider('Price')
st.write(my_sider)
'Column '
col1,col2,col3=st.columns([.2,.3,.5])
col1.markdown("data ")
col2.write(df[2:])
with col3:
    st.header("area_chart of data")
    st.area_chart(data=df)
    
with st.expander('Click to Expand'):
    st.bar_chart(df)
    st.write("You are seeing to me!")
    if camera_image:
        st.image(camera_image)
    
'Progress bar'
import time
st.write('Starting a extensive task computation')
latest_iteration=st.empty()
my_bar=st.progress(0,text="Task is being completed please wait......")
time.sleep(2)
for i in  range(100):
    my_bar.progress(i+1)
    latest_iteration.text(f'Iteration :{1+i}')
    time.sleep(.2)
st.write('we are done :+2:')
    