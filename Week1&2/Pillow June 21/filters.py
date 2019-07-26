#author: Johana
#module name:filters
#Date: June 21, 2019


from PIL import Image
def load_img(name):
    myImage= Image.open(name)
    return myImage
load_img("rose.jpg")

def show_img(img):
    img.show()
#show_img(load_img("rose.jpg"))

def save_img(img, name):
    img.save(name, 'JPEG')

def obamicon(img):
    
    pixels= img.getdata()

    new_pixels =[]
    
    darkblue=(0,51,76)
    red=(217,26,33)
    lightblue=(112,150,158)
    yellow=(252,227,166)
    
    for p in pixels:
        intensity=p[0]+p[1]+p[2]

        if intensity<182:
            new_pixels.append(darkblue)
        elif intensity>=182 and intensity<364:
            new_pixels.append(red)
        elif intensity>=364 and intensity<546:
            new_pixels.append(lightblue)
        else:
            new_pixels.append(yellow)
            
    newImg= Image.new("RGB",img.size)
    newImg.putdata(new_pixels)
    newImg.show()
    return newImg
