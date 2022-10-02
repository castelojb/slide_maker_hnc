import streamlit as st
import pyperclip

from src.hymn.utils import get_letter, shown_search_bar
from src.setup import base_path


def quick_hymn_show_page():

	hymn = shown_search_bar(base_path)

	letter = get_letter(hymn[1])
	st.text(letter)

	if st.button('Copiar', on_click=pyperclip.copy(letter)):
		st.success('Hino copiado!', icon="✅")
