import matplotlib
matplotlib.use('Agg')
import joblib
import numpy as np
from scipy import misc

from skimage import data
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage import measure
from skimage.measure import regionprops
from skimage.transform import resize

import pickle
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import simplejson as json
import cv2
import os
from werkzeug.utils import secure_filename
import imutils
import sys
import imageio

def PlateDetection(file):
    filename = file
    #car_image = imread(filename, as_gray=True)
    car_image = imageio.imread(filename, as_gray=True)
    #car_image = imutils.rotate(car_image, 270)
    # car_image = imread("car.png", as_gray=True)
    # it should be a 2 dimensional array
    #print(car_image.shape)

    # the next line is not compulsory however, a grey scale pixel
    # in skimage ranges between 0 & 1. multiplying it with 255
    # will make it range between 0 & 255 (something we can relate better with
    car_image = cv2.resize(car_image, (600,600) )
    gray_car_image = car_image * 255
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(gray_car_image, cmap="gray")
    threshold_value = threshold_otsu(gray_car_image)
    binary_car_image = gray_car_image > threshold_value
    # print(binary_car_image)
    ax2.imshow(binary_car_image, cmap="gray")
    # ax2.imshow(gray_car_image, cmap="gray")
    # plt.show()

    # CCA (finding connected regions) of binary image


    # this gets all the connected regions and groups them together
    label_image = measure.label(binary_car_image)

    # print(label_image.shape[0]) #width of car img

    # getting the maximum width, height and minimum width and height that a license plate can be
    plate_dimensions = (0.03*label_image.shape[0], 0.08*label_image.shape[0], 0.15*label_image.shape[1], 0.3*label_image.shape[1])
    plate_dimensions2 = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.4*label_image.shape[1])
    min_height, max_height, min_width, max_width = plate_dimensions
    plate_objects_coordinates = []
    plate_like_objects = []

    fig, (ax1) = plt.subplots(1)
    ax1.imshow(gray_car_image, cmap="gray")
    flag =0
    # regionprops creates a list of properties of all the labelled regions
    for region in regionprops(label_image):
        # print(region)
        if region.area < 50:
            #if the region is so small then it's likely not a license plate
            continue
            # the bounding box coordinates
        min_row, min_col, max_row, max_col = region.bbox
        # print(min_row)
        # print(min_col)
        # print(max_row)
        # print(max_col)

        region_height = max_row - min_row
        region_width = max_col - min_col
        # print(region_height)
        # print(region_width)

        # ensuring that the region identified satisfies the condition of a typical license plate
        if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
            flag = 1
            plate_like_objects.append(binary_car_image[min_row:max_row,
                                    min_col:max_col])
            plate_objects_coordinates.append((min_row, min_col,
                                            max_row, max_col))
            rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row, edgecolor="red",
                                        linewidth=2, fill=False)
            ax1.add_patch(rectBorder)
            # let's draw a red rectangle over those regions
    #if(flag == 1):
        # print(plate_like_objects[0])
        #plt.show()

    if(flag==0):
        min_height, max_height, min_width, max_width = plate_dimensions2
        plate_objects_coordinates = []
        plate_like_objects = []

        fig, (ax1) = plt.subplots(1)
        ax1.imshow(gray_car_image, cmap="gray")

        # regionprops creates a list of properties of all the labelled regions
        for region in regionprops(label_image):
            if region.area < 50:
                #if the region is so small then it's likely not a license plate
                continue
                # the bounding box coordinates
            min_row, min_col, max_row, max_col = region.bbox
            # print(min_row)
            # print(min_col)
            # print(max_row)
            # print(max_col)

            region_height = max_row - min_row
            region_width = max_col - min_col
            # print(region_height)
            # print(region_width)

            # ensuring that the region identified satisfies the condition of a typical license plate
            if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
                # print("hello")
                plate_like_objects.append(binary_car_image[min_row:max_row,
                                        min_col:max_col])
                plate_objects_coordinates.append((min_row, min_col,
                                                max_row, max_col))
                rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row, edgecolor="red",
                                            linewidth=2, fill=False)
                ax1.add_patch(rectBorder)
                # let's draw a red rectangle over those regions
        # print(plate_like_objects[0])
        #plt.show()
    if len(plate_like_objects) == 0 :
        sys.exit("Image input Error has occurred")
    license_plate = np.invert(plate_like_objects[0])

    labelled_plate = measure.label(license_plate)

    fig, ax1 = plt.subplots(1)
    ax1.imshow(license_plate, cmap="gray")
    # the next two lines is based on the assumptions that the width of
    # a license plate should be between 5% and 15% of the license plate,
    # and height should be between 35% and 60%
    # this will eliminate some
    character_dimensions = (0.35*license_plate.shape[0], 0.60*license_plate.shape[0], 0.05*license_plate.shape[1], 0.15*license_plate.shape[1])
    min_height, max_height, min_width, max_width = character_dimensions

    characters = []
    counter=0
    column_list = []
    for regions in regionprops(labelled_plate):
        y0, x0, y1, x1 = regions.bbox
        region_height = y1 - y0
        region_width = x1 - x0

        if region_height > min_height and region_height < max_height and region_width > min_width and region_width < max_width:
            roi = license_plate[y0:y1, x0:x1]

            # draw a red bordered rectangle over the character.
            rect_border = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, edgecolor="red",
                                        linewidth=2, fill=False)
            ax1.add_patch(rect_border)

            # resize the characters to 20X20 and then append each character into the characters list
            resized_char = resize(roi, (20, 20))
            characters.append(resized_char)

            # this is just to keep track of the arrangement of the characters
            column_list.append(x0)
    # print(characters)
    #plt.show()

    #print("Loading model")
    filename = './flaskblog/finalized_model.sav'
    model = pickle.load(open(filename, 'rb'))

    #print('Model loaded. Predicting characters of number plate')
    classification_result = []
    # characters = session['plate_characters']

    for each_character in characters:
        # converts it to a 1D array
        each_character = each_character.reshape(1, -1);
        result = model.predict(each_character)
        classification_result.append(result)

    #print('Classification result')
    #print(classification_result)

    plate_string = ''
    for eachPredict in classification_result:
        plate_string += eachPredict[0]

    #print('Predicted license plate')
    #print(plate_string)
    column_list_copy = column_list[:]
    column_list.sort()
    rightplate_string = ''
    for each in column_list:
        rightplate_string += plate_string[column_list_copy.index(each)]

    #print('License plate')
    return rightplate_string
        
 #'./static/images/1.png'
#if __name__ == '__main__':
#    driver('./static/images/1.png')
