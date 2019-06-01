#region Import libraries
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
# import keras
# from keras.optimizers import RMSprop
# from keras.preprocessing.image import ImageDataGenerator
#endregion

#region carga de datos desde la ruta
train_normal_dir = os.path.join("D:/ITM/2019-I/IA_ITM/chest-xray-pneumonia/chest_xray/chest_xray/train/NORMAL")
train_neumonia_dir = os.path.join("D:/ITM/2019-I/IA_ITM/chest-xray-pneumonia/chest_xray/chest_xray/train/PNEUMONIA")
test_normal_dir = os.path.join("D:/ITM/2019-I/IA_ITM/chest-xray-pneumonia/chest_xray/chest_xray/test/NORMAL")
test_neumonia_dir = os.path.join("D:/ITM/2019-I/IA_ITM/chest-xray-pneumonia/chest_xray/chest_xray/test/PNEUMONIA")
#endregion

#region punto 1.1 ¿Cuántas imágenes tiene el dataset (entrenamiento y prueba)?
numberImageNormalTrain = len(os.listdir(train_normal_dir))
numberImageNeumoniaTrain = len(os.listdir(train_neumonia_dir))
numberImageNormalTest = len(os.listdir(test_normal_dir))
numberImageNeumoniaTest = len(os.listdir(test_neumonia_dir))
totalImages = numberImageNormalTrain+numberImageNeumoniaTrain+numberImageNormalTest+numberImageNeumoniaTest

print("********punto 1.1 ¿Cuántas imágenes tiene el dataset (entrenamiento y prueba)?**********")
print('Total Imagenes Normal para entrenamiento : ', numberImageNormalTrain)
print('Total Imagenes Neumonia para entrenamiento : ', numberImageNeumoniaTrain)
print('Total Imagenes para entrenamiento : ', numberImageNormalTrain + numberImageNeumoniaTrain)
print('Total Imagenes Normal para test : ', numberImageNormalTest)
print('Total Imagenes Neumonia para test : ', numberImageNeumoniaTest)
print('Total Imagenes para test : ', numberImageNormalTest + numberImageNeumoniaTest)
print('Total Imagenes : ', totalImages)
#endregion

#region ************* Impresión de algunas imagenes *****************
train_normal_names = os.listdir(train_normal_dir)
train_neumonia_names = os.listdir(train_neumonia_dir)
print(train_normal_names[:10])
print(train_neumonia_names[:10])

nrows = 4
ncols = 4

pic_index = 0

fig = plt.gcf()
fig.set_size_inches(ncols * 2, nrows * 2)

pic_index += 8
next_normal_pix = [os.path.join(train_normal_dir, fname) for fname in train_normal_names[pic_index-8:pic_index]]
next_neumonia_pix = [os.path.join(train_neumonia_dir, fname) for fname in train_neumonia_names[pic_index-8:pic_index]]

for i, img_path in enumerate(next_normal_pix+next_neumonia_pix):
    sp = plt.subplot(nrows, ncols, i + 1)
    sp.axis('Off')
    plt.title(img_path.split("/")[8].split('\\')[0]) #Modificar esta linea según sea la ruta
    img = mpimg.imread(img_path)
    plt.imshow(img, cmap='gray')

plt.show()
#endregion 

#region Punto 2.Leer el dataset utilizando ImageDataGenerator
#TODO: instalar tensorflow y Keras, realizar la importación de los paquetes y utilizar el ImageDataGenerator de keras
#endregion
