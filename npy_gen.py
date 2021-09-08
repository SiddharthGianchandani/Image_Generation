import cv2
import os
import numpy as np
import tensorflow as tf

#fol="dcgan_proper"
#fol="vae_proper"

def create_train_data():
    training_data=[]
    for img in os.listdir(fol):
        path=os.path.join(fol,img)
        img=cv2.resize(cv2.imread(path),(28,28))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        training_data.append([np.array(gray)])
    np.save('gan.npy',training_data)
    
#create_train_data()

train_data=np.load('gan.npy',allow_pickle=True)

print(train_data[:1])
