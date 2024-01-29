import math
import streamlit as st


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


st.title("Budgeteer")
new = Budget()
if st.button("New Category",type="primary"):
    st.write('why')
else:
    st.write("")
st.write()
    