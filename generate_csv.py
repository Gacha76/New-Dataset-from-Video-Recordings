import os
import csv

read_train = os.listdir("images/train")

with open("train.csv", mode="w", newline="") as train_file:
    for image_file in read_train:
        text_file = image_file.replace(".png", ".txt")
        data = [image_file, text_file]
        writer = csv.writer(train_file)
        writer.writerow(data)

read_val = os.listdir("images/val")

with open("val.csv", mode="w", newline="") as test_file:
    for image_file in read_val:
        text_file = image_file.replace(".png", ".txt")
        data = [image_file, text_file]
        writer = csv.writer(test_file)
        writer.writerow(data)