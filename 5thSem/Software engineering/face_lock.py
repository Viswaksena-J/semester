import face_recognition as fr
import os
import pickle
db_path = "/Users/viswaksenajayam/viswaksena_pic.jpeg"
faces = os.listdir(db_path)
known_face_encodings = []
n = 1
for face in faces:
    im = fr.load_image_file(db_path + face)
    #encode the first face in the image
    encoding = fr.face_encodings(im)[0]
    known_face_encodings.append(encoding)
    print("%1d of %2d is done"%(n,len(faces)))
    n+=1       
#create a pickle file
file = open(path+'encode.pickle','wb')
#dump encoding in pickle file
pickle.dump(known_face_encodings,file)
file.close()