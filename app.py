import streamlit as st
from bbquote.lib import get_quote


quote  = get_quote()  # assuming the function returns an author and a quote
#f"{quote['quote']}, {quote['show']}, {quote['role']}"
st.write(quote)


'# Title'
'## Sub title'
'### sub sub title'
