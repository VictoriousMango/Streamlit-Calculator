import streamlit as st


col1, col2 = st.columns([9, 1])
col11, col12, col13 = st.columns([1, 1, 1])
col21, col22, col23 = st.columns([1, 1, 1])
col31, col32, col33 = st.columns([1, 1, 1]) 
col41, col42, col43 = st.columns([1, 1, 1])
col51, col52, col53, col54, col55 = st.columns([1, 1, 1, 1, 1])

calculate = 'Boom'
col1.header(calculate)

# Row 1
col11.button('1')
col12.button('2')
col13.button('3')
# Row 2
col21.button('4')
col22.button('5')
col23.button('6')
# Row 3
col31.button('7')
col32.button('8')
col33.button('9')
# Row 4
col31.button('(')
col32.button('0')
col33.button(')')