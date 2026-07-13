import cv2 as cv
import numpy as np
class images:
    def __init__(self, photo_path):
        self.image=cv.imread(photo_path) 
        self.photo_path = photo_path
        if self.image is None:
            print(f"wrong path {photo_path}")
            self.height = 0
            self.width = 0
    def check_path(self):
        if self.image is None:
            print("wrong path!")
            return
    def size_of (self):
        print(f"the hight is {self.image.shape[0]}px,and the width is {self.image.shape[1]}px")
    def turn_gray(self):
        new_img=cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
        return new_img
    def flip_horizontal(self):
        return cv.flip(self.image,1)
    def flip_vertical(self):
        return cv.flip(self.image,0)
    def resize(self,new_width,new_height):
        return cv.resize(self.image, (new_width, new_height))
    def brightness(self,value):
        bright=self.image.astype(np.int32)+value
        bright=np.clip(bright,0,255)
        return bright.astype(np.uint8)
    def contrast(self,factor):
        img = self.image.astype(np.int32)
        mean=np.mean(img)
        contrast_img=(img-mean)*factor+mean
        contrast_img=np.clip(contrast_img,0,255)
        return contrast_img.astype(np.uint8)
    def negative(self):
        return 255-self.image
    def blur(self,karnel_size=5):
        return cv.blur(self.image,(karnel_size,karnel_size))
    def threshold(self,thresh=127,maxval=255):
        gray_img=cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
        val,binary=cv.threshold(gray_img,thresh,maxval,cv.THRESH_BINARY)
        return binary
    def swap_colors(self,color_1=0,color_2=1):
        swapped=self.image.copy()
        temp=swapped[:,:,color_1]
        swapped[:,:,color_1]=swapped[:,:,color_2]
        swapped[:,:,color_2]=temp
        return swapped
    def show_image(self, img, window_name="Image"):
        if img is None:
            print("No image to display!")
            return
        cv.imshow(window_name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    def save_image(self, img, path):
        if img is None:
            print("No image to save!")
            return
        cv.imwrite(path, img)
        print(f"Image saved to: {path}")
def display_menu():
    print("""
Image processing tool
=====================
0) exit
1) show the original image
2) show image info
3) convert to grayscale 
4) flip horizontal
5) flip vertical
6) resize image
7) edit the brightness
8) edit the contrast
9) negative effect
10) blur image
11) threshold (black & white)
12) swap colors
13) save image
===================== """)

def get_choice():
    try:
        choice=int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("invaled input")
        return -1
def main():
    image_path=input("Enter the image path: ")
    img=images(image_path)
    
    if img.image is None:
        print("failed to load image")
        return
    current_result=None
    while True:
        display_menu()
        choice=get_choice()
        
        
        if choice==0:
            print("Good bye...")
            break
        elif choice==1:
            img.show_image(img.image,"original image")
        elif choice==2:
            img.size_of()
        elif choice==3:
            current_result=img.turn_gray()
            img.show_image(current_result,"gray")
        elif choice==4:
            current_result=img.flip_horizontal()
            img.show_image(current_result,"horizontal flip")
        elif choice==5:
            current_result=img.flip_vertical()
            img.show_image(current_result,"vertical flip")
        elif choice==6:
            try:
                new_width = int(input("Enter new width: "))
                new_height = int(input("Enter new height: "))
                current_result = img.resize(new_width, new_height)
                img.show_image(current_result, f"Resized: {new_width}x{new_height}")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        elif choice==7:
            try:
                value = int(input("Enter brightness value (-255 to 255): "))
                current_result = img.brightness(value)
                img.show_image(current_result, f"Brightness: {value}")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == 8:
            try:
                factor = float(input("Enter contrast factor (0.1 to 3.0): "))
                current_result = img.contrast(factor)
                img.show_image(current_result, f"Contrast: {factor}")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice==9:
            current_result = img.negative()
            img.show_image(current_result, "Negative Effect")
        elif choice==10:
            try:
                kernel = int(input("Enter kernel size (3, 5, 7, 9, ...): "))
                if kernel % 2 == 0:
                    print("Kernel size must be odd! Using 5.")
                    kernel = 5
                current_result = img.blur(kernel)
                img.show_image(current_result, f"Blur: {kernel}x{kernel}")
            except ValueError:
                print("Invalid input! Using default kernel size 5.")
                current_result = img.blur(5)
                img.show_image(current_result, "Blur: 5x5")
        elif choice==11:
            try:
                thresh = int(input("Enter threshold value (0-255): "))
                current_result = img.threshold(thresh)
                img.show_image(current_result, f"Threshold: {thresh}")
            except ValueError:
                print("Invalid input! Using default threshold 127.")
                current_result = img.threshold(127)
                img.show_image(current_result, "Threshold: 127")
        elif choice == 12:
            print("Color Channels: 0=Blue, 1=Green, 2=Red")
            try:
                color_1 = int(input("Enter first channel: "))
                color_2 = int(input("Enter second channel: "))
                if color_1 not in [0, 1, 2] or color_2 not in [0, 1, 2]:
                    print("Invalid channel numbers! Using 0 and 1.")
                    color_1, color_2 = 0, 1
                current_result = img.swap_colors(color_1, color_2)
                img.show_image(current_result, f"Swapped: {color_1}<->{color_2}")
            except ValueError:
                print("Invalid input! Using default swap (0 and 1).")
                current_result = img.swap_colors(0, 1)
                img.show_image(current_result, "Swapped: Blue<->Green") 
        elif choice==13:
            if current_result is None:
                print("No image to save! Please apply a filter first.")
                continue
            save_path = input("Enter save path (e.g., output.jpg): ")
            img.save_image(current_result, save_path)
        else:
            print("invalid choice!")
""""============="""
if __name__=="__main__":
   main()        