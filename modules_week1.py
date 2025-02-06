import streamlit as st

def show():
    st.title("Week 1: Introduction to Coding")
    
    # Create 13 tabs (we'll populate first 3 with content, others as placeholders)
    tab_names = [
        "Introduction to Python",
        "You made it!",
        "What is Python?",
        *[f"Tab {i}" for i in range(4, 14)]  # Placeholder names for remaining tabs
    ]
    tabs = st.tabs(tab_names)
    
    with tabs[0]:  # Introduction to Python
        st.header("1.1 Introduction to Python - Recorded Session")
        st.video("https://www.youtube.com/watch?v=Scem9sKTtJo")
        st.markdown("[**ChatGPT Prompts**](https://chatgpt.com/share/6733c214-7ac4-8004-92f1-227d11b644ff)")
        st.write("""
        **Content**: In this session, we'll introduce you to the basics of Python and how it can be a powerful tool 
        for enhancing personal impact, whether you're looking to automate tasks, analyze data, or create small projects. 
        We will cover foundational topics such as:
        - Setting up your Python environment
        - Understanding Python syntax
        - Exploring practical applications of Python in everyday scenarios
        """)
    
    with tabs[1]:  # You made it!
        st.header("1.2 You made it! Be prepared for your final project")
        st.video("https://www.youtube.com/watch?v=fD73oMb4NRg")
        st.write("Prepare for your final project by reviewing these essential concepts...")
    
    with tabs[2]:  # What is Python?
        st.header("1.3 What is Python? Why We Chose It for Learning")
        st.write("""
        Python is a powerful, high-level programming language known for its readability and versatility. 
        Used in everything from web development to scientific research, Python's syntax is clean and intuitive, 
        making it a preferred language for both beginners and experts.
        """)
        
        st.subheader("Here's why Python is ideal for learning:")
        st.markdown("""
        * **Ease of Learning**: Python's syntax closely resembles human language
        * **Wide Application**: From data analysis to machine learning
        * **Strong Community Support**: Extensive resources and libraries
        * **Career Relevance**: Highly sought-after skill in tech
        """)
        
        st.subheader("Python's Applications Across Various Fields")
        
        fields = {
            "Geosciences": {
                "examples": "Earthquake analysis, climate modeling, geological surveys",
                "tools": "GeoPandas, GDAL, USGS Earthquake API"
            },
            "Medical and Health Sciences": {
                "examples": "Medical image analysis, drug discovery",
                "tools": "SimpleITK, OpenCV"
            },
            "Finance": {
                "examples": "Algorithmic trading, fraud detection",
                "tools": "Pandas, NumPy, Scikit-Learn"
            },
            # Add other fields similarly
        }
        
        for field, details in fields.items():
            st.markdown(f"**{field}**")
            st.markdown(f"""
            *Examples:* {details['examples']}
            *Tools:* {details['tools']}
            """)
        
        st.markdown("""
        **More References:**
        - [Python Applications](https://www.geeksforgeeks.org/python-applications-in-real-world/)
        - [7 Python Applications](https://www.bocasay.com/7-applications-python-programming/)
        - [Python Use Cases](https://trio.dev/python-applications/)
        """)
    
    # Placeholder content for remaining tabs
    for i in range(3, 13):
        with tabs[i]:
            st.header(f"Content for {tab_names[i]}")
            st.write("This content is coming soon! Check back later.")
