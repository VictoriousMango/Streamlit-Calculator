import streamlit as st
if 'expression' not in st.session_state:
    st.session_state['expression'] = ''

col1, col2 = st.columns([9, 1])
col11, col12, col13 = st.columns([1, 1, 1])
col21, col22, col23 = st.columns([1, 1, 1])
col31, col32, col33 = st.columns([1, 1, 1]) 
col41, col42, col43 = st.columns([1, 1, 1])
col51, col52, col53, col54, col55 = st.columns([1, 1, 1, 1, 1])


def changeExp(change):
    st.session_state['expression'] += change
calculate = st.session_state['expression']
col1.header(calculate)

# Row 1
b1 = col11.button('1', use_container_width=True, on_click=changeExp('1'))
b2 = col12.button('2', use_container_width=True, on_click=changeExp('2'))
b3 = col13.button('3', use_container_width=True, on_click=changeExp('3'))
# Row 2
b4 = col21.button('4', use_container_width=True, on_click=changeExp('4'))
b5 = col22.button('5', use_container_width=True, on_click=changeExp('5'))
b6 = col23.button('6', use_container_width=True, on_click=changeExp('6'))
# Row 3
b7 = col31.button('7', use_container_width=True, on_click=changeExp('7'))
b8 = col32.button('8', use_container_width=True, on_click=changeExp('8'))
b9 = col33.button('9', use_container_width=True, on_click=changeExp('9'))
# Row 4
bOB = col41.button('(', use_container_width=True, on_click=changeExp('('))
b0 = col42.button('0', use_container_width=True, on_click=changeExp('0'))
bCB = col43.button(')', use_container_width=True, on_click=changeExp(')'))
# Row 5
bAdd = col51.button(' \+ ', use_container_width=True, on_click=changeExp('+'))
bMinus = col52.button(' \- ', use_container_width=True, on_click=changeExp('-'))
bMultiply = col53.button(' \* ', use_container_width=True, on_click=changeExp('*'))
bDivide = col54.button(' / ', use_container_width=True, on_click=changeExp('/'))
bModulo = col55.button(' % ', use_container_width=True, on_click=changeExp('%'))