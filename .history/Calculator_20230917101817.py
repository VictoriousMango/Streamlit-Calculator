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
calculate = 'Boom'
col1.header(calculate)

# Row 1
col11.button('1', use_container_width=True)
col12.button('2', use_container_width=True)
col13.button('3', use_container_width=True)
# Row 2
col21.button('4', use_container_width=True)
col22.button('5', use_container_width=True)
col23.button('6', use_container_width=True)
# Row 3
col31.button('7', use_container_width=True)
col32.button('8', use_container_width=True)
col33.button('9', use_container_width=True)
# Row 4
col41.button('(', use_container_width=True)
col42.button('0', use_container_width=True)
col43.button(')', use_container_width=True)
# Row 5
col51.button(' \+ ', use_container_width=True)
col52.button(' \- ', use_container_width=True)
col53.button(' \* ', use_container_width=True)
col54.button(' / ', use_container_width=True)
col55.button(' % ', use_container_width=True)