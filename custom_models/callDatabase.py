import os
import psycopg2
import datetime


def findNav():
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigates WHERE deleted_at is null and type_name = 1 order by created_at asc"""
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Nav row try")
    # Clean up
    return results

def subNav(sub_id):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigates WHERE deleted_at is null and sub_id ='{}' order by created_at asc""".format(sub_id)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Nav row try")
    # Clean up
    return results

def findSch():
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.schools WHERE deleted_at is null order by created_at asc"""
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Nav row try")
    # Clean up
    return results            
        
def findImg(nav_id):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigate_img_refs WHERE deleted_at is null and nav_id = '{}' order by created_at desc""".format(nav_id)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        result_imgs = cursor.fetchall()
        # print(result_imgs)
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Img row try")
    # Clean up
    return result_imgs

def findSchImg():
    for school in findSch():
        schImgs = findImg(school[0])
        
        for schImg in schImgs:
            print(schImg[1],schImg[3])

def findCon(nav_id):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigate_content_refs WHERE deleted_at is null and nav_id = '{}' order by created_at asc""".format(nav_id)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        result_contents = cursor.fetchall()
        # print(result_imgs)
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Img row try")
    # Clean up
    return result_contents

def findLink(nav_id):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigate_link_refs WHERE deleted_at is null and nav_id = '{}' order by created_at asc""".format(nav_id)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        result_links = cursor.fetchall()
        # print(result_imgs)
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Img row try")
    # Clean up
    return result_links

def findDetail():
    nav_id ='c7b30d63-ce7a-4d04-be13-71ff35f4fee1'
    newsImg = findImg(nav_id)
    kList = {}
    for row in newsImg:
        vList = []
        new_id = row[0]
        new_top = row[3]
        vList.append(new_top)
        creatTime=f"{row[4]}"[:10]
        vList.append(creatTime)
        new_com = findCon(row[0])
        if new_com:
            comment_id = new_com[0][0]
            comment = new_com[0][2]
            new_com = comment
        else:
            comment = ''
        vList.append(comment)
        vList.append(comment_id)
        kList[new_id]=vList        
    return kList

def teacherNavs():
    nav_id = "d507687e-91f8-409f-a151-8afd0ca8b048"
    cList = {}
    tList = {}
    for row in subNav(nav_id):
        sub_id = row[0]
        sub_name = row[3]

        for row in subNav(sub_id):
            cou_id = row[0]
            cou_name = row[3]
            cList[cou_id]=(sub_id,sub_name,cou_id,cou_name)
            for row in findImg(cou_id):
                tea_id = row[0]
                tea_remark = row[2]
                tea_name = row[3]
                tea_comment=findCon(tea_id)[0][2]
                # print(cou_id,tea_id,tea_name,tea_comment)
                tList[tea_id]=(cou_id,cou_name,tea_id,tea_name,tea_comment,tea_remark)
                
    return tList,cList

def findClassA():
    sch_ids = findSch()
    sList={}
    scList={}
    for sch in sch_ids:
        sch_id = sch[0]
        courses = subcourseA(sch_id,'高中家教班')
        clist=[]
        if courses:
            for course in courses:
                course_id = course[0]
                course_name = course[3]
                clist.append(course_id)
                sList[course_id] = {'sch_id':sch_id,'course_name':course_name,'course_id':course_id}
                subCous = subcourseA(course_id,'高中家教班')
                subList = {}
                for subCou in subCous:
                    subCou_id = subCou[0]
                    subCou_name = subCou[3]
                    subList[subCou_id]=subCou_name
                    # print(subCou)
                sList[course_id]['subCou_id']=subList
            scList[sch_id]=clist
    dm = {}
    for c_key in sList:
        sch_id = sList[c_key]['sch_id']
        course_id = c_key
        course_name = sList[c_key]['course_name']
        subclist = sList[c_key]['subCou_id']
        for sub_id in subclist:
            subImg = findImg(sub_id)
            if subImg:
                dmImg = subImg[0][0]
                dmCon = subImg[0][3]
                dm[sub_id]={'dm_id':dmImg,'dm_con':dmCon}
    return sList,dm,scList

def subcourseA(sub_id,remark):
    conn = psycopg2.connect(database="dasyuemen", user="yutsunghan", password="doit", host="127.0.0.1", port="5432")
    # print("Connection established")
    cursor = conn.cursor()
    # Fetch all rows from table
    sql  = """  SELECT * FROM public.navigates WHERE deleted_at is null and sub_id =\'{}\' and remark =\'{}\' order by created_at asc""".format(sub_id,remark)
    # Print all rows
    try:
        # print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
    #若無法連線，跑Error
    except:
        print ("Error: Nav row try")
    # Clean up
    return results

def findClassB():
    sch_ids = [('7b2a4ccd-74a1-4242-8327-76b64a0227e2', '育才班', '(04)22216277', '', '台中市北區尊賢街9號3樓(水利大樓3樓)', '全新舒適的環境設備/坐一空一的寬廣坐位/一對一的家教式課輔/唯一獨家診斷式教學/最專業的重考班師資/安全舒適的學生宿舍/最完整的二階段', 'https://www.facebook.com/%E5%A4%A7%E5%AD%B8%E9%96%80%E6%95%99%E8%82%B2%E4%BA%8B%E6%A5%AD%E9%AB%94%E7%B3%BB-%E8%82%B2%E6%89%8D%E7%8F%AD-105336791108002', None, datetime.datetime(2021, 6, 6, 14, 1, 27, 281586, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=480, name=None)), datetime.datetime(2021, 6, 10, 0, 41, 9, 593982, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=480, name=None)), None)]
    # print(sch_ids)
    sList={}
    scList={}
    for sch in sch_ids:
        sch_id = sch[0]
        courses = subcourseA(sch_id,'高中重考班')
        clist=[]
        if courses:
            for course in courses:
                course_id = course[0]
                course_name = course[3]
                clist.append(course_id)
                sList[course_id] = {'sch_id':sch_id,'course_name':course_name,'course_id':course_id}
                subCous = subcourseA(course_id,'高中重考班')
                subList = {}
                for subCou in subCous:
                    subCou_id = subCou[0]
                    subCou_name = subCou[3]
                    subList[subCou_id]=subCou_name
                    # print(subCou)
                sList[course_id]['subCou_id']=subList
            scList[sch_id]=clist
    dm = {}
    for c_key in sList:
        sch_id = sList[c_key]['sch_id']
        course_id = c_key
        course_name = sList[c_key]['course_name']
        subclist = sList[c_key]['subCou_id']
        for sub_id in subclist:
            subImg = findImg(sub_id)
            if subImg:
                dmImg = subImg[0][0]
                dmCon = subImg[0][3]
                dm[sub_id]={'dm_id':dmImg,'dm_con':dmCon}
    return sList,dm,scList,sch_ids

if __name__ == "__main__":
    x = findClassB()
    print(x)
