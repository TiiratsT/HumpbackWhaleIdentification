import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import os

ss = pd.read_csv("Data\\humpback-whale-identification\\train.csv")
print(ss.head())

for img in os.listdir("Data\\humpback-whale-identification\\train"):
    image = mpimg.imread("Data\\humpback-whale-identification\\train\\" + img)
    plt.imshow(image)
    plt.show()
