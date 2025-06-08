import pickle
import cv2
import os
import cvzone
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)  # جرب استخدام 0 إذا كنت تواجه مشكلة مع 1
cap.set(3, 640)  # ضبط عرض الصورة
cap.set(4, 480)  # ضبط ارتفاع الصورة,üğ, dmledm eefoöoe يثخنيث

imgBackground = cv2.imread('Resources/background.png')

#importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir (folderModePath)
imgModeList = []

for path in modePathList:
        imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
 #print(len(imgModeList))


# Load the encoding file
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)

while True:
        success, img = cap.read()

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25 )
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame  = face_recognition.face_encodings(imgS,faceCurFrame )


        imgBackground [162:162+480,55:55+640] = img
        imgBackground [44:44+633,808:808+414] = imgModeList[1]

        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                #  print("matches", matches)
                #  print("faceDis", faceDis)

                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                        #print ("Hos geldiniz")
                        #print (studentIds[matchIndex])
                        y1, x2, y2, x1 = faceLoc
                        y1,x2,y2,x1 = y1 * 4,x2 * 4,y2 * 4,x1 *4
                        bbox = 55 + x1, 162 + y1, x2 - x1 , y2 - y1
                        imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)

        '''

        for encodeFace, faceLoc in zip(encace_cur_fode_cur_fra, fra):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.5)  # تحسين السلاسة
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                        student_id = studentIds[matchIndex]

                        # تكبير المسافات لجعل الصندوق حول الوجه أكثر دقة
                        y1, x2, y2, x1 = [val * 4 for val in faceLoc]
                        padding = 10  # إضافة حواف لجعل الصندوق أكثر وضوحًا
                        bbox = (55 + x1 - padding, 162 + y1 - padding, x2 - x1 + 2 * padding, y2 - y1 + 2 * padding)

                        # رسم المستطيل
                        imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

                        print(f"تم التعرف على الطالب برقم التعريف: {student_id}")  '''




        cv2.imshow("webcam", img)
        cv2.imshow("Face Attendance", imgBackground)
        cv2.waitKey(1)  # إيقاف البرنامج عند الضغط على ESC



