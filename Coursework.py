import math
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import data

#Pages
def categoryPage():
    st.title("Categories")
    category = True
    if category:
        data.totalIncome = st.number_input("Monthly Income")
        home_cost = st.number_input("Cost to mantain home")
        transportation_cost = st.number_input("Transportation cost")
        if st.button("done"):
            data.initialBudget = data.totalIncome - home_cost - transportation_cost
            data.budgetLeft = data.initialBudget
            "Initial Budget:", str(data.initialBudget).split(".")[0]
    if st.button("Reset Values"):
        data.value = 0
        data.initialBudget = 0
        data.budgetLeft = 0
        data.totalIncome = 0
        data.totalExpense = []
        data.budgetCost = []
        data.budgetName = []
        data.categories = []
        data.valueArray = []
        data.page_data = 0


def budgetPage():
    if data.initialBudget == 0:
        st.warning(":red[Please input a valid income]",icon="⚠️")
    else:
        if data.budgetLeft/data.initialBudget < (data.warning/100):
            st.warning(f"Budget left is less than {data.warning}% of total budget",icon="⚠️")
        st.title("Budget")
        "Initial Budget:", str(data.initialBudget).split(".")[0]
        "Budget Left:", str(data.budgetLeft).split(".")[0]
        budget_i = True
        if budget_i:
            budget_value = st.number_input("Budget value")
            budget_name = st.text_input("",label_visibility="collapsed",placeholder="Budget name")
            if st.button("done"):
                if budget_value == 0 or budget_name == "":
                    st.write(":red[Please input a valid value/name]")
                else:
                    data.budgetLeft -= budget_value
                    data.budgetCost.append(budget_value)
                    data.budgetName.append(budget_name)
        st.write(pd.DataFrame({
        'Budget Name': data.budgetName,
        'Budget Cost': data.budgetCost,
        }))

def settingsPage():
    st.title("Settings")
    data.warning = st.number_input("Percentage at which to display the warning at",placeholder = "30")
    if st.button("Reset Settings"):
        data.warning = 30
            


# = Main code = 
# Page selection
st.sidebar.title("Budgeteer")
page = data.page_data
if st.sidebar.button("Categories"):
    page = 0
    data.page_data = 0
if st.sidebar.button("Budget"):
    page = 1
    data.page_data = 1
if st.sidebar.button("Settings"):
    page = 2
    data.page_data = 2
# Run pages
if page == 0:
    categoryPage()
elif page == 1:
    budgetPage()
elif page == 2:
    settingsPage()
