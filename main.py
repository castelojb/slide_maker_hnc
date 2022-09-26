import streamlit as st
import glob

from src.pages.hymn import Hymn

base_path = 'data/hymn/'


def about_page():

    st.markdown('Desenvolvido pelo aluno João Araújo Castelo Branco para fins didaticos')
    st.markdown('Email: joaocb14@gmail.com')


def slide_maker():

    hymns_paths = glob.glob(base_path + '*.json')

    options = [x if ' \ '.strip() not in x else x.replace(' \ '.strip(), '/') for x in hymns_paths]

    clean_options = [x.split('/')[-1][:-5] for x in options]

    selectbox = st.selectbox(
        'Quais são os hinos que você quer?',
        list(zip(
            clean_options, hymns_paths
        )),
        format_func=lambda x: x[0]
    )

    letter = Hymn.get_letter(selectbox[1])
    st.text(letter)


if __name__ == '__main__':

    st.title('Slide Maker')
    st.subheader('Seu site para agilizar os slides')

    options = [
        ('Sobre', about_page),
        ('Slide Maker', slide_maker),
    ]

    with st.sidebar:
        option = st.radio(
            'Escolha o setor',
            options,
            format_func=lambda x: x[0]
        )

    st.subheader(option[0])
    option[1]()

