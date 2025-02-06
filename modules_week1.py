import streamlit as st

def show():
    st.title("Week 1: Introduction to Coding")
    st.write("This week covers the basics of coding. Get ready to dive into fundamental programming concepts!")

    # Create a scrollable list of tabs
    tab_titles = [
        "Introduction to Python",
        "You made it!",
        "What is Python?",
        "Tab 4", "Tab 5", "Tab 6", "Tab 7", "Tab 8", "Tab 9", "Tab 10", "Tab 11", "Tab 12", "Tab 13"
    ]

    tabs = st.tabs(tab_titles)

    with tabs[0]:  # Introduction to Python
        st.header("1.1 Introduction to Python - Recorded Session")
        st.video("https://www.youtube.com/watch?v=Scem9sKTtJo")
        st.markdown("[**ChatGPT Prompts**](https://chatgpt.com/share/6733c214-7ac4-8004-92f1-227d11b644ff)")
        st.markdown("""
        **Content**: 
        In this session, we’ll introduce you to the basics of Python and how it can be a powerful tool for enhancing personal impact, whether you're looking to automate tasks, analyze data, or create small projects. We will cover foundational topics such as setting up your Python environment, understanding Python syntax, and exploring the practical applications of Python in everyday scenarios.
        """)

    with tabs[1]:  # You made it!
        st.header("1.2 You made it! Be prepared for your final project")
        st.video("https://www.youtube.com/watch?v=fD73oMb4NRg")

    with tabs[2]:  # What is Python?
        st.header("1.3 What is Python? Why We Chose It for Learning")
        st.markdown("""
        Python is a powerful, high-level programming language known for its readability and versatility. Used in everything from web development to scientific research, Python's syntax is clean and intuitive, making it a preferred language for both beginners and experts.

        Here’s why Python is ideal for learning:
        * **Ease of Learning**: Python's syntax closely resembles human language, making it straightforward to pick up even if you're new to coding.
        * **Wide Application**: Python powers a range of projects – from data analysis and machine learning to web apps and automation.
        * **Strong Community Support**: With a large and active community, Python offers extensive resources, libraries, and frameworks for almost every purpose, so you’re never alone when troubleshooting or exploring new concepts.
        * **Career Relevance**: Python is one of the most in-demand skills in tech, highly sought after in roles related to data science, AI, web development, and more.

        **Python’s Applications Across Various Fields**

        1. **Geosciences**
           *Example:* Geoscientists use Python for **earthquake analysis, climate modeling, and geological surveys**. Tools like **GeoPandas** and **GDAL** help analyze spatial data and visualize geological information, while APIs like the [**USGS Earthquake API**](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson) allow researchers to retrieve real-time earthquake data for analysis and predictions.

        2. **Medical and Health Sciences**
           *Example:* Python is applied in **medical image analysis**, patient data management, and drug discovery. Libraries like **SimpleITK** and **OpenCV** aid in analyzing X-rays, MRIs, and other medical images, supporting radiologists in diagnosing conditions faster and with greater accuracy.

        3. **Finance**
           *Example:* Financial analysts leverage Python for **algorithmic trading, risk assessment, and fraud detection**. Libraries like **Pandas** and **NumPy** are essential for managing large financial datasets, while **Scikit-Learn** supports predictive modeling for stock prices, making Python a valuable tool for strategic financial decisions.

        4. **Education**
           *Example:* In education, Python facilitates **student performance analysis, automation of grading**, and the creation of interactive learning apps. **Jupyter Notebooks** are commonly used by educators to deliver lessons and by students to practice hands-on coding.

        5. **Engineering and Manufacturing**
           *Example:* Engineers use Python to simulate **mechanical processes, optimize design structures, and manage production lines**. For example, **SciPy** and **Matplotlib** allow engineers to model and visualize different physical systems, helping them improve designs and operational efficiency.

        6. **Entertainment and Media**
           *Example:* In media, Python is widely used for **game development, animation, and content recommendation systems**. Libraries like **Pygame** support game development, while **Machine Learning** with **TensorFlow** and **Keras** enables platforms to recommend personalized content to users.

        7. **Agriculture**
           *Example:* Python helps in **crop yield predictions, soil health analysis, and pest detection**. Using **remote sensing data and libraries like NDVI calculations**, Python can analyze plant health and provide actionable insights to farmers.

        **More References**
        - [Python Applications in Real World](https://www.geeksforgeeks.org/python-applications-in-real-world/)
        - [7 Applications of Python Programming](https://www.bocasay.com/7-applications-python-programming/)
        - [Python Applications](https://trio.dev/python-applications/)
        """)

    # Add placeholders for the remaining tabs (optional)
    for i in range(3, 13):
        with tabs[i]:
            st.write(f"Content for Tab {i + 1} goes here.")
