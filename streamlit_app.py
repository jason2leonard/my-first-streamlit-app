import streamlit as st
import pandas as pd
import random

st.title('hello world !')

#header
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.markdown('this is a drill, not a real war')
multi='''If you end a line with two spaces,:
a soft return is used for the next line.''' # 务必使用3个引号
st.markdown(multi)

#color text
st.markdown(''':red[one] :green[two] 
:blue[three]''')

#slider
number=st.slider('pick a number',2,20)

st.header("This is a header with a divider", divider="gray")
st.subheader('this is a subheader',divider='green')
st.markdown(multi)
st.header("These headers have rotating dividers", divider=True)

#dataframe

df=pd.read_csv('C:/Users/huawei/Desktop/DataFILE/carsales.csv')
st.dataframe(df)
st.divider()
st.dataframe(df,column_config={
    'Month':'Year',
    'Monthly car sales in Quebec 1960-1968':'sales number'
})
#display static table
# st.table(df)
st.divider()
#data editor
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)
# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.divider()
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.divider()
#column configuration
# st.column_config.Column
data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)

st.divider()
#display metrics
st.metric(label='Temperature',value='70 F',delta='1.2')
st.metric(label='Temperature',value='70 F',delta='-2.2')
st.divider()
col1,col2,col3=st.columns(3)
col1.metric(label='Temperature',value='70 F',delta='1.2',delta_color='inverse')
col2.metric(label='Temperature',value='70 F',delta='-2.2',delta_color='off')
col3.metric(label='Wind',value='98 mph',delta='21.2')

st.divider()
#display areatable
df_1=pd.read_csv('C:/Users/huawei/Desktop/DataFILE/carsales.csv')
st.area_chart(df_1,x='Month',y='Monthly car sales in Quebec 1960-1968')
# st.area_chart(df_1,x='Month',y='Monthly car sales in Quebec 1960-1968',stack=False)
st.line_chart(df_1,x='Month',y='Monthly car sales in Quebec 1960-1968')
st.bar_chart(df_1,x='Month',y='Monthly car sales in Quebec 1960-1968')
st.scatter_chart(df_1,x='Month',y='Monthly car sales in Quebec 1960-1968')

#display table with bokeh
st.divider()
from bokeh.plotting import figure
x=[1,2,3,4,5,6]
y=[20,12,30,23,11,23]
p=figure(title='illustraion',x_axis_label='x',y_axis_label='y')
p.line(x,y,legend_label='trend',line_width=2)
st.bokeh_chart(p,use_container_width=True)

st.divider()
#input widget
st.button('Reset',type='primary')
if st.button('say hello'):
    st.write('thanks for your kindness')
else:
    st.write('say you later')

#download button
text_content='''this is some text for you'''
st.download_button('Download some item',text_content)

#download csv file
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')
csv=convert_df(df_1)
st.download_button('download data as csv',data=csv,file_name='car_sales_numb',mime='text/csv')

#feedback button
sentiment_mapping=['1','2','3','4','5']
selected=st.feedback('stars')
if selected is not None:
    st.markdown(f'you selected {sentiment_mapping[selected]} stars')

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")

st.link_button('go to google.com',url='https://www.google.com.hk/webhp?hl=zh-CN&sourceid=cnhp')

#insert columns
import numpy as np
col1,col2=st.columns(2)
data=np.random.randn(10,1)
col1.subheader('line chart')
col1.line_chart(data)
col2.subheader('table')
col2.write(data)

st.divider()

col1,col2=st.columns([0.5,0.5]) #left contains 70% right contains 30%
data=np.random.randn(10,1)
col1.subheader('line chart')
col1.line_chart(data)
col2.subheader('table')
col2.write(data)

#container
container=st.container(border=True)
container.write('this is the container')
st.write('this is outside of the container')

#dialogue
st.divider()
st.write('for modal dialogue selection')
import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("Jason"):
        vote("Jason")
    if st.button("Bob"):
        vote("Bob")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

#expander
st.bar_chart({'data':[1,4,1,2,4,2,4]})

with st.expander('see explanation'):
    st.write('''the chart above show....''')
st.divider()

#popover 弹窗
with st.popover('open popover'):
    st.markdown('hello world')
    name=st.text_input('what is your name')

st.write('your name',name)
st.divider()

add_selectbox=st.sidebar.selectbox('how old are you',('1','22','3'))

#add tabs
tab1,tab2,tab3=st.tabs(['cat','dog','owl'])
with tab1:
    st.header('a cat')
    st.markdown('what a beautiful cat')
with tab2:
    st.header('a dog')
    st.markdown('what an adorable dog')
with tab3:
    st.header('an owl')
    st.line_chart({'sales number':[2,4,55,1,23,22]})

#navigtion and pages
# pages={
#     'your account':[
#         st.Page('hello_world.py',title='hello world'),
#         st.Page('manage_account.py',title='manage your account')
#     ],
#     'Resource':[
#         st.Page('learn.py',title='learn about us'),
#         st.Page('trial.py',title='try it out')
#     ]
# }
# pg=st.navigation(pages)
# pg.run()

# def page2():
#     st.title("Second page")
#
# pg = st.navigation([
#     st.Page("page1.py", title="First page", icon="🔥"),
#     st.Page(page2, title="Second page", icon=":material/favorite:"),
# ])
# pg.run()


#session_id
number=st.slider('a number',1,10,key='slider')
st.write(st.session_state)

def lbs_to_kgs():
    st.session_state.kg=st.session_state.lbs/2.2

def kgs_to_lbs():
    st.session_state.lbs=st.session_state.kgs*2.2

col1,buff,col2=st.columns([2,1,2])
with col1:
    pounds=st.number_input('Pounds',key='lbs',on_change=lbs_to_kgs)
with col2:
    kilogram=st.number_input('Kilograms',key='kg',on_change=kgs_to_lbs)
