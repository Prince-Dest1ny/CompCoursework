import math
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import time

'''
class Budget():
    def __init__(self):
        self.value = 0
        self.initialBudget = 0
        self.totalIncome = []
        self.totalExpense = []
        self.budgetCost = []
        self.budgetName = []
        self.categories = []
        self.valueArray = []
    
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
'''


def categoryPage():
    categories1 = []
    value1 = []
    st.title("Categories")
    category_button = st.button("New Category")
    category = True
#    if category_button and not category:
#        category = True
#    elif category_button and category:
#        category = False
    if category:
        value = st.number_input("Category value")
        name = st.text_input("",label_visibility="collapsed",placeholder="Category name")
        if st.button("done"):
            categories1.append(name)
            value1.append(value)
            #new_budget.categories.append(name)
            #new_budget.valueArray.append(value)
            #new_budget.income(value, date.today(), name)
    
     
    st.write(pd.DataFrame({
    'Category Name': categories1,
    'Category Value': value1,
    }))
    #new_budget.categories
    #new_budget.initialBudget
    #new_budget.totalIncome
    #new_budget.totalExpense
    #st.table(pd.DataFrame(data=new_budget.categories, index = [name], columns=5)
    #st.table(pd.DataFrame(Budget.totalIncome, columns=("col %d" % i for i in range(5))))
    
    #st.altair_chart()

def budgetPage():
    st.title("Budget")
    budget_button = st.button("New Budget")
    budget_i = True
    if budget_button and not budget_i:
        budget_i = True
    elif budget_button and budget_i:
        budget_i = False
    if budget_i:
        budget_value = st.number_input("Budget value")
        budget_name = st.text_input("",label_visibility="collapsed",placeholder="Budget name")
        if st.button("done"):
            new_budget.budgetCost.append(budget_value)
            new_budget.budgetName.append(budget_name)
            budget_i = False
    
    st.write(pd.DataFrame({
    'Budget Name': new_budget.budgetName,
    'Budget Cost': new_budget.budgetCost,
}))



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
elif page == 1:
    budgetPage()

    
