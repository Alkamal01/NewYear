import streamlit as st
import datetime
import random
from PIL import Image, ImageFilter

# Function to set the background
def set_background():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://www.example.com/image.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to generate New Year resolutions
def generate_resolutions():
    resolutions_list = [
        "Learn a new skill every month.",
        "Read at least one book per month.",
        "Exercise for at least 30 minutes a day.",
        "Practice mindfulness and meditation regularly.",
        "Connect with friends and family more often.",
        "Set and achieve career goals.",
    ]
    return random.sample(resolutions_list, k=3)

# Function to apply festive overlay to an image
def apply_festive_overlay(image):
    img = Image.open(image)
    overlay = Image.open('festive_overlay.jpg')
    overlay = overlay.resize(img.size)
    festive_filtered_img = Image.blend(img, overlay, alpha=0.5)
    return festive_filtered_img


# Add FontAwesome CSS for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)



# Function to create the New Year wish app
def new_year_wish():
    # Set background image
    set_background()

    # Title and Subheader
    st.title('New Year Celebration App 🎉')
    st.subheader('Wishing you a fantastic New Year!')

    # Countdown Timer
    new_year_date = datetime.datetime(2024, 1, 1)
    today = datetime.datetime.now()
    time_left = new_year_date - today
    st.write(f"Time left until New Year: {time_left.days} days, {time_left.seconds // 3600} hours.")

    # Festive Messages
    festive_messages = [
        "May this New Year bring you joy and success!",
        "Wishing you health, happiness, and prosperity in the coming year.",
        "Cheers to a new beginning! Happy New Year!",
    ]
    st.info(random.choice(festive_messages))

    # Generate Resolutions Button
    if st.button('Generate New Year Resolutions'):
        resolutions = generate_resolutions()
        st.success('Here are your New Year Resolutions:')
        for resolution in resolutions:
            st.write(f"- {resolution}")

    # Section for Music Player and Upload Photos
    col1, col2 = st.columns(2)

    with col1:
        # Section for Music Player
        st.subheader('New Year Music Player 🎶')
        st.write("Choose from the playlist or add your own cheerful New Year songs!")

        # Example playlist
        playlist = {
            "Song 1": "https://music.youtube.com/watch?v=0RPzLGxepxg&list=OLAK5uy_nfb-BiQpZg2OMUiS_YsH0KMGZXPjmO_0E",
            "Song 2": "https://music.youtube.com/watch?v=W2yASCPIkLA",
        }

        selected_song = st.selectbox('Select a song from the playlist', list(playlist.keys()))

        if st.button('Play'):
            st.audio(playlist[selected_song], format='audio/mp3', start_time=0)

    with col2:
        # Section for Upload Photos and Apply Filters
        st.subheader('Upload and Share New Year Photos 📸')
        uploaded_file = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display the original image
            # st.image(uploaded_file, caption="Original Photo", use_column_width=True)

            # Apply a festive overlay
            festive_filtered_img = apply_festive_overlay(uploaded_file)
            st.image(festive_filtered_img, caption="Festive Overlay", use_column_width=True)

            # Share on Social Media Icons (Horizontal Alignment)
            st.subheader('Share on Social Media 🌟')
            whatsapp_icon = '<a href="https://wa.me/?text=Check%20out%20my%20New%20Year%20photo%21%20🎉" target="_blank"><i class="fab fa-whatsapp"></i></a>'
            twitter_icon = '<a href="https://twitter.com/intent/tweet?text=Check%20out%20my%20New%20Year%20photo%21%20🎉" target="_blank"><i class="fab fa-twitter"></i></a>'
            instagram_icon = '<a href="https://www.instagram.com/" target="_blank"><i class="fab fa-instagram"></i></a>'
            
            icons_html = f"{whatsapp_icon} {twitter_icon} {instagram_icon}"
            st.markdown(icons_html, unsafe_allow_html=True)

if __name__ == '__main__':
    new_year_wish()
