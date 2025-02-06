import streamlit as st

def show():
    st.title("Week 1: Introduction to Coding")
    st.write("This week covers the basics of coding. Get ready to dive into fundamental programming concepts!")

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs([
        "Introduction to Python",
        "You made it!",
        "What is Python?",
        "Tab 4",
        "Tab 5",
        "Tab 6",
        "Tab 7",
        "Tab 8",
        "Tab 9",
        "Tab 10",
        "Tab 11",
        "Tab 12",
        "Tab 13"
    ])

    with tab1:
        st.header("1.1 Introduction to Python - Recorded Session")
        st.video("https://www.youtube.com/watch?v=Scem9sKTtJo")
        st.subheader("**ChatGPT Prompts**")
        st.markdown("[Links to an external site](https://chatgpt.com/share/6733c214-7ac4-8004-92f1-227d11b644ff)")
        st.subheader("**Content**:")
        st.write("In this session, we’ll introduce you to the basics of Python and how it can be a powerful tool for enhancing personal impact, whether you're looking to automate tasks, analyze data, or create small projects. We will cover foundational topics such as setting up your Python environment, understanding Python syntax, and exploring the practical applications of Python in everyday scenarios.")

    with tab2:
        st.header("1.2 You made it! Be prepared for your final project")
        st.video("https://www.youtube.com/watch?v=fD73oMb4NRg")

    with tab3:
        st.header("1.3 What is Python? Why We Chose It for Learning")
        st.write("Python is a powerful, high-level programming language known for its readability and versatility. Used in everything from web development to scientific research, Python's syntax is clean and intuitive, making it a preferred language for both beginners and experts. Here’s why Python is ideal for learning:")
        st.markdown("* **Ease of Learning**: Python's syntax closely resembles human language, making it straightforward to pick up even if you're new to coding.")
        st.markdown("* **Wide Application**: Python powers a range of projects – from data analysis and machine learning to web apps and automation.")
        st.markdown("* **Strong Community Support**: With a large and active community, Python offers extensive resources, libraries, and frameworks for almost every purpose, so you’re never alone when troubleshooting or exploring new concepts.")
        st.markdown("* **Career Relevance**: Python is one of the most in-demand skills in tech, highly sought after in roles related to data science, AI, web development, and more.")
        st.subheader("**Python’s Applications Across Various Fields**")
        st.write("1. **Geosciences**")
        st.write("*Example:* Geoscientists use Python for **earthquake analysis, climate modeling, and geological surveys**. Tools like **GeoPandas** and **GDAL** help analyze spatial data and visualize geological information, while APIs like the **USGS Earthquake API** (https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojsonLinks to an external site.) allow researchers to retrieve real-time earthquake data for analysis and predictions.")
        st.write("2. **Medical and Health Sciences**")
        st.write("*Example:* Python is applied in **medical image analysis**, patient data management, and drug discovery. Libraries like **SimpleITK** and **OpenCV** aid in analyzing X-rays, MRIs, and other medical images, supporting radiologists in diagnosing conditions faster and with greater accuracy.")
        st.write("3. **Finance**")
        st.write("*Example:* Financial analysts leverage Python for **algorithmic trading, risk assessment, and fraud detection**. Libraries like **Pandas** and **NumPy** are essential for managing large financial datasets, while **Scikit-Learn** supports predictive modeling for stock prices, making Python a valuable tool for strategic financial decisions.")
        st.write("4. **Education**")
        st.write("*Example:* In education, Python facilitates **student performance analysis, automation of grading**, and the creation of interactive learning apps. **Jupyter Notebooks** are commonly used by educators to deliver lessons and by students to practice hands-on coding.")
        st.write("5. **Engineering and Manufacturing**")
        st.write("*Example:* Engineers use Python to simulate **mechanical processes, optimize design structures, and manage production lines**. For example, **SciPy** and **Matplotlib** allow engineers to model and visualize different physical systems, helping them improve designs and operational efficiency.")
        st.write("6. **Entertainment and Media**")
        st.write("*Example:* In media, Python is widely used for **game development, animation, and content recommendation systems**. Libraries like **Pygame** support game development, while **Machine Learning** with **TensorFlow** and **Keras** enables platforms to recommend personalized content to users.")
        st.write("7. **Agriculture**")
        st.write("*Example:* Python helps in **crop yield predictions, soil health analysis, and pest detection**. Using **remote sensing data and libraries like NDVI calculations**, Python can analyze plant health and provide actionable insights to farmers.")
        st.subheader("**More References**")
        st.markdown("[https://www.geeksforgeeks.org/python-applications-in-real-world/Links to an external site.](https://www.geeksforgeeks.org/python-applications-in-real-world/Links to an external site.)")
        st.markdown("[https://www.bocasay.com/7-applications-python-programming/Links to an external site.](https://www.bocasay.com/7-applications-python-programming/Links to an external site.)")
        st.markdown("[https://trio.dev/python-applications/Links to an external site.](https://trio.dev/python-applications/Links to an external site.)")


    with tab4:
        st.write("Content for Tab 4")

    with tab5:
        st.write("Content for Tab 5")

    with tab6:
        st.write("Content for Tab 6")

    with tab7:
        st.write("Content for Tab 7")

    with tab8:
        st.write("Content for Tab 8")

    with tab9:
        st.write("Content for Tab 9")

    with tab10:
        st.write("Content for Tab 10")

    with tab11:
        st.write("Content for Tab 11")

    with tab12:
        st.write("Content for Tab 12")

    with tab13:
        st.write("Content for Tab 13")
