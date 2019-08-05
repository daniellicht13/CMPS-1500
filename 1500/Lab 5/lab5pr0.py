"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 5 Part 0
03/04/2018"""

'''This program contains functions to properly format RGB pixel values to
create images of the flags of the Netherlands, Nigeria, and the United
Arab Emirates in .ppm format'''

def get_header(width, height):
    '''Takes in desired image dimensions and gives formatted file header
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted header
    '''
    return 'P3\n' + str(width) + ' ' + str(height) + '\n' + '255' + '\n'

def netherlands(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of Netherlands
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    red = ('255 0 0 ' * width) * (height // 3)
    white = ('255 255 255 ' * width) * (height // 3)
    blue = ('0 0 255 ' * width) * (height // 3)
    flag = red + white + blue
    return flag

def main(flag):
    '''Takes in desired image dimensions and creates flag of the country in body
        of code (Netherlands, Nigeria, or UAE) in a .ppm file
        Args:
            None
        Returns:
            string: .ppm file of flag image
    '''
    width = input('Please, enter width: ')
    height = input('Please, enter height: ')
    filename = input('Please, enter output file name: ')
    f = open(filename, 'w')
    f.write(get_header(width, height))
    f.write(flag(width, height))
    f.close()
    print('The output has been written to ' + filename)
    print('View the result in XnView')
    return

def nigeria(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of Nigeria
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    green = '0 135 81 '
    white = '255 255 255 '
    row = (green * (width // 3)) + (white * (width // 3)) + (green * (width // 3))
    flag = row * height
    return flag

def uae(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of UAE
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    red = '255 0 0 '
    green = '0 115 47 '
    white = '255 255 255 '
    black = '0 0 0 '
    row1 = (red * (width // 4)) + (green * (3 * width // 4))
    row2 = (red * (width // 4)) + (white * (3 * width // 4))
    row3 = (red * (width // 4)) + (black * (3 * width // 4))
    flag = row1 * (height // 3) + row2 * (height // 3) + row3 * (height // 3)
    return flag

    
    
