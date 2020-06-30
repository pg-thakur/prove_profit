from django.shortcuts import render, HttpResponse
from home.models import detail,bss_set1
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib.dates import DateFormatter







# # Create your views here.

def home(request):
    return render(request,'home/home.html')

def analysis(request):
    if request.method=='POST':
        entity=request.POST['entityName']
        industry=request.POST['industryName']
        period1=request.POST['period1']
        period2=request.POST['period2']
        industry=request.POST['industryName']
        industry=request.POST['industryName']
        analysis=detail(entity=entity,industry=industry,period1=period1,period2=period2)

        analysis.save()
        tnca1=request.POST['tnca1']
        tnca2=request.POST['tnca2']
        tca1=request.POST['tca1']
        tca2=request.POST['tca2']
        invt1=request.POST['invt1']
        invt2=request.POST['invt2']
        trade1=request.POST['trade1']
        trade2=request.POST['trade2']
        cash1=request.POST['cash1']
        cash2=request.POST['cash2']
        capital1=request.POST['capital1']
        capital2=request.POST['capital2']
        equity1=request.POST['equity1']
        equity2=request.POST['equity2']
        ncl1=request.POST['ncl1']
        ncl2=request.POST['ncl2']
        cl1=request.POST['cl1']
        cl2=request.POST['cl2']
        ina1=request.POST['ina1']
        ina2=request.POST['ina2']



        analysis=bss_set1(total_non_current_asset=tnca1,total_current_asset=tca1,inventories=invt1,trade_other_current=trade1,cash=cash1,issued_capital=capital1,eqity=equity1,non_current_liability=ncl1,current_liability=cl1,intangible_asset=ina1)
        analysis.save()

        analysis=bss_set1(total_non_current_asset=tnca2,total_current_asset=tca2,inventories=invt2,trade_other_current=trade2,cash=cash2,issued_capital=capital2,eqity=equity2,non_current_liability=ncl2,current_liability=cl2,intangible_asset=ina2)
        analysis.save()
    return render(request,'home/analysis.html')



def article(request):
    return render(request,'home/article.html')




def report(request):
    qs=bss_set1.objects.all().values('total_non_current_asset','total_current_asset','inventories','trade_other_current','cash','issued_capital','eqity','non_current_liability','current_liability','intangible_asset').order_by('-id')[:2]
    qs1=reversed(qs)
    data=pd.DataFrame(qs1)
    data1=data.transpose()
    name=detail.objects.values_list('entity').last()

    ind=detail.objects.values_list('industry').last()
    c1=detail.objects.values_list('period1').last()
    c2=detail.objects.values_list('period2').last()
    entity=name[0]
    industry=ind[0]
    period1=c1[0]
    period2=c2[0]
    data1.columns=['period1','period2']

# for asset structure-------------------------------
    asset=data1.loc[('total_non_current_asset','total_current_asset'),:]
    asset['diffence']=asset['period2']-asset['period1']
    sum1=0
    sum2=0
    sumdiff=0
    for i in range(2):
        sum1=sum1+asset.iloc[i,0]
        sum2=sum2+asset.iloc[i,1]
        sumdiff=sumdiff+asset.iloc[i,2]
    
    asset.loc['total asset']=[sum1,sum2,sumdiff]
    asset['% of balance in period1']=asset['period1']/asset.iloc[2,0]*100
    asset['% of balance in period2']=asset['period2']/asset.iloc[2,1]*100
    asset['% of balance in difference']=asset['diffence']/asset['period1']*100


    bar=[asset.iloc[0,0],asset.iloc[0,1],asset.iloc[1,0],asset.iloc[1,1]]




    
    # for equity and liability-----------------------

    liability=data1.loc[('eqity','non_current_liability','current_liability'),:]
    liability['diffence']=liability['period2']-liability['period1']
    sum_lib1=0
    sum_lib2=0
    sum_lib_diff=0
    for i in range(1,3):
        sum_lib1=sum_lib1+liability.iloc[i,0]
        sum_lib2=sum_lib2+liability.iloc[i,1]
        sum_lib_diff=sum_lib_diff+liability.iloc[i,2]
        
    liability.loc['Total_Liability']=[sum_lib1,sum_lib2,sum_lib_diff]
    
    liability.loc['Total_Equity_And_Liability']=[sum_lib1+liability.iloc[0,0],sum_lib2+liability.iloc[0,1],sum_lib_diff+liability.iloc[0,2]]
    
    liability['% of liability in period1']=liability['period1']/liability.iloc[4,0]*100
    liability['% of liability in period2']=liability['period2']/liability.iloc[4,1]*100
    liability['% of equity&liability in difference']=liability['diffence']/liability['period1']*100
    

    chart2=[liability.iloc[2,4],liability.iloc[1,4],liability.iloc[0,4]]

    bar2=[liability.iloc[0,0],liability.iloc[0,1],
    liability.iloc[1,0],liability.iloc[1,1],
    liability.iloc[2,0],liability.iloc[2,1]]


    # for net assets---------------------------------
    
    columns=['period1','period2']
    index=['Net_tangible_Asset','Net_Asset','Issued_Capital','Diff_of_net_asset_and_issued_capital']
    net_asset=pd.DataFrame(index=index,columns=columns)
    net_asset.loc['Net_tangible_Asset']=[asset.iloc[2,0]-liability.iloc[3,0]-data1.iloc[9,0],asset.iloc[2,1]-liability.iloc[3,1]-data1.iloc[9,1]]
    net_asset.loc['Net_Asset']=[asset.iloc[2,0]-liability.iloc[3,0],asset.iloc[2,1]-liability.iloc[3,1]]
    net_asset.loc['Issued_Capital']=[data1.iloc[5,0],data1.iloc[5,1]]
    net_asset.loc['Diff_of_net_asset_and_issued_capital']=[net_asset.iloc[1][0]-net_asset.iloc[2][0],net_asset.iloc[1][1]-net_asset.iloc[2][1]]
    net_asset['diffence']=net_asset['period2']-net_asset['period1']
    net_asset['% of balance in period1']=net_asset['period1']/asset.iloc[2,0]*100
    net_asset['% of balance in period2']=net_asset['period2']/asset.iloc[2,1]*100
    net_asset['% of balance in difference']=net_asset['diffence']/asset.iloc[2,1]*100
       

    bar3=[net_asset.iloc[1,0],net_asset.iloc[1,1],
net_asset.iloc[2,0],net_asset.iloc[2,1]]



# for stability---------------------------------
    columns=['period1','period2']
    index=['Debt_to_Equity_Ratio','Debt_Ratio','Long_term_Debt_to_Equity','Noncurrent_asset_to_Net_worth','Capitalization_ratio','Current_Liability_ratio']
    stability=pd.DataFrame(index=index,columns=columns)
    stability.loc['Debt_to_Equity_Ratio']=[liability.iloc[3,0]/liability.iloc[0,0],liability.iloc[3,1]/liability.iloc[0,1]]
    stability.loc['Debt_Ratio']=[liability.iloc[3,0]/asset.iloc[2,0],liability.iloc[3,1]/asset.iloc[2,1]]
    stability.loc['Long_term_Debt_to_Equity']=[liability.iloc[1,0]/liability.iloc[0,0],liability.iloc[1,1]/liability.iloc[0,1]]
    stability.loc['Noncurrent_asset_to_Net_worth']=[asset.iloc[0,0]/net_asset.iloc[1,0],asset.iloc[0,1]/net_asset.iloc[1,1]]
    stability.loc['Capitalization_ratio']=[liability.iloc[1,0]/(liability.iloc[1,0]+liability.iloc[0,0]),liability.iloc[1,1]/(liability.iloc[1,1]+liability.iloc[0,1])]
    stability.loc['Current_Liability_ratio']=[liability.iloc[2,0]/liability.iloc[3,0],liability.iloc[2,1]/liability.iloc[3,1]]

    stability['diffence']=stability['period2']-stability['period1']

    line1=[stability.iloc[0,0],stability.iloc[0,1],stability.iloc[1,0],stability.iloc[1,1],stability.iloc[3,0],stability.iloc[3,1],stability.iloc[4,0],stability.iloc[4,1],stability.iloc[5,0],stability.iloc[5,1]]




# for liquidity ratio------------------------------

    columns=['period1','period2']
    index=['Current_ratio','Quick_ratio','Cash_ratio']
    liquidity=pd.DataFrame(index=index,columns=columns)
    liquidity.loc['Current_ratio']=[asset.iloc[1,0]/liability.iloc[2,0],asset.iloc[1,1]/liability.iloc[2,1]]
    liquidity.loc['Quick_ratio']=[(asset.iloc[1,0]-data1.iloc[2,0])/liability.iloc[2,0],(asset.iloc[1,1]-data1.iloc[2,1])/liability.iloc[2,1]]
    liquidity.loc['Cash_ratio']=[data1.iloc[4,0]/liability.iloc[2,0],data1.iloc[4,1]/liability.iloc[2,1]]

    liquidity['diffence']=liquidity['period2']-liquidity['period1']

    line2=[liquidity.iloc[0,0],liquidity.iloc[0,1],liquidity.iloc[1,0],liquidity.iloc[1,1],liquidity.iloc[2,0],liquidity.iloc[2,1]]




    table={
        'df' : data1.to_html(),
        'asset':asset.to_html(),
        'liability':liability.to_html(),
        'net_asset':net_asset.to_html(),
        'stability':stability.to_html(),
        'liquidity':liquidity.to_html(),
        'period1':period1,
        'period2':period2,
        'entity':entity,
        'industry':industry,

        'non_current_asset_p1': asset.iloc[0,0],
        'non_current_asset_p2':asset.iloc[0,1],
        'p_non_current_asset':asset.iloc[0,2],
        'current_asset_p1':asset.iloc[1,0],
        'current_asset_p2':asset.iloc[1,1],
        'p_current_asset':asset.iloc[1,2],
        'total_asset_p1':asset.iloc[2,0],
        'total_asset_p2':asset.iloc[2,1],
        'p_total_asset':asset.iloc[2,2],


        'equity_p1':liability.iloc[0,0],
        'equity_p2':liability.iloc[0,1],
        'p_equity':liability.iloc[0,2],
        'p_noncurrent_liab':liability.iloc[1,2],
        'p_current_liab':liability.iloc[2,2],


        'net_tangible_p1':net_asset.iloc[0,0],
        'net_tangible_p2':net_asset.iloc[0,1],
        'net_asset_p1':net_asset.iloc[1,0],
        'net_asset_p2':net_asset.iloc[1,1],
        'issued_capital_p1':net_asset.iloc[2,0],
        'issued_capital_p2':net_asset.iloc[2,1],

        'asset_pie_val1':asset.iloc[1,4],
        'asset_pie_val2':asset.iloc[0,4],


        'bar_1':bar[0],
        'bar_2':bar[1],
        'bar_3':bar[2],
        'bar_4':bar[3],

        'chart2_1':chart2[0],
        'chart2_2':chart2[1],
        'chart2_3':chart2[2],

        'bar2_1':bar2[0],
        'bar2_2':bar2[1],
        'bar2_3':bar2[2],
        'bar2_4':bar2[3],
        'bar2_5':bar2[4],
        'bar2_6':bar2[5],

        'bar3_1':bar3[0],
        'bar3_2':bar3[1],
        'bar3_3':bar3[2],
        'bar3_4':bar3[3],

        'line1_1':line1[0],
        'line1_2':line1[1],
        'line1_3':line1[2],
        'line1_4':line1[3],
        'line1_5':line1[4],
        'line1_6':line1[5],
        'line1_7':line1[6],
        'line1_8':line1[7],
        'line1_9':line1[8],
        'line1_10':line1[9],

        'line2_1':line2[0],
        'line2_2':line2[1],
        'line2_3':line2[2],
        'line2_4':line2[3],
        'line2_5':line2[4],
        'line2_6':line2[5],
        
    }
    return render(request,'home/report.html',table)
