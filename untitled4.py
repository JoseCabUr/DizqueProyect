# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:58:07 2023

@author: Alumno
"""

#show tables: SQL Show Tables: List All Tables in a Database - Database Star
import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql

import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta


################ MySQL ###################
database = 'empresa'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method

def consulta():
    consulta = " SELECT departamento FROM empleado "
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    #df["salario$"]= df.salario.map(lambda x: str(x) + "$")
    print("type(df)=", type(df))
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(10)=",df.head(10))
    print("df.tail(10)=",df.tail(10))
    print("df.sample(20)=",df.sample(20))
    #df_nuevo= df.nombre.map(lambda x: str.upper(x))
    print("df_nuevo.head(10)=",df_nuevo.head(10))
    #df2_nuevo=df.salario.map(lambda x: x*1.07)
    print("df_nuevo.head(10)=",df2_nuevo.head(10))
    #df ["salario$"] = df.salario.map(lambda x: x*1.07)
    print("df.head(10)=",df.head(10))
    
consulta()

