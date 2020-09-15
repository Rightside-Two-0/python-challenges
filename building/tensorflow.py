# @Author: two_0
# @Date:   14-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 14-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#%%
import tensorflow as tf
#%%md
#Load MNIST dataset
#%%
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255, x_test / 255
#%%md
#Build tf.keras.Sequential model
#%%
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])
#%%md
#Predictions
#%%
predictions = model(x_train[:1]).numpy()
predictions
#%%md
#Convert to probabilites
#%%
tf.nn.softmax(predictions).numpy()
#%%md
#Loss function
#%%
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
            loss=loss_fn,
            metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
#%%md
#Evaluate the model
#%%
model.evaluate(x_test, y_test, verbose=2)
