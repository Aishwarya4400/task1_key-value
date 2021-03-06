# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BURnNV0oh1OplBHWQYB5A_Z8wueQn8lT
"""

import logging
import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

d={} #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value, timeout=0a):
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database.") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. ") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")

 
 
print("enter any key")
n=int(input())
if(n==1):
  print("enter key")
  key=input()
  value=int(input())
  create(key,value)
if(n==2):
  print("enter key to read")
  def checkKey(d, key): 
      if d.has_key(key): 
        print("Present, value =", d[key] )
      else: 
        print("Not present")
  checkKey(d, key)
  read(key)
if(n==3):
  print("enter key")
  key=input()
  read(key)
if(n<1 or n>3):
  print("enter valid number")
exit()


#we can access these using multiple threads like
t1=Thread(target=(create),args=(1,)) #as per the operation
t1.start()
time.sleep(1)
t2=Thread(target=(read),args=(1,)) #as per the operation
t2.start()
time.sleep(1)
t3=Thread(target=(delete),args=(1,))
t3.start()
time.sleep(1)
#and so on upto tn
print(d)
#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

y=input("If you want it to master database Say yes or no")
if(y=='yes'):
  data={}
  import json
  with open('master.json','r') as fp:
    data = json.load(fp)
  master=dict(data)
  master.update(d)
  with open('master.json','w') as fp:
    json.dump(master,fp)

print("All task done")