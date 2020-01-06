import utilities

def rotate_90_degrees(image_array, direction = 1):
        '''(list, num) -> list
        returns a rotated image of the giver image_array. if the user enters 1, it will rotate clockwise 90 degrees, if -1 is entered, it will rotate 90 degrees anticlock wise. 
        examples:
        >>>rotate_90_degrees([[1, 1, 0], [0, 0, 0], [0, 0, 1]], -1)
        [[0, 0, 1], [1, 0, 0], [1, 0, 0]]
        >>>rotate_90_degrees([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 1)
        [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
        '''
        size1 = len(image_array)
        size2 = len(image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        if direction == 1:
                                output_array[i][j]=image_array[size1-j-1][i]
                        elif direction == -1:
                                output_array[i][j]=image_array[j][size2-i-1]
        return output_array

def flip_image(image_array, axis = 0):
        '''(list, num) -> list
        returns an imaged flipped on different axis. if number entered is 0, it will be flipped along the y axis, if number entered is 1, it will be flipped along x axis, if number entered is -1, it will be flipped along the x=y axis
        examples:
        >>>flip_image([[1, 2, 0], [0, 0, 0], [0, 0, 1]], -1)
        [[1, 0, 0], [0, 0, 2], [0, 0, 1]]
        >>>flip_image([[3, 2, 0], [0, 0, 0], [0, 0, 1]], 1)
        [[0, 2, 3], [0, 0, 0], [1, 0, 0]]
        >>>flip_image([[3, 2, 0], [0, 0, 0], [0, 0, 1]], 0)
        [[0, 0, 1], [0, 0, 0], [3, 2, 0]]
        '''
        size1 = len(image_array)
        size2 = len(image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        if axis == 0:
                                output_array[i][j]=image_array[size1-i-1][j]
                        elif axis == 1:
                                output_array[i][j]=image_array[i][size2-j-1]
                        elif axis == -1:
                                output_array[i][j]=image_array[size1-j-1][size2-i-1]
        return output_array

def invert_grayscale(image_array):
        '''(list) -> list
        return an inverted gray scale image by tranforming every pixel into 255-pixel. can only be used on grayscale images
        examples:
        >>>invert_grayscale([[1, 1, 0], [0, 0, 0], [0, 0, 1]])
        [[254, 254, 255], [255, 255, 255], [255, 255, 254]]
        '''
        size1 = len(image_array)
        size2 = len(image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        value = 255-image_array[i][j]
                        output_array[i][j] = value
        return output_array

def crop(image_array, direction, n_pixels):
        '''(list, string, num) -> list
        returns a cropped image depending on the direction and n-pixels entered. if the direction is 'left', it will crop from the left. This applied for 'right', 'up', 'down'. the n'pixels represent the number of pixels one wants to cut off from the image
        examples:
        >>>crop([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 'up', 1)
        [[0, 0, 0], [0, 0, 1]]
        >>>crop([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 'down', 1)
        [[1, 1, 0], [0, 0, 0]]
        >>>crop([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 'right', 1)
        [[1, 1], [0, 0], [0, 1]]
        >>>crop([[1, 1, 0], [0, 0, 0], [0, 0, 1]], 'left', 1)
        [[1, 0], [0, 0], [0, 0]]
        '''
        size1 = len(image_array)
        size2 = len(image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        output_array[i][j]=image_array[i][j]
        if direction == "left":
                for i in range(size1):
                        for j in range(n_pixels):
                                output_array[i].pop(j)
        elif direction == "right":
                for i in range(size1):
                        for j in range(n_pixels):
                                output_array[i].pop(size2-j-1)
        elif direction == "down":
                for i in range(n_pixels):
                        output_array.pop(-1)
        elif direction == "up":
                for i in range(n_pixels):
                        output_array.pop(0)
        return output_array

def rgb_to_grayscale(rgb_image_array):
        '''(list) -> list
        returns the grayscale image of the original rgb image. This is done by adding up the color numbers r, b, and g into one number that represents a color from black to white valued between 0-255. This does not work on images that are already grayscal
        example:
        >>>rgb_to_grayscale([[[6, 9, 80]], [[7, 9, 0]]])
        [[16.1964], [7.3753]]
        '''
        size1 = len(rgb_image_array)
        size2 = len(rgb_image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        value =rgb_image_array[i][j][0]*0.2989 + rgb_image_array[i][j][1]*0.5870 + rgb_image_array[i][j][2]*0.1140
                        output_array[i][j] = value
        return output_array

def invert_rgb(image_array):
        '''(list) -> list
        returns the inverted colored image of the original image. Does this in a similar matter with the invert_grayscale function
        example:
        >>>invert_rgb([[[6, 9, 80]], [[7, 9, 0]]])
        [[[249, 246, 175]], [[248, 246, 255]]]
        '''
        size1 = len(image_array)
        size2 = len(image_array[0])
        output_array = []
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        for k in range(len(image_array[i][j])):
                                output_array[i][j].append(255 - image_array[i][j][k])
        return output_array

def histogram_equalization(img_array):
        '''(list) -> list
        returns an image that has more evenly distributed pixels throughout the image to allow it to have a better contrast level. This only works with grayscale images
        examples:
        >>>histogram_equalization([[1, 1, 0], [0, 0, 0], [0, 0, 1]])
        [[170, 170, 0], [0, 0, 0], [0, 0, 170]]
        '''
        cdf = [0]*256
        size1 = len(img_array)
        size2 = len(img_array[0])
        output_array = []
        for k in range(0, 256):
                cdf.append(0)
        for i in range(size1):
                output_array.append([])
                for j in range(size2):
                        output_array[i].append([])
                        cdf[img_array[i][j]]+=1
        for i in range(size1):
                for j in range(size2):
                        sum = 0
                        for k in range(0,img_array[i][j]):
                                sum+=cdf[k]
                        output_array[i][j] = sum*255/size1/size2
        return output_array

if (__name__ == "__main__"):
    file = 'gray.png'
    img = utilities.image_to_list(file)
    img2 = histogram_equalization(img)
    utilities.write_image(img2, 'equal2.png')