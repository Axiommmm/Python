import streamlit as st

def equals():
     try:
         st.session_state.bar = str(eval(st.session_state.bar))
     except:
         with col5:
            st.write("Invalid value")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        width: 200%;
        height: 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>""", unsafe_allow_html=True)
     
if "bar" not in st.session_state:
   st.session_state.bar = ""

st.write("Result")
st.title(st.session_state.bar if st.session_state.bar != "" else "Cleared")

col1, col2, col3, col4, col5 = st.columns([1,1,1,1,4])

with col1:
   st.button("C", on_click=lambda: st.session_state.update(bar=""))
   st.button("")
   st.button("7", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "7"))
   st.button("4", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "4"))
   st.button("1", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "1"))
   st.button(".", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "."))
with col2:
   st.button("(", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "("))
   st.button(" ")
   st.button("8", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "8"))
   st.button("5", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "5"))
   st.button("2", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "2"))
   st.button("0", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "0"))
with col3:
   st.button(")", on_click=lambda: st.session_state.update(bar=st.session_state.bar + ")"))
   st.button("  ")
   st.button("9", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "9"))
   st.button("6", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "6"))
   st.button("3", on_click=lambda: st.session_state.update(bar=st.session_state.bar + "3"))
with col4:
   if(st.session_state.bar != ""):
      st.button("⌫", on_click=lambda: st.session_state.update(bar = st.session_state.bar[0:-1] if st.session_state.bar[-1] != " " else st.session_state.bar[0:-3]))
   else:
      st.button("⌫")
   st.button("÷", on_click=lambda: st.session_state.update(bar=st.session_state.bar + " / "))
   st.button("×", on_click=lambda: st.session_state.update(bar=st.session_state.bar + " * "))
   st.button("\u2212", on_click=lambda: st.session_state.update(bar=st.session_state.bar + " - "))
   st.button("**+**", on_click=lambda: st.session_state.update(bar=st.session_state.bar + " + "))
   st.button("=", on_click=equals)

