import streamlit as st
from src.pages.find_hym_page import quick_hymn_show_page
from src.pages.slide_maker_page import slide_maker_page


def about_page():

    st.markdown('Desenvolvido por João Araújo Castelo Branco para fins didaticos')
    st.markdown('Email: joaocb14@gmail.com')


if __name__ == '__main__':

    st.title('Slide Maker')
    st.subheader('Seu site para agilizar os slides')

    options = [
        ('Sobre', about_page),
        ('Busca Rápida', quick_hymn_show_page),
        ('Slide Maker', slide_maker_page)
    ]

    with st.sidebar:
        option = st.radio(
            'Escolha o setor',
            options,
            format_func=lambda x: x[0]
        )

    st.subheader(option[0])
    option[1]()

