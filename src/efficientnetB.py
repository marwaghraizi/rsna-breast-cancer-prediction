import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten, BatchNormalization, Input, SeparableConv2D, Rescaling, Activation
import sys
from keras.applications.efficientnet import EfficientNetB6
from keras import Model
from tensorflow.keras import layers
import tensorflow as tf
from keras.utils import image_dataset_from_directory


image_size = (512, 512)
batch_size = 32

train_path = sys.argv[1]
test_path = sys.argv[2]

train_ds = image_dataset_from_directory(train_path, seed=1337, image_size = image_size, batch_size = batch_size)
test_ds = image_dataset_from_directory(test_path, seed=1337, image_size = image_size, batch_size = batch_size, shuffle = False)

y_true = []
for images, labels in test_ds:
    y_true.extend(labels.numpy())

def plot_hist(hist, file="plot.png"):
    plt.plot(hist.history["accuracy"])
    plt.plot(hist.history["val_accuracy"])
    plt.title("model accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.savefig(file)




def unfreeze_model(model):
    # We unfreeze the top 20 layers while leaving BatchNorm layers frozen
    for layer in model.layers[-20:]:
        if not isinstance(layer, layers.BatchNormalization):
            layer.trainable = True

    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
    model.compile(
        optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"]
    )

# https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/#transfer-learning-from-pretrained-weights
# not exactly the same since this is binary classification
with tf.device('/device:GPU:0'):

    inputs = layers.Input(shape=(512, 512, 3))
    x = inputs
    model = EfficientNetB6(include_top=False, input_tensor=x, weights="imagenet")
    model.trainable = False

    x = layers.GlobalAveragePooling2D(name="avg_pool")(model.output)
    x = layers.BatchNormalization()(x)

    top_dropout_rate = 0.2
    x = layers.Dropout(top_dropout_rate, name="top_dropout")(x)

    outputs = layers.Dense(1, activation="sigmoid", name="pred")(x)

    model = tf.keras.Model(inputs, outputs, name="EfficientNet")
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)

    model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"])

    epochs = 25
    hist = model.fit(train_ds, epochs=epochs, batch_size=batch_size, validation_data=test_ds)

plot_hist(hist, "before_freezing_accuracy.png")
unfreeze_model(model)

epochs = 15
hist = model.fit(train_ds, epochs=epochs, validation_data=test_ds)
plot_hist(hist, "after_freezing_accuracy.png")