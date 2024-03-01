### Region-Analysis
The goal of this assignment is to use Linked Lists to manage binary regions identified in an image.

The objective of this project is to use linked list as a data structure to keep track of regions identified based on connected component analysis performed in the previous assignment. In this assignment, we want to enhance the previously developed RegionAnalysis class such that each region, also called a Binary Labeled OBject (BLOB), is maintained as an object along its own set of properties or attributes. More importantly, we want to allow for the selection of a subset of these BLOBs based on their properties, or in other words, allow mechanisms to filter or remove certain BLOBs based on their properties.

In enhancing the RegionAnalysis class, we want to create a new class to manage each BLOB. This class should include attributes to represent a BLOB as well as its properties. A predefined class Blob is implemented for this purpose and its constructor already given. The constructor defines the representation of a BLOB to be a list of pixel locations that belong to the BLOB, specifically stored as a Linked List. In addition, properties of the BLOB are to be maintained such as the color of the BLOB, its size or area, its centroid, a bounding box representation of a rectangle that bounds the BLOB, and a unique id/number. Methods to manage these attributes or to compute them are to be included in the class.

Further, we want to enhance the RegionAnalysis class to include a way to store the BLOBs or regions computed from performing the connected component analysis. We specifically want to store these BLOBs as a Linked List, where each node in the list is an object of class Blob. As a result, each node will include all the attributes we have defined in the class Blob. We also want to include a blob image, which would be an image of the blobs after filtering or removal of a subset of regions resulting from connected component analysis. Finally, we want to know the count of BLOBs after filtering. The RegionAnalysis class needs to also include additional methods to manage the new attributes added.

In this assignment, you are given the implementation of the Linked List data structure in the file dpcourse/LinkedList.py. You are also given the full implementation of connected component analysis using both the Stack and Queue data structures in the file imageops/RegionAnalysis.py. In addition, a skeleton implementation of the class Blob is also provided in the file imageops/RegionAnalysis.py along with definitions of specific methods to be implemented. Finally, additional attributes and methods to manage all connected component regions are defined in the class RegionAnalysis.

#### Implement the following functionalities to support operations on a BLOB as methods in the class Blob:
  * add - method to add pixel location that is part of the blob
  * id - get and set methods to provide a unique id for the blob
  * color - get and set methods for the color value as a trichromat to represent the color of the blob; e.g.,     [a, b, c]
  * centroid - method to compute the centroid or mean position of the blob, specified as [centroid_x, centroid_y]
  * size - method to compute the size or area of the blob (same as total count of pixels in the blob)
  * bounding box - get and set methods to compute and return the rectangle coordinates that bound the blob, specified as [min_x, min_y, max_x, max_y]

#### Implement the following functionalities to support operations for the enhanced RegionAnalysis class:
  * floodfill methods using stack/queue - these methods need to be modified so that the methods generate a Blob that includes all the pixel locations belonging to that Blob and returns the object.
  * connected component analysis methods for stack/queue - these methods need to be modified so that all resulting Blobs and relevant attributes are stored in the linked list (self.regions).
  * set blob image - method that takes a filtering argument and processes all BLOBs to filter out the ones that are less than the argument value and use the remaining to generate a blob image. In this assignment, we are using the size/area as the filtering attribute.
      * As an example, if the argument value is 15, all Blobs of size greater than 15 would shown in the blob image. In addition, each blob would include a bounding box shown in white (pixel value [255, 255, 255] in the blob image.
  * get blob image - method that returns the blob image generated in the method set blob image
  * get number of blobs - method that return the number of blob after filtering based on argument value provided in the set blob image method.
  

You are given the driver program (ca-03.py) that calls methods to perform connected component analysis as well as blob filtering. Once you finish writing your methods, the driver program will test connected component analysis and blob filtering using either the Stack or Queue implementation based on the input argument. A blob image will be generated based on the argument value passed from the driver program.
