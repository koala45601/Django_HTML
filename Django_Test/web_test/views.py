from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.files.storage import FileSystemStorage

@login_required

# Create your views here.
def homepage(request):
# Show Progrm HelloWorld for Test Web Connect
#    return HttpResponse('<h1>Hello Kung Duangporn1</h1>')
# show index.html
    return render(request,'index.html')
@login_required
def Login_page(request):
    return render(request,'temp_login.html')

@login_required
def addstock(request):
    if request.method == 'POST':
        data = request.POST.copy() 
        form = imgfrom(request.POST, request.FILES) 
        name = data.get('s_name')
        stock_id = data.get('s_id')
        category_1 = data.get('Cat')
        score_1 = data.get('s_count')
        remark_1 = data.get('rem_1')
        file = data.get('myfile')

        newstock = Stock_Me()
        newstock.Stock_name = name
        newstock.Stock_ID = stock_id
        newstock.category = category_1
        newstock.socrce = score_1
        newstock.Stock_remark = remark_1
        
        newstock.save()
        

        return redirect('show-stock')

    return render(request,'page1.html')


def register(request):
    if request.method == 'POST':
        data_1 = request.POST.copy()
        Password_1 = data_1.get('Password_1')
        email = data_1.get('Email')
        name_1 = data_1.get('name_1')
        lastname_1 = data_1.get('lastname_1')

        newuser = User()
        newuser.username = email
        newuser.first_name = name_1
        newuser.last_name = lastname_1
        newuser.email = email
        newuser.set_password(Password_1)
        newuser.save()

        return redirect('home-page')
    return render(request, 'Login.html')

@login_required
def show_stock(request):
    Stock_show = Stock_Me.objects.all() #ดีวค่าจาก DB ทั้งหมด
    con_1 = {'Stock_show':Stock_show} 
    return render(request,'Stock.html',con_1)

@login_required
#seach data
def search_1(request):
    #MODESLS.object.all() ดึงค่า All
    #models.object.get(Stock_ID=1) ดึงค่าแค่ตัวเดียวหากเกินจะ Error 
    #MODELS.objects.filter(Stock_name='Pock Meet') ดึงค่า หลายค่า >1
    #show_1 = Stock_Me.objects.get(Stock_ID=)
    if request.method == 'POST':
        data = request.POST.copy() #ดึงค่าจาก input ใน HTML
        search_id = int(data.get('search')) 
        print(search_id, type(search_id))

        try:
            result = Stock_Me.objects.get(Stock_ID=search_id)
            print('RESULE : ',str(result))
            context = {'result':result,'check':'Found'}
        except:
            context = {'result':'Cant not find ID','check':'Not Found'}
        return render(request, 'search.html',context)

    return render(request, 'search.html')

@login_required
def EditProfile(request):
    username = request.user.username
    current = User.objects.get(username=username)
    if request.method == 'POST' and request.FILES['image_1']:
        data_1 = request.POST.copy()
        #Password_1 = data_1.get('Password_1')
        email = data_1.get('email')
        name_1 = data_1.get('name_1')
        lastname_1 = data_1.get('lastname_1')

        edituser = User.objects.get(username=username)
        try:
            setprofile = profile.objects.get(user=edituser)
        
        except:
            setprofile = profile()
            setprofile.user = edituser

        ############## File System #######################
        file_img = request.FILES['image_1']
        file_img_name = file_img.name
        fs = FileSystemStorage()
        filename = fs.save(file_img_name,file_img)
        uoload_file = fs.url(filename)
        # 6: คือใช้ชื่อไฟล์ตั้งแต่ตัวอักษรที่ 6 ปัจจุบมัรที่ต้องใช้แบบนี้เพราะมันใช้ : /media/682.jpg  ตัดให้เหลือ /image.png
        setprofile.img_profile = uoload_file[6:]
        setprofile.save()

        ############## File System #######################

        edituser.username = email
        edituser.first_name = name_1
        edituser.last_name = lastname_1
        edituser.email = email
        #edituser.set_password(Password_1)
        edituser.save()
        
        return redirect('profile')
    
    context = {'data':current}
    return render(request, 'profile.html',context)

def doc_upload(request):
    
    if request.method == 'POST' and request.FILES['doc_up_1']:
        data = request.POST.copy()
        doc_name = data.get('doc_name')
        doc_date = data.get('doc_date')
        
        
        upload_file = upload_document()
        upload_file.userlevel = 'Admin'
        upload_file.document_name = doc_name
        upload_file.start_date = doc_date
        file_doc = request.FILES['doc_up_1']
        file_doc_name = file_doc.name
        fs = FileSystemStorage()
        file_doc_1 = fs.save(file_doc,file_doc_name)
        file_doc_2 = fs.url(file_doc_1)
        upload_file.document_up = file_doc_2[6:]
        upload_file.save()

        return redirect('doc_up_load')
    return render(request, 'upload_doc.html')