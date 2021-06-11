import os
import psycopg2
from . import baseuuid

def uploadImg(nav_id,imgName,remark):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql = """INSERT INTO public.navigate_img_refs (id,nav_id,remark)
             VALUES(%s,%s,%s); """   
    record_to_insert = (imgName,nav_id,remark)
    print(record_to_insert)
    try:
        # print(sql)
        cursor.execute(sql,record_to_insert)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    #若無法連線，跑Error
    except:
        print ("Error: upload Img try")
    finally:
    # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def uploadCon(imgName,remark):
    id = f'{baseuuid.uudiv4()}'
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql = """INSERT INTO public.navigate_content_refs (id,nav_id,content)
             VALUES(%s,%s,%s); """   
    record_to_insert = (id,imgName,remark)
    print(record_to_insert)
    try:
        # print(sql)
        cursor.execute(sql,record_to_insert)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
    #若無法連線，跑Error
    except:
        print ("Error: upload Img try")
    finally:
    # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def uploadNav(sub_id,type_name,name,remark):
    id = f'{baseuuid.uudiv4()}'
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql = """INSERT INTO public.navigates (id,sub_id,type_name,name,remark)
             VALUES(%s,%s,%s,%s,%s); """   
    record_to_insert = (id,sub_id,type_name,name,remark)
    print(record_to_insert)
    try:
        # print(sql)
        cursor.execute(sql,record_to_insert)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
    #若無法連線，跑Error
    except:
        print ("Error: upload Nav try")
    finally:
    # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    x = uploadImg()
    print(x)
    for row in x:
        print(row)
