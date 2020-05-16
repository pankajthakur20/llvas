import cv2
import glob
import os
import sys
import time
import matplotlib.pyplot as plt
path='/home/ubuntu/llvascloud/attendance/'
ext='.jpg'
faceCascade = cv2.CascadeClassifier("/home/ubuntu/llvascloud/haarcascade_frontalface_default.xml")
os.chdir(path)
i=0 #Total files 
f=[]
filename=[] #List to track files
for file in glob.glob("*gray.jpg"):
    filename.append(file)
print(filename)

filename.sort() #To plot images in order, we have to sort all files.
print(filename)


for file in filename:
    print("\nProcessing File : ",file)
    name=file[0:14]

    i=i+1
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    f.append(len(faces))
    print("Found",len(faces),"Face(s)!")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    r='fd'
    fullpath="%s%s%s%s" %(path,name,r,ext)
    cv2.imwrite(fullpath, gray)
    #status = cv2.imwrite(fullpath +file, image)
    status = cv2.imwrite(fullpath, image)
print(f)
if i==0:
    print("Empty Directory")
else:
    print("\nTotal Files =",i)

plt.switch_backend('agg')
#n=int(input("Total persons : "))
#matplotlib.use('Agg')
n=3
f1=f[0]
f2=f[1]
f3=f[2]
f4=f[3]
f5=f[4]
file=[]
f1=f1/n*100
f2=f2/n*100
f3=f3/n*100
f4=f4/n*100
f5=f5/n*100
fa=[f1,f2,f3,f4,f5]
day=[1,2,3,4,5]
attendance=[f1,f2,f3,f4,f5]
filename=[]
for file in glob.glob("*fd.jpg"):
    name=file[0:14]
    filename.append(name)
filename.sort()
label=[filename[0],filename[1],filename[2],filename[3],filename[4]]
plt.xticks(fa,label,rotation=-90)
plt.subplots_adjust(bottom=0.4, top=0.9)
#plt.bar(day,attendance,tick_label=label, width=0.5,color=['red','green'], align='center')
plt.bar(day,attendance,tick_label=label, width=0.5, align='center')
plt.xlabel('Time')
plt.ylabel('Present students (%age)')
today = time.strftime("%d/%m/%Y")
#print(today)

plt.title('Attendance Position on '+str(today))
#plt.show()
plt.savefig('attendance')

