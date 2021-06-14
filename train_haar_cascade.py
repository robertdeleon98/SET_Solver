import cv2
import os
import numpy
import kaggle

# === IMPORT NEGATIVE IMAGES FOR TRAINING (RUN ONCE) ===
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files('muhammadkhalid/negative-images', path='image-data', unzip=True)

# === RESIZE IMAGES (RUN ONCE) ===
count = 1
for subdir, dirs, files in os.walk("image-data/positive-images"):
    for file in files:
        try:
            print(str(count) + ' ' + os.path.join(subdir, file))
            img = cv2.imread(os.path.join(subdir, file))
            resized_img = cv2.resize(img, (150, 100))
            cv2.imwrite("image-data/positive-images/" + str(count) + ".jpg", resized_img)
            count += 1
        except Exception as e:
            print(str(e))

count = 1
for subdir, dirs, files in os.walk("image-data/Negative Images"):
    for file in files:
        try:
            print(str(count) + ' ' + os.path.join(subdir, file))
            img = cv2.imread(os.path.join(subdir, file))
            resized_img = cv2.resize(img, (150, 100))
            cv2.imwrite("image-data/negative-images/" + str(count) + ".jpg", resized_img)
            count += 1
        except Exception as e:
            print(str(e))

# === WRITE DESCRIPTION FILES (RUN ONCE) ===
for img in os.listdir("image-data/positive-images"):
    line = img + " 1 0 0 150 100\n"
    with open("info.dat", "a") as f:
        f.write(line)
for img in os.listdir("image-data/negative-images"):
    line = img + "\n"
    with open("bg.txt", "a") as f:
        f.write(line)
