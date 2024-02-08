import math
import streamlit as st
import pandas as pd
import numpy as np

class Budget():
    def __init__(self):
        self.value = 0
        self.initialBudget = 0
        self.totalIncome = []
        self.totalExpense = []
        self.categories = {}
    
    def create(self):
        no = int(input("How many categories are there? "))
        for i in range(0,no):
            try:
                temp = ["st","nd"]
                suffix = temp[i]
            except IndexError:
                suffix = "th"
            temp = input("What's the " + i + suffix+ " category?")
            temp2 = int(input("What "))

    def income(self, inputAmt,date,source,recurring=0):
        self.value += inputAmt
        self.totalIncome.append([inputAmt,date,source,recurring])
    
    def expense(self, expenseAmt,date,source):
        self.value -= expenseAmt
        self.totalExpense.append([expenseAmt,date,source])

    #def Generation():

new_budget = Budget()

def categoryPage():
    st.title("Categories")
    category_button = st.button("New Category")
    category = True
    if category_button and not category:
        category = True
    elif category_button and category:
        category = False
    if category:
        value = st.number_input(
            "Category value")
        name = st.text_input(
            "",
            label_visibility="collapsed",
            placeholder="Category name")
        if st.button("done"):
            new_budget.categories[name] = value
            category = False
    new_budget.categories
    st.table(pd.DataFrame(new_budget.categories))
    st.altair_chart()


# = Main code = 
# page selection
page = 0
st.sidebar.title("Budgeteer")
if st.sidebar.button("Categories"):
    page = 0
elif st.sidebar.button("Budget"):
    page = 1
# Run pages
if page == 0:
    categoryPage()

st.write()
    