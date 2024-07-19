import streamlit as st
import streamlit.components.v1 as components
def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">Welcome to Seed2Sapling</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)

    st.write(":orange[Every seed has a potential tree inside it. A little nurture of the sapling makes a sturdy tree. We believe this to be true of education as well. ]")
    
    st.image('divider.png')
    
   

    st.write('Education is enabling each individual to fulfil their potential: :orange[to be, to grow, to become.]')
    st.write(' Seed2Sapling - We contribute towards kids learning during these challenging times, through PM-eVidya and Diksha initiatives.')
    
    st.write('')
    st.write('')
    col4, col5,col7, col6 , col8 = st.columns([0.03,0.45,0.04,0.7, 0.02])
    with col5:
        st.write('')
        
        components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 400px;
  max-height : 400px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.9s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://www.s2seducation.com/img/photo-story/pic6.webp">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://www.s2seducation.com/img/photo-story/pic8.webp" , alt="hiiiii">
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://www.s2seducation.com/img/photo-story/pic9.webp">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://www.s2seducation.com/img/photo-story/pic11.webp">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://www.s2seducation.com/img/photo-story/pic4.webp">
    
  </div>
  
  
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=400, width=400
)
    

    with col6:
        
        tab0,tab1, tab2 = st.tabs(["About Us", "Our Philosophy", "Contact Us"])

        with tab0:
            
            st.write("- We at Seed2Sapling (S2S) are inspired by the innate potential of every seed to mature into a tree given the proper environment.")
            st.write("- We envision to create an enriched, joyful and experiential learning environment where a student becomes knowledge (re)creator instead of knowledge consumer.")
            st.write("-  Every child has the ability to observe, experience and experiment with the world around itself.")
            
            st.write("- Our inquiry-based learning methods tap into the natural curiosity of a student by asking the right questions.")
            st.write('')

        with tab1:
            
            st.write("- The purpose of education is the manifestation of perfection within. ")
            st.write("- :orange[Vision]: Our vision is to create a framework that shall provide an ecosystem for children to explore their natural potential and nurture it for a meaningful life.")
            st.write("- :orange[Mission]: Our mission is to create an enriched, joyful and experiential learning environment where a child enjoys and actively participates to become knowledge generator and not merely being knowledge consumer. The focus is not only about intellectual development, but also on emotional stability and strong moral foundation.")
            st.write(" - We empower children to reach higher levels of Bloom's taxonomy using the knowledge they acquire through their daily experiences and understanding of the world.")


        with tab2:
            st.write(" - Seed2Sapling Education Pvt Ltd")
            st.write(" - No: 29, 4th Floor, 7th Cross Road, Ranna Rd, Pampa Extension, Hebbal Kempapura,Bengaluru, Karnataka 560024")
            st.write(" - :orange[Email]: info@s2seducation.com")
            st.write(" - :orange[Phone]: +91 9902346354")
            st.write(" - :orange[Google maps ]: https://maps.app.goo.gl/9MViAQWHBoKeRcR99")
            st.write(" -  If interested in subscribing the information from S2S, please fill [Form](https://docs.google.com/forms/d/e/1FAIpQLSdhhqFwb2Kt26ZrlftUodFLgJJ4lvP86Ty31AVffH7zGnhoXg/viewform)")
            


   
    st.write('')
    st.write('')
    st.image('divider.png')
    st.write('')
    col1,col2,col3 = st.columns([0.5,1,0.5])

    with col2:
        st.write('   Project by team - :orange[BYTEBUDDIES] - Deekshith B , Sanjana W G, KM Skanda , Sanjana B J , Shreyashri ')
    
    
if __name__ == "__main__":
    app()
    
