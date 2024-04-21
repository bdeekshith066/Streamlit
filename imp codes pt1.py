//For setting background
//For widening the page 
//Pie chart code
  
//For setting background
import streamlit as st
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

// Text decoration
st.markdown("##### Get ready to dive into the excitement of the hottest fests on campus! ")
 st.markdown("####  Your virtual BMSCE companion, offering insights into branch insiders and placement. From <u>college life</u> to hostel info, <u>cutoffs</u>, clubs, and fests, we have got you covered. Say goodbye to endless searches for <u>notes</u> and previous year <u>question papers</u> — we have it all here.", unsafe_allow_html=True)




//For widening the page 
st.set_page_config(layout="wide")


//Pie chart code
labels = 'cse', 'ise','cs-ds/iot/bs', 'ece', 'eee','md','ai-ml/ds','me','cv','ae'
            sizes = [1300, 800,450, 900, 400,250,500,350,250,160]
        

            fig1, ax1 = plt.subplots()
            pie = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,labeldistance=1.04,textprops={'fontsize': 6})
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            fig1.patch.set_alpha(0)
# Reduce the size of the pie chart
            fig1.set_size_inches(2.2, 2.2)
            for text in pie[1]:
                text.set_color('white')
            
            for text in pie[2]:
                text.set_fontsize(5)

            st.pyplot(fig1)
            st.markdown("#### :orange[No of students in each branch]")



