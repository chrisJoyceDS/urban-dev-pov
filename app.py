import streamlit as st
import pandas as pd
import pickle

# Set up the page
st.set_page_config(page_title="US Poverty Analysis", page_icon=":bar_chart:", layout="wide")


# Set up the sidebar
st.sidebar.title("Project Authors")
st.sidebar.info(
    "This application was created by [Adam Miner](https://github.com/minerad183), [Clayton Coffman](https://github.com/cmcoffman), and [Chris Joyce](https://github.com/chrisJoyceDS)."
)

st.sidebar.title("GitHub Repository")
st.sidebar.info(
    "[Link to the public GitHub repository](https://github.com/chrisJoyceDS/urban-dev-pov)."
)

# Load the data
# @st.cache
# def load_data():
#     return data

# data = load_data()

# Load the KMeans clustering model
# @st.cache(allow_output_mutation=True)
# def load_kmeans_model():
#     with open("path/to/kmeans_model.pkl", "rb") as f:
#         kmeans_model = pickle.load(f)
#     return kmeans_model

# kmeans_model = load_kmeans_model()

# Load the LinearRegression model
# @st.cache(allow_output_mutation=True)
# def load_linear_regression_model():
#     with open("path/to/linear_regression_model.pkl", "rb") as f:
#         linear_regression_model = pickle.load(f)
#     return linear_regression_model

# linear_regression_model = load_linear_regression_model()

# Define the function to make predictions using the models
def make_predictions(data, model):
    # Placeholder code to make predictions using the models
    pass
# Define the contents of the Homepage tab

def homepage_tab():
    st.title("Identifying poverty signals in cities across the US over time")
    st.write("Problem Statement:")
    st.write("""Poverty in the United States cannot be simply identified by tracking household income, it is not monolithic. Within each city, county, and state, poverty can take many forms and can overlap, from food access, to medical access, to effects on the environment. Therefore, to properly identify poverty in a cross-disciplinary matter, factors of poverty must be synthesized and analyzed together. 
This study attempts to create a profile of poverty in neighborhoods across the United States. Using socioeconomic data from the U.S. Census, and landcover data from the U.S. Geological Survey (USGS), and using an unsupervised learning process, we will cluster neighborhoods in U.S. cities into types of socioeconomic and environmental neighborhoods from the years 2000 to 2020. 
We will analyze any correlations between environmental factors and a socioeconomic indicator of poverty nationwide in an effort to interpret the impact of environmental factors on poverty. These results will be made available as a web application where users can interact and explore the relationships between these data points. """)

def visuals_tab():
    st.title("Visualizations go here!")

# Define the contents of the KMeans tab
def kmeans_tab():
    st.title("KMeans Clustering Model")
    st.write("This tab allows you to make predictions using the KMeans clustering model.")

    # User input
    st.sidebar.subheader("User Input Features")
    # Placeholder code for user input features

    # Prediction
    st.subheader("Prediction")
    # kmeans_prediction = make_predictions(census_data, kmeans_model)
    # st.write(kmeans_prediction)
    st.write("Predictions populate here!")

# Define the contents of the Linear Regression tab
def linear_regression_tab():
    st.title("Linear Regression Model")
    st.write("This tab allows you to make predictions using the Linear Regression model.")

    # User input
    st.sidebar.subheader("User Input Features")
    # Placeholder code for user input features

    # Prediction
    st.subheader("Prediction")
    # linear_regression_prediction = make_predictions(census_data, linear_regression_model)
    # st.write(linear_regression_prediction)
    st.write("Predictions populate here!")

# Create the tabs
tabs = {
    "Homepage": homepage_tab,
    "Visuals": visuals_tab,
    "KMeans Clustering": kmeans_tab,
    "Linear Regression": linear_regression_tab
}

# Render the tabs
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(tabs.keys()))
tab = tabs[selection]
tab()
