import os, sys
import shutil

a = os.listdir(os.getcwd()+"/raw-images-training/ara")
print a

i = 40
print len(a)
while i<60:
    b = os.listdir(os.getcwd()+"/raw-images-training/ara/"+a[i])
    os.makedirs(os.getcwd()+"/training-images/training-200/" + a[i])
    j = 0
    try:
        while j<30:
            shutil.copy(os.getcwd()+"/raw-images-training/ara/"+a[i]+"/"+b[j], os.getcwd()+"/training-images/training-200/"+a[i]+"/"+b[j])
            j = j+1
    except:
        print a[i]
    i = i+1

print b









# import os, sys
# import shutil
#
# a = os.listdir(os.getcwd()+"/raw-images-training")
# print a
#
# i = 0
# print len(a)
# while i<100:
#     b = os.listdir(os.getcwd()+"/raw-images-training/"+a[i])
#     os.makedirs(os.getcwd()+"/raw-images-testing/" + a[i])
#     j = 0
#     try:
#         while j<50:
#             shutil.move(os.getcwd()+"/raw-images-training/"+a[i]+"/"+b[j], os.getcwd()+"/raw-images-testing/"+a[i]+"/"+b[j])
#             j = j+1
#     except:
#         print a[i]
#     i = i+1
#
# print b







'''
# !/usr/bin/python

import os, sys

# listing directories


print os.getcwd()+"/raw-images"

a = os.listdir(os.getcwd()+"/raw-images")

print a

i = 0
print len(a)
while i<len(a):
    os.rename("raw-images/"+a[i], "raw-images/"+a[i].replace(" ", "_"))
    i = i+1

print i
# renaming directory ''tutorialsdir"
#os.rename("tutorialsdir","tutorialsdirectory")

print "Successfully renamed."

# listing directories after renaming "tutorialsdir"
#print "the dir is: %s" %os.listdir(os.getcwd())
'''


