import math
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import data
import time

    
    

#Home page
#declan's code
def homePage():
    st.markdown("# :rainbow[Budgeteer]")
    with st.form("Home"):
        category = True
        if category:
            data.totalIncome = st.number_input("Monthly Income ($)")
            home_cost = st.number_input("Cost to maintain home ($)")
            transportation_cost = st.number_input("Transportation cost ($)")
            savings = st.number_input("Percentage of salary you wish to save (%):")
            if st.form_submit_button("done"):
                #ethan's code
                if data.totalIncome - home_cost - transportation_cost - (data.totalIncome*(savings/100)) < 0:
                    st.write(":red[You may have keyed in one or more variable wrongly! Please re-key in your values.]")
                else:
                    data.initialBudget = data.totalIncome - home_cost - transportation_cost - (data.totalIncome*(savings/100))
                    data.savings = data.totalIncome * (savings/100)
                    data.budgetLeft = data.initialBudget
                    st.session_state.initialBudget = data.initialBudget
                    st.session_state.budgetLeft = data.budgetLeft
                    "Initial Budget: $", str(data.initialBudget)
                    "Savings: $", str(data.savings)

#Budget page
#Declan's code
def budgetPage():
    if 'debt' not in st.session_state:
        st.session_state.debt = 0
    if 'initialBudget' not in st.session_state:
        st.session_state.initialBudget = data.initialBudget
    if 'budgetLeft' not in st.session_state:
        st.session_state.budgetLeft = data.budgetLeft
    if 'budgetValue' not in st.session_state:
        st.session_state.budgetValue = 0
    if data.initialBudget == 0:
        st.warning("Please fix your budget inputs :3",icon="⚠️")
    else:
        if st.session_state.budgetLeft - st.session_state.budgetValue >= 0:
            st.session_state.budgetLeft -= st.session_state.budgetValue
        else:
            st.session_state.debt += st.session_state.budgetValue - st.session_state.budgetLeft
        if st.session_state.budgetLeft/st.session_state.initialBudget < (data.warning/100):
            st.warning(f"Budget left is less than {data.warning}% of total budget",icon="⚠️")
        #ethan's code
        st.title("Budget")
        "Initial Budget:", str(data.initialBudget)
        "Budget Left:", str(st.session_state.budgetLeft)
        "Debt: $", str(st.session_state.debt)
        budget_i = True
        if budget_i:
            #declan's code
            def budgetButtonCallback():
                if st.session_state.budgetLeft == 0:
                    st.warning("Budget left has reached 0!")
                if st.session_state.budgetValue <= 0 or st.session_state.budgetName == "":
                    st.write(":red[Please input a valid value/name]")
                    return
                if st.session_state.budgetLeft >= 0:
                    data.budgetCost.append(budget_value)
                    data.budgetName.append(budget_name)
                    return
                if st.session_state.budgetLeft < 0:
                    st.warning("Amount inputted has exceeded budget!")
                    return
            with st.form("budget_form"):
                budget_name = st.text_input("",label_visibility="collapsed",placeholder="Expenditure name",key='budgetName')
                budget_value = st.number_input("Expenditure value", key='budgetValue')
                submit = st.form_submit_button('Done', on_click=budgetButtonCallback())

        st.write(pd.DataFrame({
        'Expenditure Name': data.budgetName,
        'Expenditure Cost': data.budgetCost,
        }))
        
#base values before starting
#matthias + declan's code
def settingsPage():
    st.title("Settings")
    data.warning = st.number_input("Percentage at which to display the warning at",value = data.warning)
    if st.button("Reset Settings"):
        data.warning = 30
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
        data.budgetValue = 0
        


invalid_value = ""
budget_value = 0

# Page selection
#matthias's code
st.sidebar.title("Budgeteer")
page = data.page_data
if st.sidebar.button("Home"):
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
    homePage()
elif page == 1:
    budgetPage()
elif page == 2:
    settingsPage()
