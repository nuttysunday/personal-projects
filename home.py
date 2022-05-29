import streamlit as st
from PIL import Image

st.header("Personal Projects")

with st.expander("Image Colorization (08/2021 - 10/2021)"):
    st.write("Description: Made a Neural Network which is inspired from a research paper called 'Let there be color!' using tensorflow framework, cleansing and prepocessing of the dataset. Trained the neural network model, which converts the black and white images to color images")
    st.write("Technologies Used: Tensorflow, Deep learning, Convolutional neural networks(CNN), Google Colab, skimage, os")
    video_file1 = open('colourization.mp4', 'rb')
    video_bytes1 = video_file1.read()
    st.video(video_bytes1)
    st.write("Test results")
    image = Image.open('testing.PNG')
    st.image(image)

with st.expander("Hand gesture recogniton (05/2021 - 07/2021)"):
    st.write("Description: With the help of this project you can play/ pause, increase/ decrease volume of video playing on your system")
    st.write("Technologies Used: OpenCV, mediapipe, numpy, vlc and pycaw ")
    st.write("Github link: [link](https://github.com/nuttysunday/Hand-Gesture-Recognition)")
    video_file = open('hand.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with st.expander("Covid Data Analysis (02/2021 - 05/2021)"):
    st.write("Description: Used matplotlib and seaborn to display beautiful visualisation of covid19 data, and machine learning to predict the number of cases over a certain time period")
    st.write("Technologies Used: pandas, numpy, matplotlib, seaborn , machine learning, sklearn (linear regression, polynomial regression")
    st.write("Github link: [link](https://github.com/nuttysunday/Covid19-Prediction)")
    video_file1 = open('covid.mp4', 'rb')
    video_bytes1 = video_file1.read()
    st.video(video_bytes1)

with st.expander("Healthcare Chatbot (01/2022 - 05/2022)"):
    st.write("Description:")
    st.write("A healthcare Chatbot which converses human-like using NLP and predicts disease after symptoms are provided as an input with an accuracy of 92%")
    st.write("Technologies Used: tensorflow, sklearn, numpy, pandas, streamlit, matplotlib, NLP, machine learning")
    st.write("Github link: [link](https://github.com/nuttysunday/healthcare_chatbot)")
    video_file1 = open('healthcare.mp4', 'rb')
    video_bytes1 = video_file1.read()
    st.video(video_bytes1)

st.header("Work Experience:")

with st.expander("Free lancing (Research Paper): Protocol-Based-Deep-Intrusion-Detection-for-DoS-Normal-and-DDoS-Attacks (04/2022 - 5/2022)"):
    st.write("A free lancing project for the client where i did the coding of the research paper, got accuracy of '93%' on training set, and '87%' on testing set")
    st.write("Technologies Used: Tensorflow, Deep learning, RNN, LSTM, Jupyter Notebook, Upsampling")
    st.write("Github link: [link](https://github.com/nuttysunday/Protocol-Based-Deep-Intrusion-Detection-for-DoS-Normal-and-DDoS-Attacks)")
    st.write("Research Paper link: [link](https://github.com/nuttysunday/Protocol-Based-Deep-Intrusion-Detection-for-DoS-Normal-and-DDoS-Attacks/blob/main/1__Protocol-Based_Deep_Intrusion_Detection_for_DoS_and_DDoS_Attacks_Using_UNSW-NB15_and_Bot-IoT_Data-Sets.pdf)")
    