from src.hymn.utils import shown_search_bar, get_letter, prepare_txt_file
from src.setup import base_path
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_empty_hymns() -> list:
	return []


def slide_maker_page():

	hymn = shown_search_bar(base_path)
	letter = get_letter(hymn[1])
	st.code(letter, language='textile')

	selected_hymns = get_empty_hymns()

	if st.button('Adicionar Hino'):
		selected_hymns.append(hymn)

	st.subheader('Hinos Selecionados')
	st.text(
		', '.join(
			x[0] for x in selected_hymns
		)
	)

	st.download_button(
		"Baixar hinos",
		data=prepare_txt_file(selected_hymns),
		file_name='Hinos.txt'
	)

	if st.checkbox('Limpar Lista'):
		if st.button('Toda'):
			selected_hymns.clear()
			st.experimental_rerun()

		del_hymn = st.selectbox(
			'Quais deles você quer apagar?',
			selected_hymns,
			format_func=lambda x: x[0]
		)

		if st.button('Apagar'):
			if del_hymn is not None:
				selected_hymns.remove(del_hymn)
				st.experimental_rerun()

