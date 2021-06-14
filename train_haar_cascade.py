# === IMPORT NEGATIVE IMAGES FOR TRAINING (RUN ONCE) ===
# import kaggle
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files('muhammadkhalid/negative-images', path='image-data', unzip=True)

# === RESIZE IMAGES (RUN ONCE) ===
import cv2
import os
import numpy

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
