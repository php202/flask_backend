import os
import psycopg2
import datetime
import re


def modCon(dics):
    for dic in dics:
        content =dics[dic]
        try:
            sql  = """  UPDATE public.navigate_content_refs SET content = %s , updated_at = %s WHERE deleted_at is null and id = %s  """
            # Print all rows
            # print(content,datetime.datetime.now(),dic)
            print(sql)
            mod_record=(content,f'{datetime.datetime.now()}',dic)
            conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
            cursor = conn.cursor()
            cursor.execute(sql,mod_record)
            print(mod_record)
            updated_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            print("Complete: modCon")
        #若無法連線，跑Error
        except:
            print("Error: modCon try")
        # Clean up

def modSch(dics):
    for dic in dics:
        content = dics[dic]
    try:
        conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        sql  = """  UPDATE public.schools SET content = %s , updated_at = %s WHERE deleted_at is null and id = %s  """
        print(sql)
        modrecord = (content,f'{datetime.datetime.now()}',dic)
        cursor.execute(sql,modrecord)
        conn.commit()
        cursor.close()
        conn.close()
        print("Complete: modSch")
    #若無法連線，跑Error
    except:
        print("Error: modCon try")
    # Clean up

def modImgre(imgName,remark):
    try:
        conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        sql  = """  UPDATE public.navigate_img_refs SET remark = %s , updated_at = %s WHERE deleted_at is null and id = %s  """
        print(sql)
        mod_Img_record = (remark,f'{datetime.datetime.now()}',imgName)
        cursor.execute(sql,(mod_Img_record))
        conn.commit()
        cursor.close()
        conn.close()
        print("Complete: modSch")
    #若無法連線，跑Error
    except:
        print("Error: modCon try")
    # Clean up

def modnews(dics):
    for dic in dics:
        content =dics[dic]
        if 'mai' == dic[:3]:
            dic = dic[3:]
            try:
                sql  = """  UPDATE public.navigate_img_refs SET remark = %s , updated_at = %s WHERE deleted_at is null and id = %s  """
                # Print all rows
                # print(content,datetime.datetime.now(),dic)
                print(sql)
                mod_record=(content,f'{datetime.datetime.now()}',dic)
                conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
                cursor = conn.cursor()
                cursor.execute(sql,mod_record)
                print(mod_record)
                updated_rows = cursor.rowcount
                conn.commit()
                cursor.close()
                conn.close()
                print("Complete: modmainews")
            #若無法連線，跑Error
            except:
                print("Error: modCon try")
            # Clean up
        else:
            dic = dic[3:]
            try:
                sql  = """  UPDATE public.navigate_content_refs SET content = %s , updated_at = %s WHERE deleted_at is null and id = %s  """
                # Print all rows
                # print(content,datetime.datetime.now(),dic)
                print(sql)
                mod_record=(content,f'{datetime.datetime.now()}',dic)
                conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
                cursor = conn.cursor()
                cursor.execute(sql,mod_record)
                print(mod_record)
                updated_rows = cursor.rowcount
                conn.commit()
                cursor.close()
                conn.close()
                print("Complete: modsubnews")
            #若無法連線，跑Error
            except:
                print("Error: modCon try")
            # Clean up

        

if __name__ == "__main__":
    x = modCon()
    print(x)