import streamlit as st

def show():
    st.title("Week 1: Introduction to Coding")
    st.write("This week covers the basics of coding. Get ready to dive into fundamental programming concepts!")

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs([
        "Introduction to Python",
        "You made it!",
        "What is Python?",
        "Python Script?",
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
        st.header("1.4 What is in the Python Script?")
        st.write("A Python script combines libraries, variables, functions, and loops to create structured workflows. In a Python script, you’ll find a set of instructions written in the Python programming language. These instructions, also called code, tell the computer exactly what to do, step by step. Think of a Python script like a recipe in a cookbook, where each line of code is an instruction for completing part of the overall task. Here’s a breakdown of the main parts in a typical Python script, explained simply:")
        st.write("Importing Libraries: Often, the script starts by “importing libraries.” Libraries are collections of pre-built code that allow the script to do specific tasks, like handling data, creating visuals, or connecting to the internet. By importing them, the script can use these functions without needing to write them from scratch.")
        st.write("Example: `import pandas as pd` – this line imports a library for handling data tables.")
        st.write("Defining Variables: Variables are like labeled containers that store information, such as numbers or text. Throughout the script, these containers are used to keep track of information or settings that might be needed later.")
        st.write("Example: `temperature = 72` – stores the number 72 in a variable called “temperature.”")
        st.write("Functions and Loops: Functions are small, reusable chunks of code that perform a specific task. For example, a function might calculate an average or convert text to uppercase. Loops, on the other hand, are instructions that repeat a task multiple times. Both are used to make the code more efficient and reduce repetition.")
        st.write("Example: `for item in list:` – this starts a loop that goes through each item in a list one by one.")
        st.write("Data Processing and Analysis: Many Python scripts work with data, processing it to make it easier to analyze. This part of the script could involve cleaning data (e.g., removing empty spaces), calculating results (e.g., averages, totals), or organizing data to prepare it for the next steps.")
        st.write("Output and Visualization: Finally, a script might show results to the user by creating a chart, printing out text, or even saving the output to a file. This makes the information easy to understand and share.")
        st.write("Example: `print(\"The average temperature is:\", average_temp)` – this line displays a message with the average temperature.")
        st.write("Each of these parts works together in a Python script to achieve the final goal – whether that’s analyzing data, creating a web app, or generating visuals. The entire process runs from the top of the script to the bottom, following each step just like you would follow the steps in a recipe.")
        st.code("""
# 1. Importing Libraries
import pandas as pd  # This library helps manage and analyze data in tables
import matplotlib.pyplot as plt  # This library helps create visualizations like charts

# 2. Defining Variables
data = {'Temperature': [70, 75, 80, 85, 90], 'Humidity': [30, 45, 50, 60, 70]}  # Creating some sample data
city = "Kurdistan"  # Name of the location for the data

# 3. Creating a DataFrame (Data Table) and Calculating the Average Temperature
df = pd.DataFrame(data)  # Turning the data dictionary into a table
average_temp = df['Temperature'].mean()  # Calculating the average temperature

# 4. Loop through Data to Print Each Temperature
print(f"Weather data for {city}:")
for temp in df['Temperature']:
    print(f"- Temperature: {temp}°F")  # Prints each temperature on a new line

# 5. Visualize Data: Plotting Temperature and Humidity
plt.plot(df['Temperature'], label='Temperature', color='red')  # Plot temperature in red
plt.plot(df['Humidity'], label='Humidity', color='blue')  # Plot humidity in blue
plt.xlabel('Day')  # Label x-axis
plt.ylabel('Value')  # Label y-axis
plt.title(f"Weather Data for {city}")  # Title for the chart
plt.legend()  # Show legend to differentiate between temperature and humidity
plt.show()  # Display the chart

# 6. Output the Result
print(f"The average temperature in {city} is {average_temp}°F.")
""", language="python")

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
