import os
import psycopg2
from . import baseuuid

def finduser(account,password):
    password = baseuuid.uudiv5(password)
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT name FROM public.users WHERE account =\'{}\' and password=\'{}\' and deleted_at is null order by created_at asc""".format(account,password)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: user row try")
        rowcount = []
    # Clean up
    return results


def alluser():
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT account,name,password FROM public.users WHERE deleted_at is null order by created_at asc"""
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        users = {}
        for row in results:
            user_account = row[0]
            user_name = row[1]     
            user_password = row[2]
            users[user_account] = {'name':user_name,'password':user_password}
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: user row try")
        users = {}
    # Clean up
    return users

if __name__ == "__main__":
    x = alluser()
    print(x)
    for row in x:
        print(row)
