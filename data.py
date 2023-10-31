# Define a function 'app()' which accepts 'car_df' as an input.
import streamlit as st
def app(cars_df):
  st.header("View Data")
  st.table(cars_df)
  # st.header("View Data")
  # with st.beta_expander("View DataSet"):
  #   st.table(cars_df)

  # st.subheader("Columns Description:")
  # if st.checkbox("Show summary"):
  #   st.table(cars_df.describe())  


  # beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
  # with beta_col1:
  #   if st.checkbox("Show all column names"):
  #     st.table(list(cars_df.columns))
  # with beta_col2:
  #   if st.checkbox("View Column Data-Types"):
  #     st.table(cars_df.astype(str))

  # with beta_col3:
  #   if st.checkbox("View Column Data"):
  #     column_data = st.selectbox('Select column', tuple(cars_df.columns))
  #     st.write(cars_df[column_data])
