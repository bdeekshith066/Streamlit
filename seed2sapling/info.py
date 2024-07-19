import streamlit as st

def app():
    

    # Introduction
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text">Our Solutions</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    
    st.image('divider.png')

    with st.form('Form1'):
        st.subheader(":orange[Dialogue on Learning]")
        st.write(" A long-term engagement with teachers to present a teaching methodology (constructivist approach aided by inquiry) whose main focus is on the process of scientific and mathematical thinking and discovery, and the skills associated with it.")
        st.form_submit_button('Click here to know more')


    with st.form('Form2'):
        st.subheader(":orange[Learn2Learn In-classroom Programme]")
        st.write(" It is a curriculum-aligned programme for science and mathematics from grade 4th to 9th, facilitated along with school teachers in the classrooms.")
        st.form_submit_button('Click here to know more')

    with st.form('Form3'):
        st.subheader(":orange[School Consultancy]")
        st.write("One way to develop the attitude of exploration is by creating an environment that encourages it and also nurture the innate potential of a child.")
        st.form_submit_button('Click here to know more')

    with st.form('Form4'):
        st.subheader(":orange[DH-Cube Learning Centre ]")
        st.write(" Hearts-on, Heads-on and Hands-on learning through advanced projects in STEM.")
        st.form_submit_button('Click here to know more')

    
