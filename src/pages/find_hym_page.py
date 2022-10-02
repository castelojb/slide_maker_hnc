import streamlit as st

from src.hymn.utils import get_letter, shown_search_bar
from src.setup import base_path


def quick_hymn_show_page():

	hymn = shown_search_bar(base_path)

	letter = get_letter(hymn[1])
	st.code(letter, language='textile')
