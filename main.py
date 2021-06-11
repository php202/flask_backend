from flask import Flask, request, abort, render_template, url_for, flash, redirect, make_response, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from custom_models import callDatabase,modDatabase,userDatabase,baseuuid,uploadDatabase
import configparser
import cv2
import time
from werkzeug.utils import secure_filename
import datetime
import os


app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
app.secret_key = config.get('flask', 'secret_key')

navigates=callDatabase.findNav()
schools = callDatabase.findSch()


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if 'imgtype' in request.form:
            nav_id = request.form['imgtype']
            imgName = f'{upload(request,"img")}'
            uploadDatabase.uploadImg(nav_id,imgName,"金榜")
        else:
            print(request.form)
            modDatabase.modCon(request.form)
        # 偷看一下 request.form 
    gold_imgs = callDatabase.findImg('62501555-302e-4aec-9798-d898f056cf1b')
    moreinfos = callDatabase.findImg('f485390a-0222-415c-8441-c95d7145c51a')
    super_golds = callDatabase.findImg('cff742dd-d41d-40c1-9d70-89da6a0a3113')[:2]
    main_contents = callDatabase.findCon('991d0a0a-e40f-45eb-93c5-d2d5ef024a5f')
    news = callDatabase.findImg('c7b30d63-ce7a-4d04-be13-71ff35f4fee1')
    youtube_links = callDatabase.findLink('d41d526e-39e0-4279-87f2-b729f06f31e0')
    youtube_contents = callDatabase.findCon('d41d526e-39e0-4279-87f2-b729f06f31e0')
    ideas = callDatabase.findCon('63e97e7f-2571-4cfc-bd0e-60c98565523c')
    return render_template("index.html",navs = navigates, schs = schools, golds = gold_imgs,moreinfo = moreinfos, sugo = super_golds, mains = main_contents, ytl = youtube_links, ytc = youtube_contents, ideas = ideas, news=news)

@app.route('/eLearning', methods=['POST', 'GET'])
def eLearning():
    nav_id ='177a30b4-cd8c-4c1d-8048-2fa8cfb06211'
    if request.method == 'POST':
        imgName = f'{upload(request,nav_id)}'
        uploadDatabase.uploadImg(nav_id,imgName,navigates[1][3])
    eLearns = callDatabase.findImg(nav_id)
    return render_template("eLearning.html",navs = navigates, schs = schools, eLearns = eLearns)
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # 偷看一下 request.form 
        # print(request.form)
        modDatabase.modCon(request.form)
    abouts = callDatabase.findCon('a08fd1fd-b4bb-4c68-9198-83a669a01994')
    main_contents = callDatabase.findCon('991d0a0a-e40f-45eb-93c5-d2d5ef024a5f')
    ideas = callDatabase.findCon('63e97e7f-2571-4cfc-bd0e-60c98565523c')
    schoolImgs = callDatabase.findImg("73390cd0-ad43-45cc-a4b4-194cafe0d33c")
    return render_template("about.html", navs = navigates, schs = schools, schImgs=schoolImgs, mains = main_contents, ideas = ideas, abouts = abouts)   
@app.route('/news', methods=['GET', 'POST'])
def news():
    nav_id = 'c7b30d63-ce7a-4d04-be13-71ff35f4fee1'
    if request.method == 'POST':
        mainnews = request.form['mainnews']
        subnews = request.form['subnews']
        imgName = f'{upload(request,nav_id)}'
        print(request.form)
        uploadDatabase.uploadImg(nav_id,imgName,navigates[2][3])
        modDatabase.modImgre(imgName,mainnews)
        uploadDatabase.uploadCon(imgName,subnews)
    news = callDatabase.findImg(nav_id)
    return render_template("news.html",navs = navigates, schs = schools, news = news)
@app.route('/news-detail', methods=['GET', 'POST'])
def detail():
    if request.method == 'POST':
        # 偷看一下 request.form 
        print(request.form)
        modDatabase.modnews(request.form)
    details = callDatabase.findDetail()
    return render_template("news-detail.html",navs = navigates, schs = schools, details = details)
@app.route('/class-A', methods=['GET', 'POST'])
def classA():
    if request.method == 'POST':
        if 'remark' in request.form:
            remark = request.form['remark']
            for key in request.files:
                nav_id = key
            imgName = f'{upload(request,nav_id)}'
            uploadDatabase.uploadImg(nav_id,imgName,remark)

        else:
            if 'schools' in request.form:
                sub_id = request.form['schools']
                name = request.form['course']
                uploadDatabase.uploadNav(sub_id,2,name,'高中家教班')
            elif 'courses' in request.form:
                sub_id = request.form['courses']
                name = request.form['subcourse']
                uploadDatabase.uploadNav(sub_id,3,name,'高中家教班')
            else:
                for key in request.form:
                    nav_id = key
                    remark = request.form[key]
                modDatabase.modImgre(nav_id,remark)

    sLists = callDatabase.findClassA()[0]
    dms = callDatabase.findClassA()[1]
    scLists = callDatabase.findClassA()[2]

    return render_template("class-A.html",navs = navigates, schs = schools,sLists = sLists,dms=dms,scLists=scLists)
@app.route('/class-B', methods=['GET', 'POST'])
def classB():
    if request.method == 'POST':
        if 'remark' in request.form:
            remark = request.form['remark']
            for key in request.files:
                nav_id = key
            imgName = f'{upload(request,nav_id)}'
            uploadDatabase.uploadImg(nav_id,imgName,remark)

        else:
            if 'schools' in request.form:
                sub_id = request.form['schools']
                name = request.form['course']
                uploadDatabase.uploadNav(sub_id,2,name,'高中重考班')
            elif 'courses' in request.form:
                sub_id = request.form['courses']
                name = request.form['subcourse']
                uploadDatabase.uploadNav(sub_id,3,name,'高中重考班')
            else:
                for key in request.form:
                    nav_id = key
                    remark = request.form[key]
                modDatabase.modImgre(nav_id,remark)
    sLists = callDatabase.findClassB()[0]
    dms = callDatabase.findClassB()[1]
    scLists = callDatabase.findClassB()[2]
    sch_ids = callDatabase.findClassB()[3]
    return render_template("class-B.html",navs = navigates, schs = sch_ids,sLists = sLists,dms=dms,scLists=scLists)
@app.route('/parent', methods=['POST', 'GET'])
def parents():
    nav_id ='0c212679-7830-4003-a6a4-482ee13263b8'
    if request.method == 'POST':
        imgName = f'{upload(request,nav_id)}'
        uploadDatabase.uploadImg(nav_id,imgName,navigates[7][3])
    parentImg = callDatabase.findImg(nav_id)
    return render_template("parent.html",navs = navigates, schs = schools, parentImg = parentImg)
@app.route('/school', methods=['GET', 'POST'])
def school():
    if request.method == 'POST':
        if 'imgtype' in request.form:
            remark = request.form['imgtype']
            nav_id = navigates[5][0]
            imgName = f'{upload(request,"img")}'
            uploadDatabase.uploadImg(nav_id,imgName,remark)

        else:
            modDatabase.modSch(request.form)
        
    schoolImgs = callDatabase.findImg("73390cd0-ad43-45cc-a4b4-194cafe0d33c")
    return render_template("school.html", navs = navigates, schs = schools, schImgs = schoolImgs) 

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        if 'imgtype' in request.form:
            t_name = request.form['teachername']
            t_remark = request.form['teachercontent']
            nav_id = request.form['imgtype']
            print(t_name,t_remark,nav_id)
            imgName = f'{upload(request,"img")}'
            uploadDatabase.uploadImg(nav_id,imgName,t_name)
            uploadDatabase.uploadCon(imgName,t_remark)
        else:
            modDatabase.modSch(request.form)
    tNavs = callDatabase.teacherNavs()[0]
    cNavs = callDatabase.teacherNavs()[1]
    subNavs = callDatabase.subNav('d507687e-91f8-409f-a151-8afd0ca8b048') 
    As = callDatabase.findCon('1cbddc0a-818b-4b6c-b069-5d662152b22b')
    Bs = callDatabase.findCon('53aacb2c-9f7f-4d0c-97d6-8b4c51d57f49')
    return render_template("teacher.html",navs = navigates, tNavs = tNavs, cNavs = cNavs, subNavs = subNavs, As = As , Bs = Bs) 

@app.errorhandler(404)
def page_not_found(e):
    return render_template("base.html")



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message = '請證明你並非來自黑暗草泥馬界'

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user_id):
    if user_id not in users:
        return

    user = User()
    user.id = user_id
    return user

@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    if user_id not in users:
        return

    user = User()
    user.id = user_id

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = baseuuid.uudiv5(request.form['password']) == users[user_id]['password']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html",navs = navigates, schs = schools)
    # print(request.form)
    user_id = request.form['user_id']
    password = request.form['password']
    users = userDatabase.finduser(user_id,password)
    if users != []:
        user = User()
        user.id = user_id
        login_user(user)
        flash(f'{users[0][0]}！歡迎進入管理員模式！')
        return redirect(url_for('about'))
    flash('登入失敗了...')
    return render_template('login.html',navs = navigates, schs = schools)

@app.route('/logout')
def logout():
    user_id = current_user.get_id()
    logout_user()
    flash(f'{user_id}！歡迎下次再來！')
    return render_template('login.html',navs = navigates, schs = schools)

# imgupload
app.send_file_max_age_default = datetime.timedelta(seconds=1)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp', 'jepg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST', 'GET'])  # 添加路由
def upload(request,nav_id):
    if request.method == 'POST':
        imgName = f'{baseuuid.uudiv4()}'
        f = request.files[nav_id] 
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": '請檢查上傳圖片類型，僅限於png、PNG、jpg、JPG、bmp'})
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        print(f.filename)
        upload_path = os.path.join(basepath, 'static/img', f'{imgName}.jpg',)  
        # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/img', imgName,'.jpg'), img)
        # return render_template('upload_ok.html',userinput=user_input,val1=time.time())
    return imgName


users = userDatabase.alluser()
# print(users)

if __name__ == '__main__':
 app.run(debug=True)