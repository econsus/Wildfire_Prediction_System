import numpy as np
import pandas as pd
import tensorflow as tf


df=pd.read_csv('Variables_without_index.csv')
label=pd.read_csv('label.csv')


def normalize_series(data, min, max):
    data = data - min
    data = data / (max-min)
    return data


data = df[['slhf','sshf']].values #take the data value
data = normalize_series(data, data.min(axis=0), data.max(axis=0)) #Normalizing the data
label = np.array(label) #turning labels pandas dataset into numpy array

#The problem is here. I dont know how to reshape the label, cuz the label can only take a !D array
#Without reshaping the data, it will be to big to run causing resource exhausted error
#Reshaping the data into shape of (times,lat,lon) ideally,
#Because the label can only accept 1D array, have to improvise on how to reshape the data
data = data.reshape((8760,69,185,2))
label = label.reshape((8760,69,185))

#OR maybe i could just limit the time dimensions of the original 1D array
#didnt work, it sometimes can make it even worse, from 600 GiB to 1,3 TiB
#I dont know anymore now. If you want to try this than feel free,
#Since my laptop is a very low end, with i5-3230m, with dedicated intel hd 4k graphic.
#times = 90*24*69*185 #days*hours*lat*lon
#data=data[:times]
#label=label[:times]

x_train = data[:int(len(data)*0.8)]
x_test = data[int(len(data)*0.8):]
label_train = label[:int(len(label)*0.8)]
label_test = label[int(len(label)*0.8):]
print(x_train.shape)

#Creating the models, input shape include all dimensions of the data except the first one
#tweak it a little to make a less time taking for training or to make a better accuracy
model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(128,(3,3),input_shape=(69,185,2),activation='relu',padding='same'),
        #tf.keras.layers.MaxPooling2D(),
        #tf.keras.layers.Conv1D(64,3,activation='relu'),
        #tf.keras.layers.MaxPooling1D(),
        #tf.keras.layers.Flatten(),
        #tf.keras.layers.LSTM(128),#,return_sequences=True),
        #tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(128,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(4,activation='softmax')
        #tf.keras.layers.Reshape((69,185,4))
    ])

print(model.summary())
#compiling the model, sometimes if the input shape isnt correct it will raise error,
#even if the input shape is correct, if the labels have more than 1 dimensions it will stil raises an error
model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=['acc'])

#Trying to debug
sample_data=data[:10]
pred=model.predict(sample_data)
print(pred)

#fitting the model, no problem on this part so far
model.fit(x_train,label_train,epochs=10,validation_data=(x_test,label_test),verbose=1)

model.save('Saved_model2.keras')
model.save('Test_model_2.h5')
