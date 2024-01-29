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

category = None

st.title("Budgeteer")

new_budget = Budget()
category
category_button = st.button("New Category")
if category_button and not category:
    category = True
else:
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

st.write()
    