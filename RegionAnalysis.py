__author__ = "Shishir Shah"
__version__ = "1.0.0"
__copyright__ = "Copyright 2022 by Shishir Shah, Quantitative Imaging Laboratory (QIL), Department of Computer  \
                Science, University of Houston.  All rights reserved.  This software is property of the QIL, and  \
                should not be distributed, reproduced, or shared online, without the permission of the author."


import sys
from imageops.DSImage import MyImage as MyImage
from dpcourse import Stack
from dpcourse import Queue
from dpcourse import LinkedList
import random
import math


class Blob:

    ''' Already defined is the constructor that initializes
    the attributes to be maintained to an identified binary
    labeled object (region) in an image.'''
    def __init__(self):
        '''This is the linked list to store all pixel positions belonging to the blob (region).'''
        self.region = LinkedList.LinkedList()

        '''This is the color assigned to be blob (region) during connected component analysis.'''
        self.color = [0, 0, 0]

        '''This is the centroid specified as x and y image coordinate for the blob (region).'''
        self.centroid_x = 0
        self.centroid_y = 0

        '''This is the total number of pixels that belong to the blob (region), 
        also considered as the area of the blob.'''
        self.size = 0

        '''This is the bounding box coordinates for the blob specified
        as [min_x, min_y, max_x, max_y].'''
        self.bbox = []

        '''This is the id or a count given to the blob considering that each blob is unique.'''
        self.id = 0

    #Do we use the functions in the linked list class for the below functions

    '''Write a method that adds the pixel location given 
    as 'x_pos' and 'y_pos' to the linked list that maintains 
    a list of pixels belonging to a particular region.'''
    '''Pixel positions are stored in the region attribute, so we would use the add or append function of the
    linked list class'''
    def add(self, x_pos, y_pos):
        #not sure whether to use the add or append function here
        self.region.add(x_pos, y_pos)

    '''Write a method to set the id for the blob (region) 
    given the input argument 'num'.'''
    def set_id(self, num):
        self.id = num

    '''Write a method to get the id for the blob (region).'''
    def get_id(self):
        return self.id

    '''Write a method to set the color for the blob (region) 
    such that it can be used to generate a blob image.'''
    def set_color(self, color):
        # pass
        self.color = color

    '''Write a method to get the color for the blob (region) 
    such that it can be used to generate a blob image.'''
    def get_color(self):
        return self.color


    '''Write a method to return the centroid of the blob (region).'''
    #need to calculate the centroid(using boundary box)
    def get_centroid(self):
        x_min, y_min, x_max, y_max = self.bbox
        return (x_min + x_max)/2, (y_min + y_max)/2


    '''Write a method to return the size (area) of the blob (region).'''
    #this is same as total count of pixels in the blob(need to see how many nodes are in region object)
    #not sure to do return self.size() instead
    def get_size(self):
        return self.region.size()

    '''Write a method to set the bounding box of the blob (region).
    The bounding box should be specified as the upper left coordinates (min_x, min_y)
    and the lower right coordinates (max_x, max_y) that surrounds the blob (region).'''
    #how do we get the coordinates of the bounding box??
    #use centroid to get the bounding box coordinates and size
    #do we iterate through all the pixel locaitons to find the
    def set_bbox(self):
        # coords = []
        #
        # #storing the pixel locaitons into a list
        # current = self.region.head
        # while current is not None:
        #     coords.append(current.data)
        #     current = current.next

        #iterate through the list to get the min_x, min_y, max_x, and max_y



        #store these min, max x and y coordinates into the  blob attribute
        #self.bbox = min_x, min_y, max_x, max_y




    '''Write method to return the bounding box of the blob (region).'''
    def get_bbox(self):
        return self.bbox


class RegionAnalysis:

    def __init__(self, image):
        try:
            if not isinstance(image, MyImage):
                raise TypeError
        except TypeError:
            print('Image has to be type MyImage.')
            sys.exit(2)
        try:
            if image.get_channels() != 1:
                raise TypeError
        except TypeError:
            print("Image has to be binary image.")
            sys.exit(2)
        self.binary_image = image
        self.height = image.get_height()
        self.width = image.get_width()
        self.label_image = MyImage()
        self.label_image.new_image(self.width, self.height, [0, 0, 0])
        self.num_regions = 0

        '''The following attributes enhance the class implemented in CA-02.'''

        '''This is the linked list of all blobs (regions) in the image after 
        completing connected component analysis.'''
        self.regions = LinkedList.LinkedList()
        '''This is the blob image that would show blobs (regions) of interest.'''
        self.blob_image = MyImage()
        '''This is the initiated blob image, with all pixels being black.'''
        self.blob_image.new_image(self.width, self.height, [0, 0, 0])
        '''This is the total number of blobs (regions) of interest.'''
        self.num_blobs = 0

    '''This method generates a random trichromat value as a list to be used
    in assigning a color value.'''
    def __generate_random_labelvalue(self):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        return [a, b, c]



    '''This method returns the binary image generated as a 
    result of the thresholding operation.'''
    def get_binary_image(self):
        return self.binary_image

    '''This method returns the image with all identified regions such that
    each groups of pixels identified as belong to a region are assigned the 
    same color value.'''
    def get_label_image(self):
        return self.label_image

    '''This method returns the total number of regions resulting from connected
    component analysis.'''
    def get_num_regions(self):
        return self.num_regions

    '''This method performs connected component analysis on the binary image
    using the Stack data structure. This method will need to be modified to accept
    the return value from the modified floodfill method and to add generated blob (region)
    to the linked list that stores all blobs (self.regions).'''
    def connected_components_stack(self):
        data = self.binary_image.get_image_data().copy()
        self.num_regions = 0

        for i in range(self.width):
            for j in range(self.height):
                #we found a new region/blob
                if int(data[j, i]) == 255:
                    self.num_regions += 1
                    #add the region(blob) generated from flood_fill with all the attributes associated to that region to the regions attribute
                    #__floodfill_stack would return a region with pixel locations
                    self.regions.add(self.__floodfill_stack(data, i, j))

                    #how do we make sure we store relevant attributes are stored into linked list as well
                    #what should we be returning
        return self.regions

    '''This method performs connected component analysis on the binary image
    using the Queue data structure. This method will need to be modified to accept
    the return value from the modified floodfill method and to add generated blob (region)
    to the linked list that stores all blobs (self.regions).'''
    def connected_components_queue(self):
        data = self.binary_image.get_image_data().copy()
        self.num_regions = 0

        for i in range(self.width):
            for j in range(self.height):
                #we found a new region/blob
                if int(data[j, i]) == 255:
                    self.num_regions += 1
                    #add the region(blob) generated from flood_fill with all the attributes associated to that region to the regions attribute
                    #__floodfill_queue would return a region with pixel locations
                    self.regions.add(self.__floodfill_queue(data, i, j))
        return self.regions


    '''This is a private method that performs the floodfill algorithm using
    the Stack data structure.  You may need to modify this method to manage
    each identified blob (region) using the given Blob class and the 
    enhanced RegionAnalysis class. This private method should return a blob (region).'''
    def __floodfill_stack(self, temp, x, y):
        ny = [-1, -1, -1, 0, 0, 1, 1, 1]
        nx = [-1, 0, 1, -1, 1, -1, 0, 1]

        frontier = Stack.Stack()

        pixel_value = int(temp[y, x])
        # target color is same as replacement
        if pixel_value != 255:
            return

        frontier.push([x, y]) #x, y is the coordinates of target value

        label_value = self.__generate_random_labelvalue() #genereate random label value

        self.label_image.set_image_pixel(x, y, label_value) #change target color to randomized label color
        temp[y, x] = 0

        while not frontier.is_empty():
            loc = frontier.pop()
            x = loc[0]
            y = loc[1]
            for k in range(len(ny)):
                # if the adjacent pixel at position (x + nx[k], y + ny[k]) is
                # is valid and has the same color as the current pixel
                if 0 <= y + ny[k] < self.height and 0 <= x + nx[k] < self.width: #checking if within bounds
                    if int(temp[y + ny[k], x + nx[k]]) == pixel_value: #pixel value belongs to that blob
                        frontier.push([x + nx[k], y + ny[k]])
                        self.label_image.set_image_pixel(x + nx[k], y + ny[k], label_value)
                        temp[y + ny[k], x + nx[k]] = 0
                        #because we found a neighboring pixel with the target value, we add that pixel location to the region blob
                        # function ends when no neighboring pixels have the same target value
                        self.region.add(x + nx[k], y + ny[k])
        return self.region

    '''This is a private method that performs the floodfill algorithm using
    the Queue data structure. You may need to modify this method to manage
    each identified blob (region) using the given Blob class and the 
    enhanced RegionAnalysis class.  This private method should return a blob (region).'''
    def __floodfill_queue(self, temp, x, y):
        ny = [-1, -1, -1, 0, 0, 1, 1, 1]
        nx = [-1, 0, 1, -1, 1, -1, 0, 1]

        # create a queue and enqueue starting pixel
        q = Queue.Queue()
        # get the target color
        pixel_value = int(temp[y, x])

        # target color is same as replacement
        if pixel_value != 255:
            return

        q.enqueue([x, y])
        label_value = self.__generate_random_labelvalue()
        self.label_image.set_image_pixel(x, y, label_value)
        temp[y, x] = 0

        # break when the queue becomes empty
        while not q.is_empty():
            # dequeue front node and process it
            loc = q.dequeue()
            x = loc[0]
            y = loc[1]

            # process all eight adjacent pixels of the current pixel and
            # enqueue each valid pixel
            for k in range(len(ny)):
                # if the adjacent pixel at position (x + nx[k], y + ny[k]) is
                # is valid and has the same color as the current pixel
                if 0 <= y + ny[k] < self.height and 0 <= x + nx[k] < self.width:
                    if int(temp[y + ny[k], x + nx[k]]) == pixel_value:
                        q.enqueue([x + nx[k], y + ny[k]])
                        self.label_image.set_image_pixel(x + nx[k], y + ny[k], label_value) #replace target value with the random generated label value
                        temp[y + ny[k], x + nx[k]] = 0 #set node as visited/marked
                        self.region.add(x + nx[k], y + ny[k])
        return self.region

    '''Write the method that performs the selection of subset of blobs (regions) from
    all the regions identified after connected component analysis and generates the
    blob image to include those blobs (region) along with a bounding box surrounding
    each of the blobs (regions).'''
    def set_blob_image(self, size_threshold=0):
        #need to use self.regions
        #need to iterate through each blob(region) in the regions attribute and check each of the sizes(number of locaiotn pixls)

        current = self.regions.head
        while current is not None:
            #if region satisfies threshold, add it to the blob image
            if current.size() >= size_threshold:
                #not sure how we add the regions that satisfy the threshold to the label image

                #need to pass in the bounding box of each region that satisfies condiiton as well as the intensity value for the pixels in the range of the bounding box
                self.blob_image.set_image_pixels(current.get_bbox(), [255, 255, 255])
            #iterate to the next region
            current = current.next


    '''Write the method that returns the blob image.'''
    def get_blob_image(self):
        return self.blob_image


    '''Write the method that returns the total number of blobs (regions) 
    resulting from the selection/filtering operation specified to be performed.'''
    #set_blob_image is called before the get functions(get_blob_image, get_num_blobs)
    def get_num_blobs(self):
        return self.num_blobs
