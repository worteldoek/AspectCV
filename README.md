# AspectCV
AspectCV is a OpenCV Python application for object detection.
  
  
## Table of Contents
1. [General Info](#general-information)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Setup](#setup)
5. [Functional Code](#functional-code)
    1. [Upload image and draw rectangle](#upload-image-and-draw-rectangle)
    2. [Saving rectangle's coordinates](#save-rectangles-coordinates)
        1. [Save as .txt file](#save-as-txt-file)
        2. [INSERT INTO SQL database](#insert-into-sql-database)
6. [GUI](#gui)


## General Info
Cv2 app to draw bounding box and template on image


## Technologies Used
- Conda - version ..
- Python - version 3.10
- OpenCV with Qt backend - version 1.0


## Features
List the ready features here:

- Awesome feature


## Setup
Proceed to how to install / setup one's local environment / get started with the project.

* Install Conda

* Create enviroment w/ Python 3.10

  `> conda create --name py310qt python=3.10`

* Activate enviroment

  Windows:`> activate py310qt`

  Linux, macOS: `> source activate py310qt `

* Use Conda to install OpenCV with Qt backend

  `> conda install -c conda-forge menpo`


## Functional code
  
### Upload image and draw rectangle
To write an OpenCV application that allows users to upload an image as a source image and draw a rectangle around an object, you can follow these steps:
  
> 1. Import the necessary OpenCV libraries and modules.
> 2. Load the source image using cv2.imread().
> 3. Create a function to handle mouse events.
> 4. Create a window to display the image using cv2.namedWindow().
> 5. Set the mouse callback function using cv2.setMouseCallback().
> 6. Use the cv2.rectangle() function to draw the rectangle around the object.
> 7. Save the exact coordinates of the vertices after rotation is done.

```python
import cv2
import math

# Load the image
img = cv2.imread('image.jpg')

# Create a function to handle mouse events
def draw_rect(event, x, y, flags, param):
    global pts, img, img_copy
    
    # Left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        pts = [(x, y)]
        
    # Left button up
    elif event == cv2.EVENT_LBUTTONUP:
        pts.append((x, y))
        
        # Calculate the width and height of the rectangle
        w = int(math.sqrt((pts[0][0]-pts[1][0])**2 + (pts[0][1]-pts[1][1])**2))
        h = int(math.sqrt((pts[1][0]-pts[2][0])**2 + (pts[1][1]-pts[2][1])**2))
        
        # Find the rotation angle
        angle = math.atan2(pts[1][1]-pts[0][1], pts[1][0]-pts[0][0])
        
        # Create a rotation matrix
        M = cv2.getRotationMatrix2D(pts[0], math.degrees(angle), 1)
        
        # Rotate the image
        img_copy = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
        
        # Draw the rotated rectangle
        rect = cv2.boxPoints(((pts[0][0], pts[0][1]), (w, h), math.degrees(angle)))
        rect = np.int0(cv2.transform(np.array([rect]), M))[0]
        cv2.polylines(img_copy, [rect], True, (0, 255, 0), 2)
        
        # Save the coordinates of the vertices
        coords = [tuple(cv2.transform(np.array([[x, y]]), M)[0]) for x, y in rect]
        print(coords)
        

# Create a window to display the image
cv2.namedWindow('image')

# Set the mouse callback function
cv2.setMouseCallback('image', draw_rect)

while True:
    # Display the image
    cv2.imshow('image', img_copy)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cv2.destroyAllWindows()

```

In this example, we use the `cv2.boxPoints()` function to get the coordinates of the rotated rectangle vertices. We then use the `cv2.transform()` function to transform the coordinates using the rotation matrix. Finally, we save the transformed coordinates in a list.

# Drawing rotated rectangles  
  
Here are three possible options to allow the drawing of rotated rectangles:

> 1. Use the `cv2.getRotationMatrix2D()` function to create a rotation matrix and the `cv2.warpAffine()` function to rotate the image.
> 2. Use the `cv2.getAffineTransform()` function to create an affine transformation matrix and the `cv2.warpAffine()` function to apply the transformation to the image.
> 3. Use the `cv2.fillConvexPoly()` function to fill the rectangle with a mask, and the `cv2.getRotationMatrix2D()` function and `cv2.warpAffine()` function to rotate the mask. Then use the `cv2.bitwise_and()` function to mask the original image with the rotated mask.

Option 1 and 2 are used in the example code above. Option 3 is demonstrated in the following code example:

```python
import cv2
import math
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Create a function to handle mouse events
def draw_rect(event, x, y, flags, param):
    global pts, img, img_copy, mask
    
    # Left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        pts = [(x, y)]
        
    # Left button up
    elif event == cv2.EVENT_LBUTTONUP:
        pts.append((x, y))
        
        # Create a mask with the same size as the image
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        
        # Fill the rectangle with white in the mask
        cv2.fillConvexPoly(mask, np.array(pts), (255, 255, 255))
        
        # Find the rotation angle
        angle = math.atan2(pts[1][1]-pts[0][1], pts[1][0]-pts[0][0])
        
        # Create a rotation matrix
        M = cv2.getRotationMatrix2D(pts[0], math.degrees(angle), 1)
        
        # Rotate the mask
        mask_rotated = cv2.warpAffine(mask, M, (img.shape[1], img.shape[0]))
        
        # Mask the original image with the rotated mask
        img_copy = cv2.bitwise_and(img, img, mask=mask_rotated)
        
        # Save the coordinates of the vertices
        coords = [tuple(cv2.transform(np.array([[x, y]]), M)[0]) for x, y in pts]
        print(coords)

# Create a window to display the image
cv2.namedWindow('image')

# Set the mouse callback function
cv2.setMouseCallback('image', draw_rect)

while True:
    # Display the image
    cv2.imshow('image', img_copy)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cv2.destroyAllWindows()
```

In this example, we create a mask with the same size as the image and fill the rectangle with white in the mask using the `cv2.fillConvexPoly()` function. We then rotate the mask using the `cv2.getRotationMatrix2D()` function and `cv2.warpAffine()` function, and use the `cv2.bitwise_and()` function to mask the original image with the rotated mask. Finally, we save the transformed coordinates in a list using the `cv2.transform()` function.

## Saving rectangle's coordinates 

### 1. Save as .txt file
Once the user has drawn a rotated rectangle and the program has saved the exact coordinates of the vertices after rotation, the next step is to save this information. One way to do this is to use a text file to store the coordinates. The following code example demonstrates how to save the coordinates to a text file:

```python
# Open the text file
with open('coordinates.txt', 'w') as f:
    # Write the coordinates to the file
    for coord in coords:
        f.write(str(coord[0]) + ',' + str(coord[1]) + '\n')
```

In this example, we open a text file using the `open()` function with the 'w' mode to write to the file. We then write each coordinate to the file using the `write()` function, separated by a comma and a newline character.


### 2.  Insert to a SQL database
Another way to save the coordinates is to use a database, such as SQLite or MySQL. This allows for easier retrieval and manipulation of the data. The following code example demonstrates how to save the coordinates to an SQLite database:

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('coordinates.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS coords
             (id INTEGER PRIMARY KEY,
              x INT NOT NULL,
              y INT NOT NULL)''')

# Insert the coordinates into the table
for coord in coords:
    c.execute("INSERT INTO coords (x, y) VALUES (?, ?)", (coord[0], coord[1]))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
```

In this example, we first connect to an SQLite database using the `connect()` function. We then create a cursor using the `cursor()` function and create a table using the `execute()` function. We then insert each coordinate into the table using the `execute()` function with placeholders for the x and y values. Finally, we commit the changes using the `commit()` function and close the connection using the `close()` function.

# GUI
Now that we have covered how to allow users to upload an image, draw a rotated rectangle around an object, and save the coordinates of the vertices after rotation, let's look at **3 options** to allow the drawing of rotated rectangles:

> 1. OpenCV `cv2.ROTATED_RECT`: This function can be used to draw a rotated rectangle using the `cv2.rectangle()` function. The `cv2.ROTATED_RECT` function takes as input the center point of the rectangle, its size, and its angle. We can then draw the rotated rectangle using the `cv2.rectangle()` function. This option is straightforward to implement, but it requires some knowledge of trigonometry to calculate the correct size and angle of the rectangle.
> 2. Mouse callback functions: We can use OpenCV mouse callback functions to capture user input and draw a rotated rectangle on the image. This option involves creating a function that is called whenever the user clicks or drags the mouse on the image. The function should update the image with the drawn rectangle and store the coordinates of the vertices. This option is more user-friendly than the first option, but it requires some knowledge of OpenCV mouse callback functions.
> 3. Pygame: Pygame is a Python library that is commonly used for game development, but it can also be used for image manipulation. We can use Pygame to create a GUI that allows the user to draw a rotated rectangle on the image. This option involves creating a Pygame window, loading the image into the window, and creating a rectangle object that the user can drag and rotate. This option is the most user-friendly, but it requires the most programming knowledge.

Overall, the choice of method will depend on the specific requirements  of the application and the skill level of the programmer. Option 1 is  the simplest but requires more mathematical knowledge, while option 3 is the most user-friendly but requires more programming knowledge. Option 2 is a good balance between simplicity and user-friendliness.

The simplest option for making a GUI, apart from **Pygame**, would be to use a Python library such as Tkinter or PyQt. Both of these libraries provide a set of tools for creating graphical user interfaces in Python.

**Tkinter** is a built-in Python library that provides a simple and easy-to-use set of tools for creating GUIs. It is a popular choice for creating small to medium-sized GUI applications in Python. Tkinter provides a set of widgets (such as buttons, labels, and text boxes) that can be used to create the user interface. It also provides a layout manager that allows you to arrange the widgets on the screen.

**PyQt** is another popular GUI toolkit for Python. It provides a wide range of widgets and features for creating GUI applications, including support for multimedia, web browsing, and 3D graphics. PyQt is more powerful than Tkinter, but it also has a steeper learning curve.

Both Tkinter and PyQt are well-documented and have large communities of users who can provide support and guidance. Overall, the choice between Tkinter and PyQt will depend on the specific requirements of the application and the level of experience of the programmer.



The best choice of option for your application will depend on the specific requirements of your project and your level of experience with programming and image processing.

If you have some experience with trigonometry and image processing, and your project requires a simple user interface, then option 1 (using `cv2.ROTATED_RECT`) may be the best choice. It is a straightforward approach that does not require any additional libraries or programming tools.

If you want to provide a more user-friendly interface that allows the user to draw the rotated rectangle on the image directly, then option 2 (using mouse callback functions) would be a good choice. It requires some knowledge of OpenCV mouse callback functions but can provide a simple and intuitive user interface.

If you are comfortable with programming and want to provide a more advanced user interface with additional features, then option 3 (using Pygame or another GUI toolkit) may be the best choice. This option will provide the most flexibility and control over the user interface, but it will require more programming knowledge and additional libraries.

Overall, the best choice of option for your application will depend on your specific needs and your level of experience with programming and image processing.



