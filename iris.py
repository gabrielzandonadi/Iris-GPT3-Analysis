import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load the Iris dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Create a basic layout for the app
st.title("Exploratory Data Analysis of Iris Dataset")
st.markdown("The Iris dataset is a collection of information about different types of flowers. Each flower is described by 4 different measurements: the length and width of the petals and the length and width of the sepals. These measurements are used to identify 3 different species of Iris flowers: setosa, versicolor, and virginica.")
st.markdown("This app allows you to explore the Iris dataset using various types of plots, summary statistics and correlation. You can select different options for the data visualization using the sidebar.")
st.markdown("To explore the data, select the options in the sidebar, and the corresponding plots, summary statistics and correlation will be displayed.")
st.sidebar.title("Iris Dataset EDA")

# Create a function to display basic statistics and information about the dataset
def show_dataset_info():
    st.write("**Shape:**")
    st.write(df.shape)
    st.write("**Columns:**")
    st.write(df.columns)
    st.write("**Head:**")
    st.write(df.head())
    st.write("**Description:**")
    st.write(df.describe())

# Create a function to visualize the data using different types of plots
def show_plots():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plot_type = st.sidebar.selectbox("Select a plot type", ["Histogram", "Scatter Plot", "Box Plot","Violin Plot"])
    if plot_type == "Histogram":
        st.write("Histogram")
        for col in df.columns[:-1]:
            st.write(f"Histogram of {col}")
            sns.histplot(data=df, x=col)
            st.pyplot()
    elif plot_type == "Scatter Plot":
        st.write("Scatter Plot")
        sns.scatterplot(x='sepal_length', y='sepal_width', hue='species',data=df)
        st.pyplot()
    elif plot_type == "Box Plot":
        st.write("Box Plot")
        sns.boxplot(data=df, x='species', y='petal_length')
        st.pyplot()
    elif plot_type == "Violin Plot":
        st.write("Violin Plot")
        sns.violinplot(x='species', y='petal_length', data=df)
        st.pyplot()

# Create a function to show the summary of the dataset
def show_summary():
    st.write("Summary of the dataset")
    st.write(df.describe())

# Create a function to show the description of the dataset
def show_description():
    st.write("Description of the dataset")
    st.write(df.describe(include='all'))

# Create a function to show the correlation of the dataset
def show_correlation():
    st.write("Correlation of the dataset")
    st.write(df.corr())
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot()

# Create a sidebar for selecting different types of plots and options for the data visualization
st.sidebar.subheader("Explore the Iris dataset")
dataset_info = st.sidebar.checkbox("Show dataset info")
if dataset_info:
    show_dataset_info()

plots = st.sidebar.checkbox("Show Plots")
if plots:
    show_plots()

summary = st.sidebar.checkbox("Show Summary")
if summary:
        show_summary()

description = st.sidebar.checkbox("Show Description")
if description:
    show_description()

correlation = st.sidebar.checkbox("Show Correlation")
if correlation:
    show_correlation()
