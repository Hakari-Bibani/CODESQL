import streamlit as st

def show():
    st.title("Week 1: Introduction to Coding")
    st.write("This week covers the basics of coding. Get ready to dive into fundamental programming concepts!")

    tab_names = [
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
    ]

    tabs = st.tabs(tab_names)

    # Define a dictionary of list styles
    list_styles = {
        "roundy": """
            <style>
            .roundy-list {
                list-style: none; /* Remove default bullet points */
                padding-left: 0;  /* Remove default padding */
            }
            .roundy-list li {
                background-color: #f0f2f6; /* Background color for each list item */
                padding: 0.5em 1em;
                margin-bottom: 0.5em;
                border-radius: 20px; /* Round the corners */
                border: 1px solid #ccc;
            }
            </style>
        """,
        "square": """
            <style>
            .square-list {
                list-style: square outside;
                padding-left: 1.5em;
            }
            </style>
        """,
        "checkmark": """
            <style>
            .checkmark-list {
                list-style: none;
                padding-left: 0;
            }
            .checkmark-list li:before {
                content: "\\2713\\0020"; /* Unicode checkmark */
                color: green;
                margin-left: -1.3em;
                margin-right: 0.3em;
            }
            </style>
        """,
        "plain": "" # No styling
    }

    # Choose the list style you want to use (make this changeable via a selectbox if needed)
    selected_list_style = st.sidebar.selectbox("Select List Style", list(list_styles.keys()))

    # Apply the selected list style
    st.markdown(list_styles[selected_list_style], unsafe_allow_html=True)  # Put styling here so it applies to all lists.

    with tabs[2]:
        st.header("1.3 What is Python? Why We Chose It for Learning")
        st.write("Python is a powerful, high-level programming language known for its readability and versatility. Used in everything from web development to scientific research, Python's syntax is clean and intuitive, making it a preferred language for both beginners and experts.")
        st.write("Here’s why Python is ideal for learning:")
        st.markdown(f"""
            <ul class="{'roundy-list' if selected_list_style == 'roundy' else ('square-list' if selected_list_style == 'square' else ('checkmark-list' if selected_list_style == 'checkmark' else ''))}">
                <li>Ease of Learning: Python's syntax closely resembles human language, making it straightforward to pick up even if you're new to coding.</li>
                <li>Wide Application: Python powers a range of projects – from data analysis and machine learning to web apps and automation.</li>
                <li>Strong Community Support: With a large and active community, Python offers extensive resources, libraries, and frameworks for almost every purpose, so you’re never alone when troubleshooting or exploring new concepts.</li>
                <li>Career Relevance: Python is one of the most in-demand skills in tech, highly sought after in roles related to data science, AI, web development, and more.</li>
            </ul>
        """, unsafe_allow_html=True)

        st.subheader("Python’s Applications Across Various Fields")

        st.subheader("1. Geosciences")
        st.write("*Example:* Geoscientists use Python for **earthquake analysis, climate modeling, and geological surveys**. Tools like **GeoPandas** and **GDAL** help analyze spatial data and visualize geological information, while APIs like the **USGS Earthquake API** (https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojsonLinks to an external site.) allow researchers to retrieve real-time earthquake data for analysis and predictions.")

        st.subheader("2. Medical and Health Sciences")
        st.write("*Example:* Python is applied in **medical image analysis**, patient data management, and drug discovery. Libraries like **SimpleITK** and **OpenCV** aid in analyzing X-rays, MRIs, and other medical images, supporting radiologists in diagnosing conditions faster and with greater accuracy.")

        st.subheader("3. Finance")
        st.write("*Example:* Financial analysts leverage Python for **algorithmic trading, risk assessment, and fraud detection**. Libraries like **Pandas** and **NumPy** are essential for managing large financial datasets, while **Scikit-Learn** supports predictive modeling for stock prices, making Python a valuable tool for strategic financial decisions.")

        st.subheader("4. Education")
        st.write("*Example:* In education, Python facilitates **student performance analysis, automation of grading**, and the creation of interactive learning apps. **Jupyter Notebooks** are commonly used by educators to deliver lessons and by students to practice hands-on coding.")

        st.subheader("5. Engineering and Manufacturing")
        st.write("*Example:* Engineers use Python to simulate **mechanical processes, optimize design structures, and manage production lines**. For example, **SciPy** and **Matplotlib** allow engineers to model and visualize different physical systems, helping them improve designs and operational efficiency.")

        st.subheader("6. Entertainment and Media")
        st.write("*Example:* In media, Python is widely used for **game development, animation, and content recommendation systems**. Libraries like **Pygame** support game development, while **Machine Learning** with **TensorFlow** and **Keras** enables platforms to recommend personalized content to users.")

        st.subheader("7. Agriculture")
        st.write("*Example:* Python helps in **crop yield predictions, soil health analysis, and pest detection**. Using **remote sensing data and libraries like NDVI calculations**, Python can analyze plant health and provide actionable insights to farmers.")

        st.subheader("More References")
        st.markdown("[https://www.geeksforgeeks.org/python-applications-in-real-world/](https://www.geeksforgeeks.org/python-applications-in-real-world/)")
        st.markdown("[https://www.bocasay.com/7-applications-python-programming/](https://www.bocasay.com/7-applications-python-programming/)")
        st.markdown("[https://trio.dev/python-applications/](https://trio.dev/python-applications/)")
