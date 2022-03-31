import os
import shutil
def nextStep():
    open(file1,'w')
    open(file2,'w')

file1=input('Enter the name of the first file')
if os.path.exists(file1):
    data_a=open(file1,'r')
    file2=input('Enter the name of the seconf file')
    if os.path.exists(file2):
      data_b=open(file2,'r')
      nextStep()
    else:  
         print('The file dosent exist')
else:
    print('The file dosen''t exits')

