import tensorflow as tf  # now import the tensorflow module
from tensorflow.keras import datasets, layers, models
import numpy as np
import matplotlib.pyplot as plt
import cv2
from LoadDataSet import loadDataSet
import time

print(tf.version)  # make sure the version is 2.x


start = time.time()

class_names = ['Boredom','Engagement','Confusion','Frustration']


dataset_test , dataset_train, te_lables, tr_labels = loadDataSet()
train_images = np.array(dataset_train)
train_labels = np.array(tr_labels)

test_images = np.array(dataset_test)
test_labels = np.array(te_lables)

train_images.shape
rank = tf.rank(train_images)

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

#initializer = tf.keras.initializers.glorot_uniform(1)

accuracys = []
histories = []

model = models.Sequential()
# Layer 1
# The input shape of our data will be 640, 480, 3 and we will process 16 filters of size 3x3 over our input data.
# We will also apply the activation function relu to the output of each convolution operation.
model.add(layers.Conv2D(16, (3, 3), activation='relu', input_shape=(480, 640, 3)))
# Layer 2 
# This layer will perform the max pooling operation using 2x2 samples and a stride of 2.
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

#model.summary()

# Adding dense layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

summary = model.summary()

# Train the model
model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=20, 
                    validation_data=(test_images, test_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

'''
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
'''



end = time.time()
print('Elapsed time:')
print(end - start)



history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
epochs = range(1, len(acc) + 1)


plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.clf()


#plotting Accuracy
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

print('Accuracy Test:')
print(test_acc)
#accuracys.append(test_acc)
#histories.append(history.history['val_accuracy'])