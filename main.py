import streamlit as st
import base64
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Doodleism",
    page_icon="🎨",
    layout="wide"
)
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
        @import url('https://fonts.googleapis.com/css2?family=Metanoia&display=swap');
 @font-face {
        font-family: 'Metanoia';
        src: url('fonts/Metanoia.woff2') format('woff2'),
             url('fonts/Metanoia.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }
    
    .main-header {
        text-align: center;
        font-size: 4rem;
        
        font-family: 'Metanoia', sans-serif;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
        color: #4A4A4A;
    }

                html {
        scroll-behavior: smooth;
    }
    
    .nav-links { 
        text-align: center;
        margin: 0px 0 40px 0;
    }
    
    .nav-links a {
        margin: 0 15px;
        text-decoration: none;
        color: #333;
        font-weight: 500;
        padding: 5px 10px;
        border-radius: 5px;
    }
    
    .nav-links a:hover {
        text-decoration: underline;
    }
    
    
            .banner {
        background-color: #f8f1e9;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
        color: #2e7d32;
        font-size: 2rem;
        font-weight: bold;
    }
            .disclaimer {
        font-size: 0.8rem;
        color: #555;
        text-align: center;
    }
            .category-title {
        text-align: center;
        font-weight: bold;
        color: #333;
        margin-top: 10px;
    }
    .card {
        border-radius: 10px;
        padding: 10px;
        transition: transform 0.3s;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .cta { 
        display: flex;
        flex-wrap: wrap; /* Allows wrapping on smaller screens */
        background-color: #e6e6e6;
        padding: 30px;
        gap: 30px;
        align-items: center;
        justify-content: center;
    }

    .cta img {
        width: 100%;
        max-width: 500px; /* Default for large screens */
        height: auto;
    }

    .cta-form {
        flex: 1;
        min-width: 300px; /* Ensures form doesn't shrink too much */
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .cta {
            flex-direction: column; /* Stack items on smaller screens */
            text-align: center;
        }
        .cta img {
            max-width: 350px;
        }
    }

    @media (max-width: 480px) {
        .cta img {
            max-width: 250px;
        }
    }

    .custom-title1 {
        font-family: 'Nunito', sans-serif;
        font-size: 32px;
        font-weight: bold; /* Bold text */
        text-align: center; /* Centers title on smaller screens */
    }

    .contact-form input, .contact-form button {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .contact-form button {
        background-color: #333;
        color: white;
        cursor: pointer;
        border: none;
    }
            </style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="nav-links">
    <a href="#home">HOME</a>
    <a href="#gallery">GALLERY</a>
    <a href="#celeb-corner">CELEB CORNER</a>
    <a href="#contact">CONTACT US</a>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="main-header">BK STUDIO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Elevate your space with timeless portraits</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("B722849C-CB32-4ED3-90EA-515898C94CAC.PNG")

with col3:
    st.write(' ')

st.markdown("""
<div class="banner" style="background-image: url('https://placeholder.com'); background-size: cover;">
    Spring Sale -30% &nbsp;&nbsp;&nbsp; code: SPRING25
</div>
<p class="disclaimer">*applicable to all items in my store, excluding rush orders and printed products.</p>
""", unsafe_allow_html=True)

def get_image_base64(image_path):
    """Converts a local image to a base64 string for embedding in HTML."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def image_card(img_path, title, col):
    with col:
        img_base64 = get_image_base64(img_path)  # Convert image to base64
        st.markdown(
            f"""
            <style>
                .image-container {{
                    text-align: center;
                    transition: transform 0.3s ease-in-out;
                }}
                .image-container:hover {{
                    transform: scale(1.1);
                }}
                .image-container img {{
                    display: block;
                    margin: auto;
                    border-radius: 10px;
                    
                    width: 100%; /* Makes image responsive */
                    max-width: 350px; /* Ensures max size on large screens */
                    height: auto; /* Maintains aspect ratio */
                    
                    @media (max-width: 768px) {{ /* Medium screens */
                        max-width: 250px;
                    }}
                    
                    @media (max-width: 480px) {{ /* Small screens */
                        max-width: 180px;
                    }}
                }}
                .image-title {{
                    font-size: 14px;
                    margin-top: 5px;
                }}
            </style>
            <div class="image-container">
                <img src="data:image/jpeg;base64,{img_base64}">
                <p class="image-title">{title}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# What are you looking for? section
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400&display=swap');

        /* Override Streamlit's default padding */
        .custom-title-container {
            background-color: #F3F3F4;
            width: 100vw; /* Full viewport width */
            position: relative;
            left: -70px; /* Adjust alignment */
            padding: 30px 0;
            text-align: center;
            margin-bottom: 40px;
        }

        .custom-title {
            font-family: 'Nunito', sans-serif;
            font-size: 32px;
            font-weight: normal;
            color: black;
        }

        /* Extend background to full width */
        .main .block-container {
            padding-left: 0px;
            padding-right: 0px;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div id="gallery" class="section"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="banner" style="background-color: #F3F3F4; background-size: cover; font-family: 'Nunito', sans-serif; font-size: 32px;
            font-weight: normal;
            color: black; border-radius: 0px;">
    What are you looking for?
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
image_card("solo.jpeg", "SOLO", col1)
image_card("couple2.jpeg", "COUPLES", col2)
image_card("friends.jpeg", "FRIENDS", col3)

col1, col2, col3 = st.columns(3)

image_card("family2.jpeg", "FAMILIES", col1)
image_card("family.jpeg", "SPECIAL OCCASION", col2)
image_card("baby.jpeg", "EXTRAS", col3)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400&display=swap');

        /* Override Streamlit's default padding */
        .custom-title-container2 {
            background-color: #F3F3F4;
            width: 100vw; /* Full viewport width */
            position: relative;
            left: -70px; /* Adjust alignment */
            padding: 30px 0;
            text-align: center;
            margin-bottom: 10px;
        }

        .custom-title2 {
            font-family: 'Nunito', sans-serif;
            font-size: 32px;
            font-weight: normal;
            color: black;
        }

        /* Extend background to full width */
        .main .block-container {
            padding-left: 0px;
            padding-right: 0px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div id="celeb-corner" class="section"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="banner" style="background-color: #F3F3F4; background-size: cover; font-family: 'Nunito', sans-serif; font-size: 32px;
            font-weight: normal;
            color: black; border-radius: 0px; margin-bottom: 0px;">
    Celeb Corner
</div>
""", unsafe_allow_html=True)
# Image URLs and Captions
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# List of images and captions (convert to base64)
images = [
    (get_base64_image("keerthy.jpeg"), "Ms. Keerthy Suresh"),
    (get_base64_image("arya.jpeg"), "Mr. Arya"),
    (get_base64_image("sam.jpeg"), "Ms. Samantha Ruth Prabhu"),
    (get_base64_image("arun.jpeg"), "Mr. Arun Vijay"),
    (get_base64_image("vaibhav.jpeg"), "Mr. Vaibhav"),
]

# Auto-refresh every 3 seconds
count = st_autorefresh(interval=2000, limit=None, key="slider_key")

# Calculate index for rotating images
index = count % len(images)

# Inject CSS for proper layout
st.markdown(
    """
    <style>
    .slider-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        overflow: hidden;
        width: 100%;
    }
    .slider-item {
        flex: 1;
        max-width: 200px;
        text-align: center;
    }
    .slider-item img {
        width: 100%;
        max-width: 150px;
        height: auto;
        border-radius: 10px;
        object-fit: cover;
    }
    .caption {
        font-size: 14px;
        font-weight: bold;
        margin-top: 5px;
    }
    
    /* Responsive Styles */
    @media (max-width: 768px) { /* Tablets */
        .slider-wrapper {
            flex-wrap: wrap;
        }
        .slider-item {
            width: 45%;
        }
    }

    @media (max-width: 480px) { /* Mobile */
        .slider-item {
            width: 90%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generate dynamic HTML for images (base64 encoded)
slider_html = f"""
<div class="slider-wrapper">
    <div class="slider-item">
        <img src="data:image/jpeg;base64,{images[index % len(images)][0]}" />
        <div class="caption">{images[index % len(images)][1]}</div>
    </div>
    <div class="slider-item">
        <img src="data:image/jpeg;base64,{images[(index + 1) % len(images)][0]}" />
        <div class="caption">{images[(index + 1) % len(images)][1]}</div>
    </div>
    <div class="slider-item">
        <img src="data:image/jpeg;base64,{images[(index + 2) % len(images)][0]}" />
        <div class="caption">{images[(index + 2) % len(images)][1]}</div>
    </div>
</div>
"""

# Display the slider
st.markdown(slider_html, unsafe_allow_html=True)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400&display=swap');

        .custom-title {
            font-family: 'Nunito', sans-serif;
            font-size: 32px;
            font-weight: normal;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .review-box {
            background-color: #fdfbf5; /* Light beige shade */
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            font-family: 'Avenir', sans-serif;
        }

        .review-stars {
            color: #FFD700; /* Gold star color */
            font-size: 20px;
        }

        .review-text {
            font-size: 16px;
            color: #333;
            line-height: 1.5;
        }

        .review-author {
            font-weight: bold;
            margin-top: 10px;
        }

        .review-location {
            font-size: 14px;
            color: #777;
        }

        .plus-icon {
            font-size: 24px;
            color: #bbb;
            cursor: pointer;
            text-align: center;
            display: block;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner" style="background-color: #F3F3F4; background-size: cover; font-family: 'Nunito', sans-serif; font-size: 32px;
            font-weight: normal;
            color: black; border-radius: 0px; margin-bottom: 10px;">
    What Clients Say
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="review-box">
        <div class="review-stars">⭐⭐⭐⭐⭐</div>
        <p class="review-text">"Jordi created the perfect wedding invitation for us! The portrait looked just like us and we received so many compliments."</p>
        <p class="review-author">Sarah & Michael</p>
        <p class="review-location">New York, USA - March 15, 2024</p>
        <div class="plus-icon">+</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="review-box">
        <div class="review-stars">⭐⭐⭐⭐⭐</div>
        <p class="review-text">"The family portrait with our pets is amazing! Jordi captured everyone's personality perfectly."</p>
        <p class="review-author">The Johnson Family</p>
        <p class="review-location">Los Angeles, USA - June 8, 2024</p>
        <div class="plus-icon">+</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="review-box">
        <div class="review-stars">⭐⭐⭐⭐⭐</div>
        <p class="review-text">"Quick turnaround and excellent communication. The anniversary gift was a huge hit!"</p>
        <p class="review-author">David L.</p>
        <p class="review-location">London, UK - September 22, 2024</p>
        <div class="plus-icon">+</div>
    </div>
    """, unsafe_allow_html=True)

img_65=get_image_base64("potrait.jpeg")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400&display=swap');

        .custom-title1 {
            font-family: 'Nunito', sans-serif;
            font-size: 32px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div id="contact" class="section"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="cta">
    <img src="data:image/jpeg;base64,{img_65}" alt="Artist with portrait">
    <div class="cta-form">
        <div class='custom-title1'>Get your Portrait done today!</div>
        <div class="contact-form">
            <label>Name</label>
            <input type="text" placeholder="">
            <label>Phone number</label>
            <input type="tel" placeholder="">
            <label>Email</label>
            <input type="email" placeholder="">
            <button>Request Portrait</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Encode your uploaded image
image_path = "WhatsApp Image 2025-04-03 at 3.18.44 AM.jpeg"
img_base644 = encode_image(image_path)

# Your Instagram profile link
instagram_url = "https://www.instagram.com/_bk_studio_?igsh=MXdnOXJnaGZnamRqag%3D%3D&utm_source=qr"

# Footer HTML
footer = f"""
    <div style="text-align: center; padding: 20px; ">
        <a href="{instagram_url}" target="_blank">
            <img src="data:image/jpeg;base64,{img_base644}" alt="Follow us on Instagram" style="width: 250px; height: 200px">
        </a>
        <p style="font-size: 14px; color: #666; margin-top: 5px;">
            © 2025 BK Studios - All Rights Reserved
        </p>
    </div>
"""

# Display the footer
st.markdown(footer, unsafe_allow_html=True)
