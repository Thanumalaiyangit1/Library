from pymongo import MongoClient
import streamlit as st

c=MongoClient("mongodb+srv://Thanu:Thanu%401234@cluster0.oge2x.mongodb.net/")
db=c["libary"]
col=db["admin"]
col1=db["user"]
def display():
    a=col.find()
    for i in a:
        st.write(i)
def display1():
    a=col1.find()
    for i in a:
        st.write(i)
def insert():
    
    bn=st.text_input("Enter The Book Name :")
    ba=st.text_input("Enter The Author Name :")
    pr=st.number_input("Enter The Price :",min_value=100,max_value=1000)
    bi=st.number_input("Enter The Book Id :",min_value=0,max_value=1000)
    data={
        "book":bn,
        "author":ba,
        "price":pr,
        "book_id":bi
    }
    if(st.button("SUBMIT")):
        col.insert_one(data)
        col1.insert_one(data)
        st.success("Book Is Inserted Successfully")
def remove():
    a=st.number_input("Enter The Book Id",min_value=0,max_value=200)

    if(st.button("SUBMIT")):
        col.delete_one({"book_id":a})
        col1.delete_one({"book_id":a})
        st.success("Book Is Deleted Successfully")
def get():
    a=st.number_input("Enter The Book Id",min_value=0,max_value=200)
    c=col1.find_one({"book_id":a})
    d=st.button("get")
    if d==True:
        col1.delete_one(c)
        st.success("Taken Successfully")
     
def return1():
    try:
        n=st.number_input("Enter The Book-Id To Return",min_value=0,max_value=200)
        a=col.find({"book_id":n})
        b=col1.find({"book_id":n})
        if not (a==b):
            if(st.button("SUBMIT")):
                for i in a:
                    col1.insert_one(i)
                st.success("Book Returned")
    except:
        st.error("Invalid Book")
a=st.title("LIBRARY MANAGEMENT SYSTEM ")
p=st.sidebar.selectbox("INVENTORY",["SELECT","ADMIN","USER"])
if(p=="ADMIN"):
    c=st.sidebar.selectbox("SELECT",["SELECT","DISPLAY","INSERT","REMOVE",])
    if(c=="DISPLAY"):
        display()
    elif(c=="INSERT"):
        insert()
    elif(c=="REMOVE"):
        remove()
elif(p=="USER"):
    c=st.sidebar.selectbox("SELECT",["SELECT","DISPLAY","GET-BOOK","RETURN-BOOK",])
    if(c=="DISPLAY"):
        display1()
    elif(c=="GET-BOOK"):
        get()
    elif(c=="RETURN-BOOK"):
        return1()

