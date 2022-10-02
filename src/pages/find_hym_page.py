import glob
import json

import streamlit as st
import pyperclip

base_path = 'data/hymn/'


def get_letter(path):
	with open(path) as file:
		hymn = json.load(file)

	title = hymn['title']

	letter = '\n\n'.join(hymn['letter'])

	out = title + '\n\n' + letter

	return out


def format_options(alias_options: list[str], path_options: list[str]) -> list[tuple[str, str]]:

	data = zip(alias_options, path_options)

	struct_options = map(
		lambda x: (
			int(x[0]) if 'A' not in x[0] else int(x[0][:-2]),
			x[0],
			x[1]
		),
		data
	)

	sorted_options = sorted(
		struct_options,
		key=lambda x: x[0]
	)

	return [
		(x[1], x[2]) for x in sorted_options
	]


def quick_hymn_show_page():

	hymns_paths = glob.glob(base_path + '*.json')

	options = [x if ' \ '.strip() not in x else x.replace(' \ '.strip(), '/') for x in hymns_paths]

	clean_options = [x.split('/')[-1][:-5] for x in options]

	formated_options = format_options(clean_options, hymns_paths)

	selectbox = st.selectbox(
		'Quais são os hinos que você quer?',
		formated_options,
		format_func=lambda x: x[0]
	)

	letter = get_letter(selectbox[1])
	st.text(letter)

	if st.button('Copiar', on_click=pyperclip.copy(letter)):
		st.success('Hino copiado!', icon="✅")
