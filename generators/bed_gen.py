from random import choice, randint
import os
import cv2


def bed_generator(first_prod_id, first_set_id, n):
    images = [f for f in os.listdir(os.path.join('images', 'beds'))]
    print(len(images))

bed_generator()
