# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import csv
#from savedb import store
import time
from Naverapi import*
import re
import datetime
import random
page=int(1)


def GetreplelistByCsv(code):

    count=1
    txtcnt=0
    txtFile=open("크롤링예제.txt",'a', newline='')
    #writer=csv.writer(csvFile)
    while(1):
        if count==10:
            break;
        if count==1:
            url = "http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=" +str(code) + "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
        else:
            url = "http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=" + str(code) + "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(count)
        try:
           html=urlopen(url)
        except:
            print("오류")
            txtFile.close()
            break
        bsObj=BeautifulSoup(html.read(),"html.parser")
        score_result=bsObj.find('div',class_="score_result")
        replelist=score_result.findAll('li')
        txtRow = []
        for list in replelist:
            reple=list.find('div', class_="star_score").find('em').get_text()+"@"+list.find('div',class_="score_reple").find('p').get_text()
            print(reple)
            txtRow.append(reple)
            txtcnt+=1
        txtFile.write('\n'.join(txtRow))
        count+=1
        time.sleep(0.2)
    txtFile.close()
    return txtcnt


'''def GetreplelistByDb(code,moviename):

    count=1

    while(1):
        if count==1000:
            break
        if count==1:
            url = "http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=" +str(code) + "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
        else:
            url = "http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=" + str(code) + "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(count)
        try:
           html=urlopen(url)
        except:
            print("오류")
            break
        bsObj=BeautifulSoup(html.read(),"html.parser")
        score_result=bsObj.find('div',class_="score_result")
        replelist=score_result.findAll('li')
        for list in replelist:
            reple=list.find('div',class_="score_reple").find('p').get_text()
            store(moviename,reple)
        count+=1
        time.sleep(1)'''

while(1):
 moviename=input("검색할 영화명을 입력(종료 원할시 1):")
 if(moviename==str(1)):
      break
 code=getCodeFromNaver(moviename)
 print(code)
 txtcnt1=GetreplelistByCsv(code)
 print(txtcnt1)

