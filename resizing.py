from PIL import Image
import os
import pandas as pd
import numpy as np


train_data = pd.read_csv("Data\\humpback-whale-identification\\train.csv")

input_shape = (128, 128)

for i, img in enumerate(train_data['Image']):
    if train_data['Id'].iloc[i:i+1].values[0] == 'new_whale':
        continue
    f_name = r'Data\\humpback-whale-identification\\train\\' + img
    train_image = Image.open(f_name, )
    train_image = train_image.resize(input_shape).convert('L')
    new_f_name = r'Data\\humpback-whale-identification\\train_resized_128\\' + img
    train_image.save(new_f_name, "JPEG")        


for img in os.listdir("Data\\humpback-whale-identification\\test"):
    f_name = r'Data\\humpback-whale-identification\\test\\' + img
    test_image = Image.open(f_name)
    test_image= test_image.resize(input_shape).convert('L')
    new_f_name = r'Data\\humpback-whale-identification\\test_resized_128\\' + img
    test_image.save(new_f_name, "JPEG")
