import pandas as pd
import json
import pyodbc
import pymysql
import cx_Oracle

class SrcToDataframe:
    """This class contains list of functions which receives source file path as input and
        Returns dataframe as output"""

    def load_netezza_data(sourcefile_path):
        """This function receives absolute file path of a sql stored in txt,
        establishes the connection using pyodbc.connect, user to give necessary connection details
        Extracts data using pd.read_sql_query.
        Returns sql result as data frame.
        """
        conn = pyodbc.connect(
            "DRIVER={NetezzaSQL};SERVER=192.168.0.10; PORT=5480;DATABASE=TESTDB; UID=admin;PWD=password;")
        with open(sourcefile_path) as text:
            sql_query = text.read()
        sql_data = pd.read_sql_query(sql_query, conn)
        return sql_data

    def load_sqlserver_data(sourcefile_path):
        """This function receives absolute file path of a sql stored in txt,
        establishes the connection using pyodbc.connect, user to give necessary connection details
        Extracts data using pd.read_sql_query.
        Returns sql result as data frame.
        """
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")
        with open(sourcefile_path) as text:
            sql_query = text.read()
        sql_data = pd.read_sql_query(sql_query, conn)
        return sql_data

    def load_mysql_data(sourcefile_path):
        """This function receives absolute file path of a sql stored in txt,
        establishes the connection using pymysql.connect, user to give necessary connection details
        Extracts data using pd.read_sql_query.
        Returns sql result as data frame.
        """
        conn = pymysql.connect(host='localhost', user='root', passwd='1q2w3e4r', db='test_database')
        with open(sourcefile_path) as text:
            sql_query = text.read()
        sql_data = pd.read_sql_query(sql_query, conn)
        return sql_data

    def load_msaccess_data(sourcefile_path):
        """This function receives absolute file path of a sql stored in txt,
        establishes the connection using pyodbc.connect, user to give necessary connection details
        Extracts data using pd.read_sql_query.
        Returns sql result as data frame.
        """
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ron\Desktop\testdb.accdb;')
        with open(sourcefile_path) as text:
            sql_query = text.read()
        sql_data = pd.read_sql_query(sql_query, conn)
        return sql_data

    def load_oracle_data(sourcefile_path):
        """This function receives absolute file path of a sql stored in txt,
        establishes the connection using cx_Oracle.connect, user to give necessary connection details
        Extracts data using pd.read_sql_query.
        Returns sql result as data frame.
        """
        dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number',
                                    service_name='Service Name')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
        conn = cx_Oracle.connect(user=r'User Name', password='Personal Password',
                                 dsn=dsn_tns)  # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
        with open(sourcefile_path) as text:
            sql_query = text.read()
        sql_data = pd.read_sql_query(sql_query, conn)
        return sql_data



