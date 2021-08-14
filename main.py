import requests
import os
def MainMenu(): #Static MainMenu
    print(" Welcome To X Project \n")
    print("Choose An Option Below To Proceed : \n")
    print("1- Domain Information (WHOIS SCAN) \n")
    print("2- Subdomain Scanning  \n")
    print("3- Subdomain Takeover \n")
    print("4- Directory Bruteforcing (WHOIS SCAN) \n")
    print("5- All IN One  (WHOIS SCAN) \n")

    option=int(input(": "))
    return option

def whoisScan(url):
    # url=input("Enter Domain Without http or https: ") #taking domain form user
    host="https://www.whoisxmlapi.com/whoisserver/WhoisService"
    apiKey="at_TQ5u5iv5ieahbDIMD8dZunD6jhqXx"
    domain=url.strip()
    finalurl=host+"?apiKey="+apiKey+"&domainName="+domain+"&outputFormat=JSON"
    
    response=requests.get(finalurl)
    whoisData=response.json()
    print("Whois Information For Domain ",url,"\n")
    print("Created Date : ",whoisData['WhoisRecord']['createdDate'],"\n")
    print("Updated Date : ",whoisData['WhoisRecord']['updatedDate'],"\n")
    print("Expire Date : ",whoisData['WhoisRecord']['expiresDate'],"\n")
    print("Organization  Name : ",whoisData['WhoisRecord']['registrant']['organization'],"\n")
    print("Organization  State : ",whoisData['WhoisRecord']['registrant']['state'],"\n")
    print("Organization  Country : ",whoisData['WhoisRecord']['registrant']['country'],"\n")

def subdomanScan(url):
    finalcmd="sf.exe -d "+url+" -silent > "+url+".txt"
    os.system(finalcmd)
    f1=open(url+'.txt')
    filedata=f1.read().splitlines()
    for i in filedata:
        print(i)
    print("You Can Access Your Data In Output File Name : ",url+".txt")
    f1.close()

def subdomainTakeover(url):
    print("Subdomain Takeover Started")
    subdomanScan(url)
    finalcmd="st.exe -targets "+url+".txt > st.txt"

    os.system(finalcmd)
    f2=open('st.txt')
    filedata=f2.read().splitlines()
    for i in filedata[7:]:
        print(i)
   
    f2.close()
def directoryBruteforce(url):
    print("Directory Bruteforcing Starting")
    f3=open('dicc.txt')
    paths=f3.read().splitlines()
    for i in paths:
        finalurl="https://"+url+i
        response=requests.get(finalurl)
        print("Request To Url ",finalurl, "Status Code ",response.status_code)
        if(response.status_code==200):
            f4=open('200.txt','a')
            f4.write(finalurl)
            f4.close()

        elif(response.status_code==403):    
            f5=open('403.txt','a')
            f5.write(finalurl)
            f5.close()
        else:
            f6=open('404.txt','a')
            f6.write(finalurl)
            f6.close()
            
#Calling The Function 
choosenOption= MainMenu()
if(choosenOption==1):
    url=input("Enter Domain Without http or https: ")
    whoisScan(url)
elif(choosenOption==2):
    url=input("Enter Domain Without http or https: ")
    subdomanScan(url)
elif(choosenOption==3):
    url=input("Enter Domain Without http or https: ")
    subdomainTakeover(url)
elif(choosenOption==4):
    url=input("Enter Url Path With / : ")
    directoryBruteforce(url)
elif(choosenOption==5):
    url=input("Enter Domain Without http or https: ")
    whoisScan(url)
    subdomanScan(url)
    subdomainTakeover(url)
    directoryBruteforce(url+'/')

