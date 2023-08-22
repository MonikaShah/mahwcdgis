from django.shortcuts import render
from .models import RuralInfraAwcAcEnglishconverted, WomenStateHome, OneStopCenter, CounsellingCentresJuly23, SwadhaarGreh, UjjwalGrehJuly23, MhPoliceStations, CCI7July23,Wwh
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.contrib.gis.db import models



# Create your views here.
def homePage(request):
    return render(request, 'viewHome.html')

def ga(request):
    return render(request, 'ga.html')

@csrf_exempt
def viewMap(request):
    if request.method == "POST":
        dist = request.POST.get('district')
        taluka = request.POST.get('taluka')
        # angan_type = request.POST.get('agan_type')
        # constr = request.POST.get('constr')
        # sitangan = request.POST.get('sitangan')
        # cate1 = request.POST.get('cate1')
        # cate2 = request.POST.get('cate2')
        # cate3 = request.POST.get('cate3')
        
        # cate_val1 = request.POST.get('cate_val1')
        # cate_val2 = request.POST.get('cate_val2')
        # cate_val3 = request.POST.get('cate_val3')
        
        # print(dict(request.POST)," -")
        # print(request.POST.getlist('agan_type__in')," -")
        
        
        y={}
        for k,v in dict(request.POST).items():
            if(v[0]!=""):
                y[k]=v
        #print(y," pppp")
        
        z=['latitude', 'longitude', 'district', 'block_n', 'project', 'beat', 'anganwadi_field','agan_type']
        for k,v in dict(request.POST).items():
            if(v[0]!=""):
                if k[:-4] not in ['district', 'block_n', 'project', 'beat', 'anganwadi_field']:
                    z.append(k[:-4])
        # print(z, 'k')

        # print(RuralInfraAwcAcEnglishconverted.objects.filter(**y).count(),"   ssss")
        district =  RuralInfraAwcAcEnglishconverted.objects.filter(**y).values(*tuple(z)).distinct()
        # print(district)
        # filters = {}
        # if dist!="":
        #     filters['district'] = dist
        # if taluka!="":
        #     filters['block_n'] = taluka
        # # if cate1!="" and cate_val1!="":
        # #     filters[cate1]=cate_val1
        # if cate2!="" and cate_val2!="":
        #     filters[cate2]=cate_val2
        # if cate3!="" and cate_val3!="":
        #     filters[cate3]=cate_val3
        # if angan_type!="":
        #     filters['agan_type'] = angan_type
        # if constr!="":
        #     filters['agancbuil_field'] = constr
        # if sitangan!="":
        #     filters['child_sitagan'] = sitangan

        # print("sjdaajskd ",filters)
        
        # district =RuralInfraAwcAcEnglishconverted.objects.filter(**filters)
        # district = RuralInfraAwcAcEnglishconverted.objects.filter(district='')
        # district = serializers.serialize('json', district)
        district = list(district)
        context={"data":district}
        return JsonResponse(context)
    
    else:
        # print(WomenStateHome.objects.values('report_date'))
        awc = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type='मुख्य',project='Yavatmal')
        # awcr = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type__in= ['मुख्य',"मिनी"],district='Akola').count()
        # print(awcr)
        project = RuralInfraAwcAcEnglishconverted.objects.values('project').order_by('project').distinct()
        district = RuralInfraAwcAcEnglishconverted.objects.values('district').order_by('district').distinct()
        taluka = RuralInfraAwcAcEnglishconverted.objects.values('block_n').order_by('block_n').distinct()
        context = {'awc': awc, 'district':district,'taluka':taluka,'project':project}
        return render(request,'viewMap.html',context)
        # return render(request, 'viewMap.html')

def about_wwd(request):
    return render(request, 'about_wwd.html')

def about_op(request):
    return render(request, 'about_op.html')

def about_p(request):
    return render(request, 'about_p.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def map_query(request):
    awc_rur_infra = RuralInfraAwcAcEnglishconverted.objects.all()
    context = {'awc_rural_infra': awc_rur_infra}
    return render(request,viewMap.html,context)

@csrf_exempt
def category(request):
    if request.method == "POST":
        cate1 = request.POST.get('category_1')
        cate2 = request.POST.get('category_2')
        cate3 = request.POST.get('category_3')
        
        d1=""
        d2=""
        d3=""
        if cate1!="":
            d1 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate1).order_by(cate1).distinct())
        if cate2!="":
            d2 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate2).order_by(cate2).distinct())
        if cate3!="":
            d3 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate3).order_by(cate3).distinct())    
            
        #print(d1)
        context = {'c1':d1,'c2':d2,'c3':d3}
        
        return JsonResponse(context)
        #return render(request,'viewMap.html')
        
def category_1(request):
    category__1 = request.GET.get('category_1')
    #print(category__1)
    c1=""
    if category__1!="":
        c1 = list(RuralInfraAwcAcEnglishconverted.objects.values(category__1).order_by(category__1).distinct())
    #print(d1)
    return JsonResponse({'c1':c1})

def category_2(request):
    category__2 = request.GET.get('category_2')
    #print(category__1)
    c2=""
    if category__2!="":
        c2 = list(RuralInfraAwcAcEnglishconverted.objects.values(category__2).order_by(category__2).distinct())
    #print(" ==",c2)
    return JsonResponse({'c2':c2})

def category_3(request):
    category__3 = request.GET.get('category_3')
    #print(category__1)
    c3=""
    if category__3!="":
        c3 = list(RuralInfraAwcAcEnglishconverted.objects.values(category__3).order_by(category__3).distinct())
    #print(" ==",c2)
    return JsonResponse({'c3':c3})

def homepage_mr(request):
    return render(request,'mr/viewHome.html')
 
def about_wwd_mr(request):
    return render(request, 'mr/about_wwd.html')

def about_op_mr(request):
    return render(request, 'mr/about_op.html')

def about_p_mr(request):
    return render(request, 'mr/about_p.html')

def contact_us_mr(request):
    return render(request,'mr/contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

@csrf_exempt
def viewCCMap(request):
    if request.method == "POST":
        print(request.POST)
        child_care=request.POST.get("child_care")
        # one_stop_center=request.POST.get("one_stop_center")
        # counselling_center=request.POST.get("counselling_center")
        # swadhaar_greh=request.POST.get("swadhaar_greh")
        # ujjwal_greh=request.POST.get("ujjwal_greh")
        # mh_police=request.POST.get("mh_police") 
        d1=""
        # d2=""
        # d3=""
        # d4=""
        # d5=""
        # d6=""
        if request.POST.get('district')!="":
            if child_care!=None:
                d1 = CCI7July23.objects.filter(district=request.POST.get('district'))
                #print(d1)
            # if one_stop_center!=None:
            #     d2 = OneStopCenter.objects.filter(district=request.POST.get('district'))
            #     print(d2)
            # if counselling_center!=None:
            #     d3 = CounsellingCentresJuly23.objects.filter(district=request.POST.get('district'))
            #     #print(d3)
            # if swadhaar_greh!=None:
            #     d4 = SwadhaarGreh.objects.filter(district=request.POST.get('district'))
            #     #print(d4)
            # if ujjwal_greh!=None:
            #     d5 = UjjwalGrehJuly23.objects.filter(district=request.POST.get('district'))
            #     print(d5)
            # if mh_police!=None:
            #     d6 = MhPoliceStations.objects.filter(district=request.POST.get('district'))
            #     print(d6)
        else:
            if child_care!=None:
                d1 = CCI7July23.objects.all()
                #print(d1)
            # if one_stop_center!=None:
            #     d2 = OneStopCenter.objects.all()
            #     print(d2)
            # if counselling_center!=None:
            #     d3 = CounsellingCentresJuly23.objects.all()
            #     # print(d3)
            # if swadhaar_greh!=None:
            #     d4 = SwadhaarGreh.objects.all()
            #     #print(d4)
            # if ujjwal_greh!=None:
            #     d5 = UjjwalGrehJuly23.objects.all()
            #     print(d5)   
            # if mh_police!=None:
            #     d6 = MhPoliceStations.objects.all()
            #     print(d6)     
        
            
        d1 = serializers.serialize('json', d1)
        # d2 = serializers.serialize('json', d2)
        # d3 = serializers.serialize('json', d3)
        # d4 = serializers.serialize('json', d4)
        # d5 = serializers.serialize('json', d5)
        # d6 = serializers.serialize('json', d6)

            
        # context = {"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5, "d6":d6}
        context = {"d1":d1}
        return JsonResponse(context)
        
    else:
        awc = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type='मुख्य',project='Yavatmal')
        district = RuralInfraAwcAcEnglishconverted.objects.values('district').order_by('district').distinct()
        taluka = RuralInfraAwcAcEnglishconverted.objects.values('block_n').order_by('block_n').distinct()
        context = {'awc': awc, 'district':district,'taluka':taluka}
        return render(request, 'viewCCMap.html', context)
    
@csrf_exempt
def viewWcdMap(request):
    if request.method == "POST":
        print(request.POST)
        women_state_home=request.POST.get("women_state_home")
        one_stop_center=request.POST.get("one_stop_center")
        counselling_center=request.POST.get("counselling_center")
        swadhaar_greh=request.POST.get("swadhaar_greh")
        ujjwal_greh=request.POST.get("ujjwal_greh")
        working_women_hostel=request.POST.get("working_women_hostel")
        mh_police=request.POST.get("mh_police") 
        d1=""
        d2=""
        d3=""
        d4=""
        d5=""
        d6=""
        d7=""
        if request.POST.get('district')!="":
            if women_state_home!=None:
                d1 = WomenStateHome.objects.filter(district=request.POST.get('district'))
                #print(d1)
            if one_stop_center!=None:
                d2 = OneStopCenter.objects.filter(district=request.POST.get('district'))
                print(d2)
            if counselling_center!=None:
                d3 = CounsellingCentresJuly23.objects.filter(district=request.POST.get('district'))
                #print(d3)
            if swadhaar_greh!=None:
                d4 = SwadhaarGreh.objects.filter(district=request.POST.get('district'))
                #print(d4)
            if ujjwal_greh!=None:
                d5 = UjjwalGrehJuly23.objects.filter(district=request.POST.get('district'))
                print(d5)
            
            if mh_police!=None:
                d6 = MhPoliceStations.objects.filter(district=request.POST.get('district'))
                print(d6)

            if working_women_hostel!=None:
                d7 = Wwh.objects.filter(district=request.POST.get('district'))
                print(d7)
        else:
            if women_state_home!=None:
                d1 = WomenStateHome.objects.all()
                #print(d1)
            if one_stop_center!=None:
                d2 = OneStopCenter.objects.all()
                print(d2)
            if counselling_center!=None:
                d3 = CounsellingCentresJuly23.objects.all()
                # print(d3)
            if swadhaar_greh!=None:
                d4 = SwadhaarGreh.objects.all()
                #print(d4)
            if ujjwal_greh!=None:
                d5 = UjjwalGrehJuly23.objects.all()
                print(d5)   
            if mh_police!=None:
                d6 = MhPoliceStations.objects.all()
                print(d6)
            if working_women_hostel!=None:
                d7 = Wwh.objects.all()
                print(d7)     
        
            
        d1 = serializers.serialize('json', d1)
        d2 = serializers.serialize('json', d2)
        d3 = serializers.serialize('json', d3)
        d4 = serializers.serialize('json', d4)
        d5 = serializers.serialize('json', d5)
        d6 = serializers.serialize('json', d6)
        d7 = serializers.serialize('json', d7)

            
        context = {"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5, "d6":d6, "d7":d7}
        return JsonResponse(context)
        
    else:
        print("In else part")
        awc = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type='मुख्य',project='Yavatmal')
        district = RuralInfraAwcAcEnglishconverted.objects.values('district').order_by('district').distinct()
        taluka = RuralInfraAwcAcEnglishconverted.objects.values('block_n').order_by('block_n').distinct()
        context = {'awc': awc, 'district':district,'taluka':taluka}
        return render(request, 'viewWcdMap.html', context)

def dist_proj(request):
    district = request.GET.get('input[district]')
    
    y={}
    if(district!=None):
        y['district__in']=[district]
    pp = RuralInfraAwcAcEnglishconverted.objects.filter(**y).values('project').distinct()
    
    pp = list(pp)
    context={"pp":pp}
    
    return JsonResponse(context)

def tal_proj(request):
    taluka = request.GET.get('input[taluka]')
    
    y={}
    if(taluka!=None):
        y['block_n__in']=[taluka]
    pp = RuralInfraAwcAcEnglishconverted.objects.filter(**y).values('project').distinct()
    
    pp = list(pp)
    context={"pp":pp}
    
    return JsonResponse(context)
    
    
    
    

# @csrf_exempt
# def women_state_home(request):
#     if request.method == 'POST':
#         y={}
#         for k,v in dict(request.POST).items():
#             if(v[0]!=""):
#                 y[k]=v
#         print(y," pppp")
#         data =  WomenStateHome.objects.filter(**y)
#         # print(data)
#         data = serializers.serialize('json', data)
#         context={"data":data}
#         return JsonResponse(context)
        
#     wsh = request.GET.get('wsh')
#     #print(wsh)
#     w1=""
#     if wsh!="":
#         w1 = list(WomenStateHome.objects.values(wsh).order_by(wsh).distinct())
#     #print(w1)
#     return JsonResponse({'w1':w1})

# @csrf_exempt
# def one_stop_center(request):
#     if request.method == 'POST':
#         y={}
#         for k,v in dict(request.POST).items():
#             if(v[0]!=""):
#                 y[k]=v
#         print(y," pppp")
#         data =  OneStopCenter.objects.filter(**y)
#         # print(data)
#         data = serializers.serialize('json', data)
#         context={"data":data}
#         return JsonResponse(context)
    
#     osc = request.GET.get('osc')
#     #print(osc)
#     o1=""
#     if osc!="":
#         o1 = list(OneStopCenter.objects.values(osc).order_by(osc).distinct())
#     #print(o1)
#     return JsonResponse({'o1':o1})

# @csrf_exempt
def counselling_center(request):
    if request.method == 'POST':
        y={}
        for k,v in dict(request.POST).items():
            if(v[0]!=""):
                y[k]=v
        print(y," pppp")
        data =  CounsellingCentresJuly23.objects.filter(**y)
        print(data)
        data = serializers.serialize('json', data)
        context={"data":data}
        return JsonResponse(context)
    
    cc = request.GET.get('cc')
    #print(cc)
    c1=""
    if cc!="":
        c1 = list(CounsellingCentresJuly23.objects.values(cc).order_by(cc).distinct())
    #print(c1)
    return JsonResponse({'c1':c1})

# @csrf_exempt
# def swadhaar_greh(request):
#     if request.method == 'POST':
#         y={}
#         for k,v in dict(request.POST).items():
#             if(v[0]!=""):
#                 y[k]=v
#         print(y," pppp")
#         data =  SwadhaarGreh.objects.filter(**y)
#         # print(data)
#         data = serializers.serialize('json', data)
#         context={"data":data}
#         return JsonResponse(context)
    
#     sg = request.GET.get('sg')
#     #print(sg)
#     s1=""
#     if sg!="":
#         s1 = list(SwadhaarGreh.objects.values(sg).order_by(sg).distinct())
#     #print(s1)
#     return JsonResponse({'s1':s1})

# @csrf_exempt
# def ujjwal_greh(request):
#     if request.method == 'POST':
#         y={}
#         for k,v in dict(request.POST).items():
#             if(v[0]!=""):
#                 y[k]=v
#         print(y," pppp")
#         data =  UjjwalGreh.objects.filter(**y)
#         # print(data)
#         data = serializers.serialize('json', data)
#         context={"data":data}
#         return JsonResponse(context)
    
#     ug = request.GET.get('ug')
#     #print(ug)
#     u1=""
#     if ug!="":
#         u1 = list(UjjwalGreh.objects.values(ug).order_by(ug).distinct())
#     #print(u1)
#     return JsonResponse({'u1':u1})

