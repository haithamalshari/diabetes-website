from django.shortcuts import render
import xgboost as xgb
import pickle as pkl
import numpy as np
import os
from django.conf import settings
from Diabetes.models import Dataset

#model = open(os.path.join(settings.PROJECT_ROOT,'/static/models/xgb_model_web_xgb.dat'), 'rb')

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Create a Python file object using open()
# model_path = open(os.path.join(BASE_DIR,'/static/models/xgb_model_web_xgb.dat'), 'rb')

# Calculating BMI
def bmi_calc(w,h):
    h = h/100
    bmi = round(w/h**2,1)
    return bmi

# scaling
age_sc = {'mean': 47.56941366109208, 'std': 18.318893887483526}
bmi_sc = {'mean': 28.96734938545235, 'std': 6.804224456734176}
workout_sc = {'mean': 386.6755994358251, 'std': 455.9757722059645}

def scale(x,sc):
    y = (x-sc['mean']) / sc['std']
    return y

# One hot encoding
def feat_one_hot (en):
    from sklearn.preprocessing import OneHotEncoder
    const = en[:9]
    cat_v = [en[9:]]
    colls = [np.array(range(1,6)), np.array(range(1,8)),np.array(range(1,6)),
             np.array(range(0,4)),[0,1,2,5]]
    onehotencoder = OneHotEncoder(categories = colls)
    cat_var = onehotencoder.fit_transform(cat_v).toarray()    
    pro_entry = np.concatenate((const,cat_var[0] ))
    return pro_entry

# Data column names
col_names = ['Age','BMI','Workout_mins_in_a_week','Alcohol','Gender','Hypertension','Cholesterol','Sugar','Total_fat',
            'Race','Marital_status','EDUCATION_LEVEL','Smoking_Status','Pregnant','Diabetes']

# Create your views here.
def index(request):
    #print("request method : {}".format(request.method))
    return render (request , 'diabetes/index.html')

def index_ar(request):
    #print("request method : {}".format(request.method))
    return render (request , 'diabetes/index_ar.html')

def index_tr(request):
    #print("request method : {}".format(request.method))
    return render (request , 'diabetes/index_tr.html')

def diagnosis(request):
    # Load the model from file
    # print(settings.BASE_DIR)
    # print(os.path.join(settings.BASE_DIR,'xgb_model_web_xgb.dat'))
    model = open(os.path.join(os.path.join(settings.BASE_DIR,'xgb-hist_model_web.dat')), 'rb')
    #model_path = "/static/models/xgb_model_web_xgb.dat"
    # print('Site',site.directory)
    # print(fileobject.filename)
    # print(fileobject.path)
    classifier1 = pkl.load(model)
    if request.method == "POST":
        entry = request.POST
        age = scale(int(entry['age1']),age_sc)
        gender = int(entry['gender1'])
        race = int(entry['race1'])
        marital = int(entry['marital1'])
        edu = int(entry['edu1'])
        smoking = int(entry['smoking1'])
        bmi = scale(bmi_calc(int(entry['weight1']), int(entry['height1'])),bmi_sc)
        workout = scale(int(entry['workout1']),workout_sc)
        preg = 5 if gender == 0 else int(entry['preg1'])
        alcoho = int(entry['alcoho1'])
        bp = int(entry['bp1'])
        chol = int(entry['chol1'])
        suger = int(entry['suger1'])
        fat = int(entry['fat1'])
        entry_raw = [int(entry['age1']),bmi_calc(int(entry['weight1']), int(entry['height1'])),int(entry['workout1']),
                    int(entry['alcoho1']),int(entry['gender1']),int(entry['bp1']),int(entry['chol1']),int(entry['suger1']),
                    int(entry['fat1']),int(entry['race1']),int(entry['marital1']),int(entry['edu1']),int(entry['smoking1']),
                    preg,np.nan]
        request.session['data_col'] = [int(entry['age1']),
                                        bmi_calc(int(entry['weight1']), int(entry['height1'])),
                                        int(entry['workout1']),int(entry['alcoho1']),
                                        int(entry['gender1']),int(entry['bp1']),int(entry['chol1']),
                                        int(entry['suger1']),int(entry['fat1']),int(entry['race1']),
                                        int(entry['marital1']),int(entry['edu1']),int(entry['smoking1']),preg]
        processed_entry = [age,bmi,workout,alcoho,gender,bp,chol,suger,fat,race,marital,edu,smoking,preg]
        print(processed_entry)
        pro_entry = feat_one_hot(processed_entry)
        print("-------------------\n"*2)
        print(len(entry_raw))
        METS = ['Age','BMI','Workout_mins_in_a_week','Alcohol','Gender','Hypertension','Cholesterol','Sugar','Total_fat',
            'Race','Marital_status','EDUCATION_LEVEL','Smoking_Status','Pregnant','Diabetes']
        for i, j in zip(METS,entry_raw):
            print('{:<25} : {:.4f}'.format(i,j))
        pred = 'Diabetes-Free' if classifier1.predict([pro_entry])[0] == 0 else 'Diabetic'
        request.session['pred'] = int(classifier1.predict([pro_entry])[0])
        predprob = round(classifier1.predict_proba([pro_entry])[0,1]*100,2)
        result = {'pred':pred , 'predprob':predprob }
    #result = "Yes"
    return render (request , 'diabetes/result.html',{
        "result": result
    })

def diagnosis_ar(request):
    # Load the model from file
    # print(settings.BASE_DIR)
    # print(os.path.join(settings.BASE_DIR,'xgb_model_web_xgb.dat'))
    model = open(os.path.join(os.path.join(settings.BASE_DIR,'xgb-hist_model_web.dat')), 'rb')
    #model_path = "/static/models/xgb_model_web_xgb.dat"
    # print('Site',site.directory)
    # print(fileobject.filename)
    # print(fileobject.path)
    classifier1 = pkl.load(model)
    if request.method == "POST":
        entry = request.POST
        age = scale(int(entry['age1']),age_sc)
        gender = int(entry['gender1'])
        race = int(entry['race1'])
        marital = int(entry['marital1'])
        edu = int(entry['edu1'])
        smoking = int(entry['smoking1'])
        bmi = scale(bmi_calc(int(entry['weight1']), int(entry['height1'])),bmi_sc)
        workout = scale(int(entry['workout1']),workout_sc)
        preg = 5 if gender == 0 else int(entry['preg1'])
        alcoho = int(entry['alcoho1'])
        bp = int(entry['bp1'])
        chol = int(entry['chol1'])
        suger = int(entry['suger1'])
        fat = int(entry['fat1'])
        entry_raw = [age,bmi_calc(int(entry['weight1']), int(entry['height1'])),int(entry['workout1']),
                    alcoho,gender,chol,suger,fat,race,marital,edu,smoking,preg,np.nan]
        request.session['data_col'] = [int(entry['age1']),
                                        bmi_calc(int(entry['weight1']), int(entry['height1'])),
                                        int(entry['workout1']),int(entry['alcoho1']),
                                        int(entry['gender1']),int(entry['bp1']),int(entry['chol1']),
                                        int(entry['suger1']),int(entry['fat1']),int(entry['race1']),
                                        int(entry['marital1']),int(entry['edu1']),int(entry['smoking1']),preg]
        processed_entry = [age,bmi,workout,alcoho,gender,bp,chol,suger,fat,race,marital,edu,smoking,preg]
        print(processed_entry)
        pro_entry = feat_one_hot(processed_entry)
        print("-------------------\n")
        print(pro_entry)
        pred = 'خالي من السكري' if classifier1.predict([pro_entry])[0] == 0 else 'مصاب بالسكري'
        request.session['pred'] = int(classifier1.predict([pro_entry])[0])
        predprob = round(classifier1.predict_proba([pro_entry])[0,1]*100,2)
        result = {'pred':pred , 'predprob':predprob }
    #result = "Yes"
    return render (request , 'diabetes/result_ar.html',{
        "result": result
    })

def diagnosis_tr(request):
    # Load the model from file
    # print(settings.BASE_DIR)
    # print(os.path.join(settings.BASE_DIR,'xgb_model_web_xgb.dat'))
    model = open(os.path.join(os.path.join(settings.BASE_DIR,'xgb-hist_model_web.dat')), 'rb')
    #model_path = "/static/models/xgb_model_web_xgb.dat"
    # print('Site',site.directory)
    # print(fileobject.filename)
    # print(fileobject.path)
    classifier1 = pkl.load(model)
    if request.method == "POST":
        entry = request.POST
        age = scale(int(entry['age1']),age_sc)
        gender = int(entry['gender1'])
        race = int(entry['race1'])
        marital = int(entry['marital1'])
        edu = int(entry['edu1'])
        smoking = int(entry['smoking1'])
        bmi = scale(bmi_calc(int(entry['weight1']), int(entry['height1'])),bmi_sc)
        workout = scale(int(entry['workout1']),workout_sc)
        preg = 5 if gender == 0 else int(entry['preg1'])
        alcoho = int(entry['alcoho1'])
        bp = int(entry['bp1'])
        chol = int(entry['chol1'])
        suger = int(entry['suger1'])
        fat = int(entry['fat1'])
        entry_raw = [int(entry['age1']),bmi_calc(int(entry['weight1']), int(entry['height1'])),int(entry['workout1']),
                    alcoho,gender,chol,suger,fat,race,marital,edu,smoking,preg,np.nan]
        request.session['data_col'] = [int(entry['age1']),
                                        bmi_calc(int(entry['weight1']), int(entry['height1'])),
                                        int(entry['workout1']),int(entry['alcoho1']),
                                        int(entry['gender1']),int(entry['bp1']),int(entry['chol1']),
                                        int(entry['suger1']),int(entry['fat1']),int(entry['race1']),
                                        int(entry['marital1']),int(entry['edu1']),int(entry['smoking1']),preg]
        processed_entry = [age,bmi,workout,alcoho,gender,bp,chol,suger,fat,race,marital,edu,smoking,preg]
        print(processed_entry)
        pro_entry = feat_one_hot(processed_entry)
        print("-------------------\n")
        print(pro_entry)
        pred = 'Diyabetik DEĞIL' if classifier1.predict([pro_entry])[0] == 0 else 'Diyabetik'
        request.session['pred'] = int(classifier1.predict([pro_entry])[0])
        predprob = round(classifier1.predict_proba([pro_entry])[0,1]*100,2)
        result = {'pred':pred , 'predprob':predprob }
    #result = "Yes"
    return render (request , 'diabetes/result_tr.html',{
        "result": result
    })

def feed(request):
    feats = request.session.get('data_col')
    pred = request.session.get('pred')
    feed = int(request.POST['feed'])
    feats.append(pred)
    feats.append(feed)
    data = Dataset(age = feats[0],
                bmi = feats[1],
                wrkout = feats[2],
                alcol = feats[3],
                gender = feats[4],
                bp = feats[5],
                chol = feats[6],
                suger = feats[7],
                fat = feats[8],
                race = feats[9],
                marital = feats[10],
                edu = feats[11],
                smoke = feats[12],
                preg = feats[13],
                pred = feats[14],
                feed = feats[15])
    data.save()
    return render (request , 'diabetes/feed.html')

def feed_ar(request):
    feats = request.session.get('data_col')
    pred = request.session.get('pred')
    feed = int(request.POST['feed'])
    feats.append(pred)
    feats.append(feed)
    data = Dataset(age = feats[0],
                bmi = feats[1],
                wrkout = feats[2],
                alcol = feats[3],
                gender = feats[4],
                bp = feats[5],
                chol = feats[6],
                suger = feats[7],
                fat = feats[8],
                race = feats[9],
                marital = feats[10],
                edu = feats[11],
                smoke = feats[12],
                preg = feats[13],
                pred = feats[14],
                feed = feats[15])
    data.save()
    return render (request , 'diabetes/feed_ar.html')

def feed_tr(request):
    feats = request.session.get('data_col')
    pred = request.session.get('pred')
    feed = int(request.POST['feed'])
    feats.append(pred)
    feats.append(feed)
    data = Dataset(age = feats[0],
                bmi = feats[1],
                wrkout = feats[2],
                alcol = feats[3],
                gender = feats[4],
                bp = feats[5],
                chol = feats[6],
                suger = feats[7],
                fat = feats[8],
                race = feats[9],
                marital = feats[10],
                edu = feats[11],
                smoke = feats[12],
                preg = feats[13],
                pred = feats[14],
                feed = feats[15])
    data.save()
    return render (request , 'diabetes/feed_tr.html')