"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 5 Part 0 EC
03/04/2018"""

'''This program contains functions to properly format RGB pixel values to
create images of the flags of the Finland, Republic of Congo, the Bahamas,
and Sudan in .ppm format'''

def get_header(width, height):
    '''Takes in desired image dimensions and gives formatted file header
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted header
    '''
    return 'P3\n' + width + ' ' + height + '\n' + '255' + '\n'

def main(flag):
    '''Takes in desired image dimensions and creates flag of Netherlands
        in .ppm file
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

def finland(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of Finland
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    blue = '0 53 128 '
    white = '255 255 255 '
    row1 = (white * (5 * width // 18)) + (blue * (width // 6)) + (white * (5 * (width // 9)))
    row2 = blue * width
    flag = (row1 * (4 * height // 11)) + '\n' + (row2 * (3 * height // 11)) + '\n' + (row1 * (4 * height // 11))
    return flag

def congo(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of the Republic of Congo
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    ratio1 = (2 * width // 3)
    ratio2 = (width // 3)
    ratio3 = 0
    green = '0 149 67 '
    yellow = '251 222 74 '
    red = '220 36 31 '
    flag = ''
    for i in range(height):
        row = (green * ratio1) + (yellow * ratio2) + (red * ratio3) + '\n'
        flag += row
        ratio3 += 1
        ratio1 -= 1
    return flag
 

def bahamas(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of the Bahamas
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    ratio1 = 0
    ratio2 = width
    black = '0 0 0 '
    blue = '0 171 201 '
    yellow = '250 224 66 '
    flag = ''
    for i in range(height):
        if i < (height // 3):
            row = (black * ratio1) + (blue * ratio2) + '\n'
            flag += row
            ratio1 += 2  
            ratio2 -= 2
        elif i > (height // 3) and i < (height // 2):
            row = (black * ratio1) + (yellow * ratio2) + '\n'
            flag += row
            ratio1 += 2
            ratio2 -= 2
        elif i > (height // 2) and i < (2 * height // 3):
            row = (black * ratio1) + (yellow * ratio2) + '\n'
            flag += row
            ratio1 -= 2
            ratio2 += 2
        elif i > (2 * height // 3):
            row = (black * ratio1) + (blue * ratio2) + '\n'
            flag += row
            ratio1 -= 2
            ratio2 += 2
    return flag
    
def sudan(width, height):
    '''Takes in desired image dimensions and gives pixel values
        for flag of Sudan
        Args:
            width (str): width of image
            height (str): height of image
        Returns:
            string: formatted pixels of flag
    '''
    width = int(width)
    height = int(height)
    ratio1 = 0
    ratio2 = width
    green = '0 114 41 '
    red = '210 16 52 '
    black = '0 0 0 '
    white = '255 255 255 '
    flag = ''
    for i in range(height):
        if i < (height // 3):
            row = (green * ratio1) + (red * ratio2) + '\n'
            flag += row
            ratio1 += 1  
            ratio2 -= 1
        elif i > (height // 3) and i < (height // 2):
            row = (green * ratio1) + (white * ratio2) + '\n'
            flag += row
            ratio1 += 1
            ratio2 -= 1
        elif i > (height // 2) and i < (2 * height // 3):
            row = (green * ratio1) + (white * ratio2) + '\n'
            flag += row
            ratio1 -= 1
            ratio2 += 1
        elif i > (2 * height // 3):
            row = (green * ratio1) + (black * ratio2) + '\n'
            flag += row
            ratio1 -= 1
            ratio2 += 1
    return flag
    

