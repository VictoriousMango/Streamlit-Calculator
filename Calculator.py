import streamlit as st
if 'expression' not in st.session_state:
    st.session_state['expression'] = ''

col1, col2 = st.columns([9, 1])
col11, col12, col13 = st.columns([1, 1, 1])
col21, col22, col23 = st.columns([1, 1, 1])
col31, col32, col33 = st.columns([1, 1, 1]) 
col41, col42, col43 = st.columns([1, 1, 1])
col51, col52, col53, col54, col55 = st.columns([1, 1, 1, 1, 1])
col61, col62 = st.columns([1, 1])


def clear():
    st.session_state['expression'] = ''
def _0():
    st.session_state['expression'] += '0'
def _1():
    st.session_state['expression'] += '1'
def _2():
    st.session_state['expression'] += '2'
def _3():
    st.session_state['expression'] += '3'
def _4():
    st.session_state['expression'] += '4'
def _5():
    st.session_state['expression'] += '5'
def _6():
    st.session_state['expression'] += '6'
def _7():
    st.session_state['expression'] += '7'
def _8():
    st.session_state['expression'] += '8'
def _9():
    st.session_state['expression'] += '9'
def add():
    st.session_state['expression'] += '+'
def subtract():
    st.session_state['expression'] += '-'
def multiply():
    st.session_state['expression'] += '*'
def divide():
    st.session_state['expression'] += '/'
def modulo():
    st.session_state['expression'] += '%'
def openBracket():
    st.session_state['expression'] += '('
def closeBracket():
    st.session_state['expression'] += ')'
def equals():
    st.session_state['expression'] = str(eval(st.session_state['expression']))

calculate = 'Enter Expression' if st.session_state['expression'] == '' else st.session_state['expression']
col1.header(calculate)

# Row 1
b1 = col11.button('1', use_container_width=True, on_click=_1)
b2 = col12.button('2', use_container_width=True, on_click=_2)
b3 = col13.button('3', use_container_width=True, on_click=_3)
# Row 2
b4 = col21.button('4', use_container_width=True, on_click=_4)
b5 = col22.button('5', use_container_width=True, on_click=_5)
b6 = col23.button('6', use_container_width=True, on_click=_6)
# Row 3
b7 = col31.button('7', use_container_width=True, on_click=_7)
b8 = col32.button('8', use_container_width=True, on_click=_8)
b9 = col33.button('9', use_container_width=True, on_click=_9)
# Row 4
bOB = col41.button('(', use_container_width=True, on_click=openBracket)
b0 = col42.button('0', use_container_width=True, on_click=_0)
bCB = col43.button(')', use_container_width=True, on_click=closeBracket)
# Row 5
bAdd = col51.button(' \+ ', use_container_width=True, on_click=add)
bMinus = col52.button(' \- ', use_container_width=True, on_click=subtract)
bMultiply = col53.button(' \* ', use_container_width=True, on_click=multiply)
bDivide = col54.button(' / ', use_container_width=True, on_click=divide)
bModulo = col55.button(' % ', use_container_width=True, on_click=modulo)
# Row 6
col61.button('Clear', use_container_width=True, on_click=clear)
col62.button('=', use_container_width=True, on_click=equals)


