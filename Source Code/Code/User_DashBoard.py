#----------!!!_This is the main window where main operation are going to perform_!!!--------------------------
#_____________________________________________________________________________________________________________
#====================================Importing required libraries=============================================
#-------------------------------------------------------------------------------------------------------------

from tkinter.ttk import Label, Button
from tkinter import StringVar, Checkbutton, Tk, Label, Button, messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import simpledialog
import random
import cv2
import numpy as np
import os                                        #___Note:-  {This Library is used to create folder}


#_________________________________________________________________________________________________________
#===================================Creating class========================================================
#---------------------------------------------------------------------------------------------------------



#____________________________________________________________________________________________________________
                    #=======creation function to wrape all task===============
#------------------------------------------------------------------------------------------------------------
class User_Dash_Board_Class:
    def __init__(self, User_Dashboard_Window):

        self.User_Dashboard_Window = User_Dashboard_Window
        self.User_Dashboard_Window.title("ConsoleLancer")
        self.User_Dashboard_Window.geometry("1350x740")

#========================================================================================================
#______________________________________BACK END CODE_____________________________________________________
#---------------------This Code is inderectly cennected with front end code------------------------------
#========================================================================================================


    #==========Creating function for taking sample number from user===================
        def Sample_Number():

            global Sample_Number_R
            USER_INP = simpledialog.askstring(title="Test", prompt="Please Enter The Number of Sample You want")
            Temp_value=USER_INP
            Sample_Number_R = int(Temp_value)

    #============Creating Variable for Checking Condition of Download button================
        self.file = 0
        self.path = 0
        self.filter = 0
        #-----------------Variable For Checking Default Displaye Image ------------
        self.sample_Image = 0

    #======================Creating function to upload file===================================
        def Upload_file():
            self.filename = 0
            self.filename = filedialog.askopenfilename(initialdir='/guis', title="Open An Image File",
                                                       filetypes=(("PNG File", "*.png"), ("All Files", "*.*")))
            #----------Passing Filename Address in sel.file variable for if condition -----------------
            self.file = self.filename
            self.sample_Image = self.filename
            self.filename1 = self.filename2 = self.filename

            #-----Resizing Sample image in 700x270-------------
            my_image = Image.open(self.filename1)
            resized = my_image.resize((700, 270), Image.ANTIALIAS)
            self.my_image1 = ImageTk.PhotoImage(resized)

            #---------Resizing Image in 220x220----------------
            my_image1 = Image.open(self.filename2)
            resized1 = my_image1.resize((220, 220), Image.ANTIALIAS)
            self.my_image2 = ImageTk.PhotoImage(resized1)
            self.Filter_user_Sample = Label(User_Dashboard_Window, image=self.my_image2)

            # ---------Placing Sample Image as Default view-----
            self.default_User_sample = Label(User_Dashboard_Window, image=self.my_image1)

            if self.filename == 0:
                self.default_User_sample.place(x=310, y=280)

            else:
                #cv2.imread(Hide_the_chk_buttons())
                #self.default_User_sample.place_forget()
                #self.default_User_sample.place(x=310, y=280)
                self.default_User_sample.place_forget()
                self.defaultImage.place_forget()

                self.Filter_user_Sample.place(x=310, y=280)


            # ------Asking user for number of sample-----------
            cv2.imread(Sample_Number())  # --Asking user for number of sample

    #==============Creating function for Setting Path=================
        def savefile():
            global filepath
            filepath = filedialog.askdirectory()
            self.path = filepath

    #=============Creating Function to create new folder==============
        def createFolder(directory):   # Creating function to create New Folder
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except OSError:
                print('Error: Creating directory. ' + directory)

    #_____________________________________________________________________________________
    #=======Filter:- Creating Filters To Generate Varius Sample of Data===================
    #-------------------------------------------------------------------------------------

    #=========Creating Function for Resize Filter============
        def Resize_filter():
            global resize_Sample_number
            resize_Sample_number = Sample_Number_R
            if Resize_variable.get() == "Resize":
                Sample_folder = createFolder('%s/Resize_Effect_Sample/' % (filepath)) #Calling function to create Folder
                import cv2

                for resize_Loop in range(0, resize_Sample_number):  # Creating loop
                    img = cv2.imread(self.filename)  # calling user input image
                    w = random.randint(80, 1000)  # passing random value for ramdom width
                    h = random.randint(80, 1000)  # passing random value for ramdom width
                    width, height = w, h  # Passing x and y in height and width
                    imageresize = cv2.resize(img, (width, height))  # passing Loop width and height image in variable
                    cv2.imwrite('%s/Resize_Effect_Sample/%s.jpg' % (filepath, resize_Loop+1), imageresize)  # Saving image at specific path
                # ----Note:- This code is working properly--------------

            else:
                pass

        # ============Invert Filter ====================
        def Invert_filter():
            if Invert_variable.get() == "invert":
                import cv2
                global invert_Sample_number
                invert_Sample_number = Sample_Number_R
                Sample_folder = createFolder('%s/Invert_Effect_Sample/' % (filepath))  # Calling function to create Folder

                def invert_image():
                    image = cv2.imread(self.filename)
                    image1 = cv2.bitwise_not(image)
                    cv2.imwrite('%s/Invert_Effect_Sample/0.jpg' % (filepath),image1)  # Saving Byte change inverted image

                    for invert_loop in range(0,invert_Sample_number):
                        channel = random.uniform(0,481)
                        image2 = (channel - image)
                        cv2.imwrite('%s/Invert_Effect_Sample/%s.jpg' % (filepath, invert_loop+1), image2)           #Saving inverted image generated by random value
                cv2.imread(invert_image())
     #--------------Note:- This Code is Working Properly----------------
            else:
                pass

        # =========Flip filter===============
        def Flip_filter():

            if Flip_variable.get() == "flip":
                Sample_folder = createFolder('%s/Flip_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                originalImage = cv2.imread(self.filename)  # Taking Image For Generating Sample
                flipv = cv2.flip(originalImage, 1)  # Generating Sample
                flipbv = cv2.flip(originalImage, -0)
                flipbh = cv2.flip(originalImage, -1)

                cv2.imwrite('%s/Flip_Effect_Sample/1.jpg' % (filepath,), originalImage)  # Saving Generated Image
                cv2.imwrite('%s/Flip_Effect_Sample/2.jpg' % (filepath), flipv)
                cv2.imwrite('%s/Flip_Effect_Sample/3.jpg' % (filepath), flipbv)
                cv2.imwrite('%s/Flip_Effect_Sample/4.jpg' % (filepath), flipbh)
            else:
                pass

     # --------------Note:- This Code is working properly--------------------------

    # ===============rotate filter ======================
        def Rotate_filter():

            if Rotate_variable.get() == "rotate":
                Sample_folder = createFolder('%s/Rotate_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                originalImage = cv2.imread(self.filename)  # Taking Image For Generating Sample

                img_rotate = cv2.rotate(originalImage, cv2.ROTATE_90_CLOCKWISE)  # Generating Sample
                img_rotate90 = cv2.rotate(originalImage, cv2.ROTATE_90_COUNTERCLOCKWISE)
                img_rotate180 = cv2.rotate(originalImage, cv2.ROTATE_180)

                cv2.imwrite('%s/Rotate_Effect_Sample/1.jpg' % (filepath), originalImage)  # Saving Generated Sample
                cv2.imwrite('%s/Rotate_Effect_Sample/2.jpg' % (filepath), img_rotate)
                cv2.imwrite('%s/Rotate_Effect_Sample/3.jpg' % (filepath), img_rotate90)
                cv2.imwrite('%s/Rotate_Effect_Sample/4.jpg' % (filepath), img_rotate180)
    # ------------------Note:- This filter is working properly--------------------

            else:
                pass

    #==========Creating function for Hue Filter==============
        def Hue_filter():
            if Hue_variable.get()=="hue":
                Sample_folder = createFolder('%s/Hue_Effect_Sample/' % (filepath))  # Calling function to create Folder

                global hue_Sample_number
                hue_Sample_number = Sample_Number_R
                def hue_image():

                    image = cv2.imread(self.filename)       #Taking Sample

                    for name in range(1, hue_Sample_number + 1):
                        saturation = random.randint(5,5001)    #Passing Random number for Diffrent Sample
                        hue_Efec = random.randint(10, 1000)
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                        v = image[:,:,2]
                        v = np.where(v <= hue_Efec + saturation, v - saturation, hue_Efec)
                        image[:, :, 2] = v
                        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

                    cv2.imwrite('%s/Hue_Effect_Sample/%s.jpg' % (filepath,name1), image)


                for name1 in range(1,hue_Sample_number+1):
                    hue_image()

            #----------------Note:- This Code Is Working Properly----------------------

            else:
                pass

    #=================Creating function for Light Filter=======================
        def Light_filter():
            if Light_filter_variable.get() == "light":
                Sample_folder = createFolder('%s/Light_Effect_Sample/' % (filepath))  # Calling function to create Folder
                global light_Filter_Sample_number
                light_Filter_Sample_number = Sample_Number_R
                import cv2
                import numpy as np
                def add_light():
                    image = cv2.imread(self.filename)  # Taking Sample

                    #for name in range(1, light_Filter_Sample_number + 1):

                    gamma = random.uniform(-90,90)  # Passing Random number for Diffrent Sample
                    if gamma==0:
                        gamma=gamma+1
                    invGamma = 1.0 / gamma
                    table = np.array([((i / 255.0) ** invGamma) * 255
                                      for i in np.arange(0.5, 256)]).astype("uint8")
                    image1 = cv2.LUT(image, table)
                    if gamma >= 1:
                        cv2.imwrite('%s/Light_Effect_Sample/%s.jpg' % (filepath,name), image1)
                    else:
                        cv2.imwrite('%s/Light_Effect_Sample/%s.jpg' % (filepath,name), image1)
                for name in range(1, light_Filter_Sample_number + 1):
                    add_light()
    #--------------------Note:- This Code is working properly-----------------
            else:
                pass

    #============Creating Function for Light Color Filter==================
        def Light_color_filter():
            if Light_color_filters_variable.get() == "lColor":
                Sample_folder = createFolder('%s/Light_color_Effect_Sample/' % (filepath))  # Calling function to create Folder
                global light_Color_Sample_number
                light_Color_Sample_number = Sample_Number_R
                import cv2
                import numpy as np

                def add_light_color():
                    image = cv2.imread(self.filename)  # Taking Sample
                    gamma = random.uniform(0.1, 2.1)  # Passing Random number for Diffrent Sample
                    color = random.randint(50, 250)  # Passing Random number for Diffrent Sample
                    invGamma = 1.0 / gamma
                    image = (color - image)
                    table = np.array([((i / 255.0) ** invGamma) * 255
                                      for i in np.arange(0, 256)]).astype("uint8")

                    image = cv2.LUT(image, table)
                    if gamma >= 1:
                        cv2.imwrite('%s/Light_color_Effect_Sample/%s.jpg' % (filepath, name),image)

                    else:
                        cv2.imwrite('%s/Light_color_Effect_Sample/%s.jpg' % (filepath, name), image)

                for name in range(1, light_Color_Sample_number + 1):
                    add_light_color()

    #-------------Note:- This Code is working properly-----------------------------
            else:
                pass

    #===========Creating Fucntion for Seturation Filter================
        def Seturate_filter():
            if Seturate_variable.get()=="Seturate_Image":
                Sample_folder = createFolder('%s/Seturate_Effect_Sample/' % (filepath))  # Calling function to create Folder
                global Seturation_Sample_number
                Seturation_Sample_number = Sample_Number_R
                import cv2
                import numpy as np
                def saturation_image():
                    #image = cv2.imread(self.filename)  # Taking Sample
                    for name in range(1, Seturation_Sample_number + 1):
                        image = cv2.imread(self.filename)
                        saturation = random.randint(5,400)  # Passing Random number for Diffrent Sample
                        saturation1 = random.randint(5, 400)
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                        v = image[:, :, 2]
                        v = np.where(v <= saturation1 - saturation, v + saturation, saturation1)
                        image[:, :, 2] = v

                        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                        cv2.imwrite('%s/Seturate_Effect_Sample/%s.jpg' % (filepath,name), image)
                        cv2.imshow("w",image)

                    #for name in range(1, Seturation_Sample_number + 1):
                        #cv2.imwrite('%s/Seturate_Effect_Sample/%s.jpg' % (filepath, name), image)
                saturation_image()
    #-----------------Note:- This Code is working properly----------------
    #???????????????Note:- But Generating only One Image Need To Work on Loop??????????????????
            else:
                pass

    #========Creating Function for Gray Scale Image Filter=====================================
        def Gray_scale_Filter():
            if Gray_scale_variable.get() == "Gray":
                Sample_folder = createFolder(
                        '%s/Rectangle_covered_Sample/' % (filepath))  # Calling function to create Folder
                global gray_Scale_Sample_number
                gray_Scale_Sample_number = Sample_Number_R
                for name in range(1, gray_Scale_Sample_number + 1):
                    image = cv2.imread(self.filename)
                    height, width = image.shape[:2]
                    height_value = random.randint(10, 50)
                    width_value = random.randint(10, 50)
                    position_x = random.randint(50, height)
                    position_y = random.randint(50, width)
                    color3 = random.randint(50, 200)
                    color1 = random.randint(50, 200)
                    color2 = random.randint(50, 200)

                    cv2.rectangle(image, pt1=(position_y, position_x), pt2=(height_value, width_value),
                              color=(color1, color2, color3), thickness=-1)
                    cv2.imwrite('%s/Rectangle_covered_Sample/%s.jpg' % (filepath, name), image)

                # ???????????Note:- Generating only one sample Work on it?????????????????
            else:
                pass

    #===========================Creating Function for Addepive Filter=============================
        def Addeptive_gaussian_filter():
            if Addeptive_variable.get()=="addept":
                Sample_folder = createFolder(
                    '%s/Addeptive_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2

                global Addeptive_Sample_number
                Addeptive_Sample_number = Sample_Number_R


                def addeptive_gaussian_noise():
                    image = cv2.imread(self.filename)  # Taking Sample
                    Addept_diffs = random.randint(100, 300)  # Passing Random number for Diffrent Sample:
                    Addept_diffh = random.randint(100, 300)  # Passing Random number for Diffrent Sample:
                    Addept_diffv = random.randint(100, 300)  # Passing Random number for Diffrent Sample:
                    h, s, v = cv2.split(image)
                    s = cv2.adaptiveThreshold(s, Addept_diffs, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
                    h = cv2.adaptiveThreshold(h,Addept_diffh, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
                    v = cv2.adaptiveThreshold(v, Addept_diffv, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
                    image = cv2.merge([h, s, v])

                    cv2.imshow("w", image)
                    cv2.imwrite('%s/Addeptive_Effect_Sample/%s.jpg' % (filepath, name), image)

                for name in range(1, Addeptive_Sample_number + 1):
                    addeptive_gaussian_noise()
#???????????????This Code Is Not Generating any sample But Not Throwing Error As Well????????????????
            else:
                pass

    #=======================Creating Function for Contrass Filter============================
        def Contrass_filter():
            if Contrass_variable.get()=="Contra":
                Sample_folder = createFolder('%s/Contrass_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                global contrass_Sample_number
                contrass_Sample_number = Sample_Number_R


                def contrast_image():

                    for name in range(1, contrass_Sample_number + 1):
                        image = cv2.imread(self.filename)  # Taking Sample
                        contrast = random.uniform(-150,199)  # Passing Random number for Diffrent Sample:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                        image[:, :, 2] = [
                            [max(pixel - contrast, 0) if pixel < 190 else min(pixel + contrast, 255) for pixel in row] for
                            row in image[:, :, 2]]
                        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                        cv2.imwrite('%s/Contrass_Effect_Sample/%s.jpg' % (filepath, name), image)

                contrast_image()

    #????????Note:- This Code Is Taking Too Much Time And Genrating Only one Image But Workin With out Any Syntax Error?????
            else:
                pass

    #=====================Creating Function for Edge Canny Filter=========================
        def Edge_canny_filter():
            if Edge_detect_variable.get()=="cany":
                Sample_folder = createFolder('%s/Edge_Canny_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                global edge_cany_Sample_number
                edge_cany_Sample_number = Sample_Number_R
                def edge_detect_canny_image():

                    for name in range(1, edge_cany_Sample_number + 1):
                        image = cv2.imread(self.filename)  # Taking Sample
                        cany_diff1 = random.randint(0, 100)  # Passing Random number for Diffrent Sample:
                        cany_diff2 = random.randint(0, 100)  # Passing Random number for Diffrent Sample:
                        image = cv2.Canny(image,cany_diff1,cany_diff2)
                        cv2.imwrite('%s/Edge_Canny_Effect_Sample/%s.jpg' % (filepath, name), image)


                edge_detect_canny_image()
            else:
                pass

    #===========Creating Function for Transformation Filter==================
        def Transformation_filter():
            if Transformation_variable.get()=="Transfom":
                Sample_folder = createFolder(
                    '%s/Transform_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np

                global transformation_Sample_number
                transformation_Sample_number = Sample_Number_R

                def transformation_image():

                    for name in range(1, transformation_Sample_number + 1):
                        image = cv2.imread(self.filename)
                        rows, cols, ch = image.shape
                        ptsx1 = random.randint(0, 500)
                        ptsx2 = random.randint(0, 500)
                        pts1 = np.float32([[ptsx1, ptsx2], [200, 50], [50, 200]])
                        pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
                        M = cv2.getAffineTransform(pts1, pts2)
                        image = cv2.warpAffine(image, M, (cols, rows))

                        cv2.imwrite('%s/Transform_Effect_Sample/%s.jpg' % (filepath, name), image)

                transformation_image()
            else:
                pass

    #=============Creating Function  for Embossed Filter====================
        def crop():
            if Emboss_variable.get()=="embs":
                Sample_folder = createFolder('%s/Crop_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np
                global crop_Sample_number
                crop_Sample_number = Sample_Number_R
                for name in range(1,crop_Sample_number + 1):
                    image = cv2.imread(self.filename)
                    '''x = random.uniform(.01, .99)
                    y = random.uniform(.01, .99)'''
                    x = random.uniform(.01, .50)
                    y = random.uniform(.60, .99)

                    height, width = image.shape[:2]
                    start_row, start_col = int(height * x), int(width * x)

                    end_row, end_col = int(height * y), int(width * y)

                    cropped = image[start_row:end_row, start_col:end_col]
                    cv2.imwrite('%s/Crop_Sample/%s.jpg' % (filepath, name),cropped)
            else:
                pass

    #================Creating Function for Translation Filter=================================
        def Translation_filter():
            if Translation_variable.get()=="Translation":
                Sample_folder = createFolder(
                    '%s/Translation_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np
                global translation_Sample_number
                translation_Sample_number = Sample_Number_R

                def translation_image():
                    image = cv2.imread(self.filename)  # Taking Sample
                    translation_diff1 = random.uniform(-150,150)  # Passing Random number for Diffrent Sample:
                    translation_diff2 = random.uniform(-150,150)  # Passing Random number for Diffrent Sample:
                    rows, cols, c = image.shape
                    M = np.float32([[1,0,translation_diff1], [0, 1,translation_diff2]])
                    image = cv2.warpAffine(image, M, (cols, rows))
                    cv2.imwrite('%s/Translation_Effect_Sample/%s.jpg' % (filepath, name), image)


                for name in range(1,translation_Sample_number + 1):
                    translation_image()
            else:
                pass

    #==========creating function for salt Filter========================
        def Salt_filter():
            if salt_and_paper_variable.get()=="Salt_paper":
                Sample_folder = createFolder(
                    '%s/Salt_Effect_Sample/' % (filepath))  # Calling function to create Folder
                global edge_cany_Sample_number
                edge_cany_Sample_number = Sample_Number_R
                import numpy as np
                import cv2

                for name in range(1, edge_cany_Sample_number + 1):
                    image = cv2.imread(self.filename)  # Taking Sample
                    color3 = random.randint(50, 200)
                    color1 = random.randint(50, 200)
                    color2 = random.randint(50, 200)
                    height, width = image.shape[:2]
                    radius_value = random.randint(10, 50)
                    position_circle = random.randint(50, height)
                    position_circle = random.randint(50, width)
                    cv2.circle(image, center=(position_circle, position_circle), radius=radius_value,
                               color=(color1, color2, color3), thickness=-10)
                    cv2.imwrite('%s/Salt_Effect_Sample/%s.jpg' % (filepath, name), image)
            else:
                pass

    #=============Creating Function for Sharp Filter==================
        def Sharp_filter():
            if Sharp_variable.get()=="Sharp_value":
                global edge_cany_Sample_number
                edge_cany_Sample_number = Sample_Number_R
                Sample_folder = createFolder(
                    '%s/Pencil_Shade_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                #import numpy as np
                import random

                def sharpen_image():
                    for name in range(1, edge_cany_Sample_number + 1):
                        #image = cv2.imread(self.filename)  # Taking Sample
                        color_image = cv2.imread(self.filename)
                        sm = random.randint(1, 150)
                        sr = random.uniform(0.009, 0.9)
                        cartoon_image1, bawla = cv2.pencilSketch(color_image, sigma_s=sm, sigma_r=sr, shade_factor=0.02)
                        cv2.imshow('cartoon', cartoon_image1)
                        cv2.imwrite('%s/Pencil_Shade_Sample/%s.jpg' % (filepath, name), cartoon_image1)


                sharpen_image()

            else:
                pass

    #=========Creating function for Dilation Filter================
        def Dilation_filter():
            if dilation_variable.get()=="dilation_value":
                global dela_cany_Sample_number
                dela_cany_Sample_number = Sample_Number_R
                Sample_folder = createFolder(
                    '%s/Dilation_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np

                def dilation_image():
                    for name in range(1, dela_cany_Sample_number + 1):
                        image = cv2.imread(self.filename)  # Taking Sample
                        dila_diff1 = random.randint(0,51)  # Passing Random number for Diffrent Sample:
                        dila_diff2 = random.randint(0,51)  # Passing Random number for Diffrent Sample:
                        kernel = np.ones((dila_diff1, dila_diff2), np.uint8)
                        image = cv2.dilate(image, kernel, iterations=1)
                        cv2.imwrite('%s/Dilation_Effect_Sample/%s.jpg' % (filepath, name), image)


                dilation_image()
    # ???????????Note:- Generating only one sample?????????????????

            else:
                pass

    #==================Creating function for Blure Filter===================
        def Blure_filter():
            if Blure_variable.get()=="Blure_value":
                global dela_cany_Sample_number
                dela_cany_Sample_number = Sample_Number_R
                Sample_folder = createFolder(
                    '%s/Blure_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2

                def averageing_blur():
                    for name in range(1, dela_cany_Sample_number + 1):
                        image = cv2.imread(self.filename)  # Taking Sample
                        avgBlur_diff1 = random.randint(1,41)  # Passing Random number for Diffrent Sample:
                        avgBlur_diff2 = random.randint(1, 41)
                        image = cv2.blur(image, (avgBlur_diff1, avgBlur_diff2))

                        cv2.imwrite('%s/Blure_Effect_Sample/%s.jpg' % (filepath, name), image)


                averageing_blur()
    # ???????????Note:- Generating only one sample?????????????????
            else:
                pass

    #============Creating Function for Black Hat Filter===================
        def cartoon():
            if Black_hat_variable.get()=="Black_hat_value":
                Sample_folder = createFolder(
                    '%s/Black_Hat_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np
                global black_Hat_Sample_number
                black_Hat_Sample_number = Sample_Number_R

                for name in range(1, black_Hat_Sample_number + 1):
                    image = cv2.imread(self.filename)  # Taking Sample
                    sm = random.randint(1,1000)
                    sr = random.uniform(0.001,1.99)
                    image1 = cv2.stylization(image, sigma_s=sm, sigma_r=sr)

                    #cv2.imwrite('%s/Test_Sample/%s.jpg' % (filepath, name), image)
                    cv2.imwrite('%s/Black_Hat_Effect_Sample/%s.jpg' % (filepath, name), image1)
    # ???????????Note:- Generating only one sample?????????????????
            else:
                pass

    #=============Creating function for Top Hat Filter================
        def Top_Hat_filter():
            if Top_hat_variable.get()=="Top_hat_value":
                Sample_folder = createFolder(
                    '%s/Top_Hat_Effect_Sample/' % (filepath))  # Calling function to create Folder
                import cv2
                import numpy as np
                global top_Hat_Sample_number
                top_Hat_Sample_number = Sample_Number_R

                for name in range(1, top_Hat_Sample_number + 1):
                    image = cv2.imread(self.filename)  # Taking Sample
                    top_Hat_diff1 = random.randint(200, 500)  # Passing Random number for Diffrent Sample:
                    kernel = np.ones((top_Hat_diff1, top_Hat_diff1), np.uint8)
                    image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

                    cv2.imwrite('%s/Top_Hat_Effect_Sample/%s.jpg' % (filepath, name), image)

    # ???????????Note:- Generating only one sample?????????????????
            else:
                pass

    #=========This is a extra filter add for testing porpus===================
        def Test_filter():
            if blank_variable.get()=="test_value":
                Sample_folder = createFolder(
                    '%s/Test_Sample/' % (filepath))  # Calling function to create Folder
                global top_Hat_Sample_number
                top_Hat_Sample_number = Sample_Number_R
                import cv2
                for name in range(1, top_Hat_Sample_number + 1):
                    image = cv2.imread(self.filename)  # Taking Sample
                    top_Hat_diff1 = random.randint(1,10)  # Passing Random number for Diffrent Sample:
                    image = cv2.blur(image, (top_Hat_diff1, top_Hat_diff1))
                    cv2.imwrite('%s/Test_Sample/%s.jpg' % (filepath, name), image)
                    cv2.imshow("w", image)
                    cv2.waitKey(0)
            else:
                pass

    #____________________________________________________________________________________
    #==================Creation function for Data Set Generating=========================
    #------------------------------------------------------------------------------------
        def download_Button():
            if self.file ==0 or self.path==0:
                if self.file==0:
                    messagebox.showwarning("Warning", "Please Upload Semple Image First",
                                     parent=self.User_Dashboard_Window)
                if self.path==0:
                    messagebox.showwarning("warning", "Please select path first",
                                         parent=self.User_Dashboard_Window)
                else:
                    pass



            else:
        #---Note:-  Callig Function in Select Filter Frame-----------
                cv2.imread(Resize_filter())
                cv2.imread(Invert_filter())
                cv2.imread(Flip_filter())
                cv2.imread(Rotate_filter())
                cv2.imread(Hue_filter())
                cv2.imread(Light_filter())
                cv2.imread(Light_color_filter())
                cv2.imread(Seturate_filter())
                cv2.imread(Addeptive_gaussian_filter())
                cv2.imread(Contrass_filter())
                cv2.imread(Edge_canny_filter())
                cv2.imread(Transformation_filter())
                cv2.imread(crop())
                cv2.imread(Gray_scale_Filter())
                cv2.imread(Translation_filter())
                cv2.imread(Salt_filter())
                cv2.imread(Sharp_filter())
                cv2.imread((Dilation_filter()))
                cv2.imread(Blure_filter())
                cv2.imread(cartoon())
                cv2.imread(Top_Hat_filter())
    #----------------Note:- This Code Is Working Properly----------------

    #---------Note:- Calling Function in More Filter Frame ----------------
                cv2.imread(Test_filter())


    #___________________________________________________________________________________________
    #===============Creating variable to check on value or off value of check box==============
    #---------------Note :- These variable are for Select Filter Frame-------------------------
    #-------------------------------------------------------------------------------------------
        Resize_variable = StringVar()
        Flip_variable = StringVar()
        Invert_variable = StringVar()
        Hue_variable = StringVar()
        Rotate_variable = StringVar()
        Light_filter_variable = StringVar()
        Light_color_filters_variable = StringVar()
        Seturate_variable = StringVar()
        Addeptive_variable = StringVar()
        Contrass_variable = StringVar()
        Edge_detect_variable = StringVar()
        Transformation_variable = StringVar()
        Emboss_variable = StringVar()
        Gray_scale_variable = StringVar()
        Translation_variable = StringVar()
        salt_and_paper_variable = StringVar()
        Sharp_variable = StringVar()
        dilation_variable = StringVar()
        Blure_variable = StringVar()
        Black_hat_variable = StringVar()
        Top_hat_variable = StringVar()
    #------Note:- Above Code is working properly----------
        blank_variable = StringVar()


    #____________________________________________________________________________________
    #-----------------Putting Buttons on Screen------------------------------------------
    #____________________________________________________________________________________

        # _______Show_Feature:- Function For Putting Button On Screen_________
        def show_Feature():
            upload_Sample.place(x=290, y=580)
            save_Button.place(x=410, y=580)
            Show_Filter_button.place(x=530, y=580)
            #select_More.place(x=650, y=580)
            hide_button.place(x=650, y=580)
            Generate_Sample.place(x=780, y=580)
            feature_button1.place(x=900, y=580)

        #______Hide_Feature:- Fucntion to Hide Feature Button From Screen_____
        def hide_Feature():
            upload_Sample.place_forget()
            save_Button.place_forget()
            Show_Filter_button.place_forget()
            #select_More.place_forget()
            hide_button.place_forget()
            feature_button1.place_forget()
            Generate_Sample.place_forget()

        def Hide_the_chk_2():
            chk_size.place_forget()
            chk_invert.place_forget()
            chk_crop.place_forget()
            chk_blure.place_forget()
            chk_hue.place_forget()
            chk_light.place_forget()
            chk_light_color.place_forget()
            chk_setu.place_forget()
            chk_gray.place_forget()
            chk_addeptive.place_forget()
            chk_Contrass.place_forget()
            chk_Edge_cany.place_forget()
            Transfom_check.place_forget()
            chk_emboss.place_forget()
            chk_Translation.place_forget()
            chk_salt_paper.place_forget()
            chhk_Sharp.place_forget()
            chhk_dilation.place_forget()
            Chk_Blure.place_forget()
            chhk_Black_hat.place_forget()

        #______Hide_Check:- Fucntion for Hiding Check Box_____________________
        def Hide_the_chk_buttons():
            chk_size.place_forget()
            chk_invert.place_forget()
            chk_crop.place_forget()
            chk_blure.place_forget()
            chk_hue.place_forget()
            chk_light.place_forget()
            chk_light_color.place_forget()
            chk_setu.place_forget()
            chk_gray.place_forget()
            chk_addeptive.place_forget()
            chk_Contrass.place_forget()
            chk_Edge_cany.place_forget()
            Transfom_check.place_forget()
            chk_emboss.place_forget()
            chk_Translation.place_forget()
            chk_salt_paper.place_forget()
            chhk_Sharp.place_forget()
            chhk_dilation.place_forget()
            Chk_Blure.place_forget()
            chhk_Black_hat.place_forget()
            Chk_Test.place_forget()
            # ---------Checking User input image exist or not -------------
            if self.sample_Image == 0:
                self.defaultImage2.place_forget()
                self.defaultImage.place(x=310, y=280)
            else:
                # -----Placing 700x270 image on screen------
                self.Filter_user_Sample.place_forget()
                self.default_User_sample.place(x=310, y=280)
            Check_blank.place_forget()

        #_______More_Filter:- Function for putting some extra filter on screen
        def more_Filter():
            Check_blank.deselect()
            Check_blank.place(x=600, y=280)

            chk_size.place_forget()
            chk_invert.place_forget()
            chk_crop.place_forget()
            chk_blure.place_forget()
            chk_hue.place_forget()
            chk_light.place_forget()
            chk_light_color.place_forget()
            chk_setu.place_forget()
            chk_gray.place_forget()
            chk_addeptive.place_forget()
            chk_Contrass.place_forget()
            chk_Edge_cany.place_forget()
            Transfom_check.place_forget()
            chk_emboss.place_forget()
            chk_Translation.place_forget()
            chk_salt_paper.place_forget()
            chhk_Sharp.place_forget()
            chhk_dilation.place_forget()
            Chk_Blure.place_forget()
            chhk_Black_hat.place_forget()
            Chk_Test.place_forget()

            # ---------Checking User input image exist or not -------------
            if self.sample_Image == 0:
                self.defaultImage.place_forget()
                self.defaultImage2.place(x=310, y=280)
            else:
                self.default_User_sample.place_forget()
                self.defaultImage.place_forget()

                self.Filter_user_Sample.place(x=310, y=280)

    #_________Filter_Show:-Function For Putting CHeck Button On Screen_________
        def Filter_show():

            # ----------Creating Resized Filter Check Box -------------------- 1
            chk_size.deselect()
            chk_size.place(x=600, y=280)

            # ----------Creating Invert Filter Check Box -------------------- 2
            chk_invert.deselect()
            chk_invert.place(x=600, y=315)

            # ----------Creating flip Filter Check Box -------------------- 3
            chk_crop.deselect()
            chk_crop.place(x=600, y=350)

            # ----------Creating Rotate Filter Check Box -------------------- 4
            chk_blure.deselect()
            chk_blure.place(x=600, y=385)

            # ----------Creating Hue Filter Check Box -------------------- 5
            chk_hue.deselect()
            chk_hue.place(x=600, y=420)

            # ----------Creating ligth Filter Check Box -------------------- 6
            chk_light.deselect()
            chk_light.place(x=600, y=455)

            # ----------Creating ligth color Filter Check Box -------------------- 7
            chk_light_color.deselect()
            chk_light_color.place(x=600, y=490)

            # ----------Creating Seturation Filter Image Filter Check Box -------------------- 8
            chk_setu.deselect()
            chk_setu.place(x=770, y=280)

            # ----------Creating Gray Scale Filter Check Box -------------------- 9
            chk_gray.deselect()
            chk_gray.place(x=770, y=315)

            # ----------Creating Adeptive Gaussian Check Box -------------------- 10
            chk_addeptive.deselect()
            chk_addeptive.place(x=770, y=350)

            # ----------Creating Contrass Check Box -------------------- 11
            chk_Contrass.deselect()
            chk_Contrass.place(x=770, y=385)

            # ----------Creating Edge Detect Canny Check Box -------------------- 12
            chk_Edge_cany.deselect()
            chk_Edge_cany.place(x=770, y=420)

            # ----------Creating Transformation Check Box -------------------- 13
            Transfom_check.deselect()
            Transfom_check.place(x=770, y=455)

            # ----------Creating Emboss Check Box -------------------- 14
            chk_emboss.deselect()
            chk_emboss.place(x=770, y=490)

            # ----------Creating Translation Filter Check Box -------------------- 15
            chk_Translation.deselect()
            chk_Translation.place(x=940, y=280)

            # ----------Creating Salt And Paper Check Box -------------------- 16
            chk_salt_paper.deselect()
            chk_salt_paper.place(x=940, y=315)

            # ----------Creating Sharp Check Box -------------------- 17
            chhk_Sharp.deselect()
            chhk_Sharp.place(x=940, y=350)

            # ----------Creating Blank Check Box -------------------- 18
            chhk_dilation.deselect()
            chhk_dilation.place(x=940, y=385)

            # ----------Creating Blank Check Box -------------------- 19
            Chk_Blure.deselect()
            Chk_Blure.place(x=940, y=420)

            # ----------Creating Blank Check Box -------------------- 20
            chhk_Black_hat.deselect()
            chhk_Black_hat.place(x=940, y=455)

            # ----------Creating Blank Check Box -------------------- 21
            Chk_Test.deselect()
            Chk_Test.place(x=940, y=490)

            # ---------Checking User input image exist or not -------------
            if self.sample_Image == 0:
                self.defaultImage.place_forget()
                self.defaultImage2.place(x=310, y=280)
            else:
                self.default_User_sample.place_forget()
                self.defaultImage.place_forget()

                self.Filter_user_Sample.place(x=310, y=280)

            #----------Removing Blank Check Box------------
            Check_blank.place_forget()



#==============================================================================================================
#________________________________________FRONT END CODE________________________________________________________
#----------------------Front end code in written here but packed in back end code -----------------------------
#==============================================================================================================

        # ____________________________________________________________
        # ================Main-Background=============================
        # ------------------------------------------------------------
        self.bg = ImageTk.PhotoImage(file="bg.png")
        main_Background = Label(self.User_Dashboard_Window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ___________________________________________________________
        # ================Sub-Background=============================
        # -----------------------------------------------------------
        self.left = ImageTk.PhotoImage(file="aug1.png")
        left = Label(self.User_Dashboard_Window, image=self.left).place(x=220, y=130, width=900, height=500)

    #------------------------------------------------------------------------
    #-------------------------Creating CheckBox -----------------------------
    #------------------------------------------------------------------------
        # ----------Creating Resized Filter Check Box -------------------- 1
        chk_size = Checkbutton(left, text="Resize", variable=Resize_variable,bg="#4e4e4e", onvalue="Resize", offvalue=0,

                               font=("time new roman", 12))

        # ----------Creating Invert Filter Check Box -------------------- 2
        chk_invert = Checkbutton(left, text="invert", variable=Invert_variable, onvalue="invert", offvalue=0,
                                 bg="#4e4e4e",
                                 font=("time new roman", 12))

        # ----------Creating flip Filter Check Box -------------------- 3
        chk_crop = Checkbutton(left, text="Flip", variable=Flip_variable, onvalue="flip", offvalue=0,
                               bg="#4e4e4e", font=("time new roman", 12))

        # ----------Creating Rotate Filter Check Box -------------------- 4
        chk_blure = Checkbutton(left, text="Rotate", variable=Rotate_variable, onvalue="rotate", offvalue=0,
                                bg="#4e4e4e",
                                font=("time new roman", 12))

        # ----------Creating Hue Filter Check Box -------------------- 5
        chk_hue = Checkbutton(left, text="Hue", variable=Hue_variable, onvalue="hue", offvalue=0, bg="#4e4e4e",
                                  font=("time new roman", 12))

        # ----------Creating ligth Filter Check Box -------------------- 6
        chk_light = Checkbutton(left, text="Light", variable=Light_filter_variable, onvalue="light",
                                offvalue=0,
                                bg="#4e4e4e",
                                font=("time new roman", 12))

        # ----------Creating ligth color Filter Check Box -------------------- 7
        chk_light_color = Checkbutton(left, text="Light Color", variable=Light_color_filters_variable,
                                      onvalue="lColor",
                                      offvalue=0, bg="#4e4e4e",
                                      font=("time new roman", 12))

        # ----------Creating Seturation Filter Image Filter Check Box -------------------- 8
        chk_setu = Checkbutton(left, text="Seturation", variable=Seturate_variable, onvalue="Seturate_Image",
                               offvalue=0, bg="#4e4e4e", font=("time new roman", 12))

        # ----------Creating Adeptive Gaussian Check Box -------------------- 10
        chk_addeptive = Checkbutton(left, text="Addeptive_gaussian", variable=Addeptive_variable, onvalue="addept",
                                    offvalue=0,
                                    bg="#4e4e4e",
                                    font=("time new roman", 12))

        # ----------Creating Gray Scale Filter Check Box -------------------- 9
        chk_gray = Checkbutton(left, text="Gray Scale", variable=Gray_scale_variable, onvalue="Gray", offvalue=0,
                               bg="#4e4e4e",
                               font=("time new roman", 12))


        # ----------Creating Contrass Check Box -------------------- 11
        chk_Contrass = Checkbutton(left, text="Contrass", variable=Contrass_variable, onvalue="Contra", offvalue=0,
                                   bg="#4e4e4e",
                                   font=("time new roman", 12))

        # ----------Creating Edge Detect Canny Check Box -------------------- 12
        chk_Edge_cany = Checkbutton(left, text="Edge Canny", variable=Edge_detect_variable, onvalue="cany", offvalue=0,
                                    bg="#4e4e4e",
                                    font=("time new roman", 12))

        # ----------Creating Transformation Check Box -------------------- 13
        Transfom_check = Checkbutton(left, text="Transformation", variable=Transformation_variable,
                                     onvalue="Transfom", offvalue=0,
                                     bg="#4e4e4e",
                                     font=("time new roman", 12))

        # ----------Creating Emboss Check Box -------------------- 14
        chk_emboss = Checkbutton(left, text="Crop", variable=Emboss_variable, onvalue="embs", offvalue=0,
                                 bg="#4e4e4e",
                                 font=("time new roman", 12))

        # ----------Creating Translation Filter Check Box -------------------- 15
        chk_Translation = Checkbutton(left, text="Translation", variable=Translation_variable,
                                          onvalue="Translation", offvalue=0,
                                          bg="#4e4e4e", font=("time new roman", 12))

        # ----------Creating Salt And Paper Check Box -------------------- 16
        chk_salt_paper = Checkbutton(left, text="Salt_And Paper", variable=salt_and_paper_variable,
                                         onvalue="Salt_paper", offvalue=0,
                                         bg="#4e4e4e",
                                         font=("time new roman", 12))

        # ----------Creating Sharp Check Box -------------------- 17
        chhk_Sharp = Checkbutton(left, text="Sharp", variable=Sharp_variable, onvalue="Sharp_value", offvalue=0,
                                     bg="#4e4e4e",
                                     font=("time new roman", 12))

        # ----------Creating Blank Check Box -------------------- 18
        chhk_dilation = Checkbutton(left, text="Dilation", variable=dilation_variable, onvalue="dilation_value",
                                    offvalue=0,
                                    bg="#4e4e4e",
                                    font=("time new roman", 12))

        # ----------Creating Blank Check Box -------------------- 19
        Chk_Blure = Checkbutton(left, text="Blure", variable=Blure_variable, onvalue="Blure_value", offvalue=0,
                                bg="#4e4e4e",
                                font=("time new roman", 12))

        # ----------Creating Blank Check Box -------------------- 20
        chhk_Black_hat = Checkbutton(left, text="Black Hat", variable=Black_hat_variable, onvalue="Black_hat_value",
                                     offvalue=0,
                                     bg="#4e4e4e",
                                     font=("time new roman", 12))

        # ----------Creating Blank Check Box -------------------- 21
        Chk_Test = Checkbutton(left, text="Top_Hat", variable=Top_hat_variable, onvalue="Top_hat_value", offvalue=0,
                               bg="#4e4e4e",
                               font=("time new roman", 12))


        #---------------Some Extra Filter-------------------------------------
        # ----------Creating Blank Check Box --------------------
        Check_blank = Checkbutton(left,text="Test", variable=blank_variable, onvalue="test_value", offvalue=0,
                            bg="#4e4e4e",
                            font=("time new roman", 12))

        '''# ----------Creating All Filter Check Box --------------------
        chk_all = Checkbutton(left, text="All Filter", onvalue=1, offvalue=0, bg="#4e4e4e",
                                 font=("time new roman", 12))
        chk_all.deselect()
        chk_all.place(x=600, y=455)'''

    #---------------------------------------------------------------------------------
    #-----------------------Creating Feature Button-----------------------------------
    #---------------------------------------------------------------------------------

        #_______Default_Image:- Importing image to show as defaul___________
        self.result = ImageTk.PhotoImage(file="default_image.jpeg")
        self.defaultImage = Label(self.User_Dashboard_Window, image=self.result, bd=1, bg="#4e4e4e", cursor="hand2")

        #---------Checking User input image exist or not -------------
        if self.sample_Image == 0:
            self.defaultImage.place(x=310, y=280)
        else:
            pass

        #_______Default_Image :- For Side View in 220x220__________________
        self.result2 = ImageTk.PhotoImage(file="default_image2.jpeg")
        self.defaultImage2 = Label(self.User_Dashboard_Window, image=self.result2, bd=1, bg="#4e4e4e", cursor="hand2")

        #______Show_Feature:- _____Creating Button To Display Feature Button____________
        self.feature_Image = ImageTk.PhotoImage(file="Show.png")
        feature_button = Button(self.User_Dashboard_Window,activebackground="#4e4e4e", image=self.feature_Image, borderwidth=0, bg="#4e4e4e", command=show_Feature)
        feature_button.place(x=250,y=580)

        #______Hide_Feature:-___Creating Button To Hide Feature Button___________
        self.feature_Image1 = ImageTk.PhotoImage(file="Hide.png")
        feature_button1 = Button(self.User_Dashboard_Window, image=self.feature_Image1,activebackground="#4e4e4e", borderwidth=0, bg="#4e4e4e", command=hide_Feature)

        # ______Upload:- creating button to upload sample image_____________
        self.download = ImageTk.PhotoImage(file="Upload.png")
        upload_Sample= Button(self.User_Dashboard_Window, image=self.download,activebackground="#4e4e4e", borderwidth=0 ,bg="#4e4e4e",command=Upload_file)

        # ______Set-Path:- creating button to set Path for saving data set__________
        self.select_path = ImageTk.PhotoImage(file="Select_path.png")
        save_Button = Button(self.User_Dashboard_Window,image=self.select_path,activebackground="#4e4e4e", borderwidth=0,bg="#4e4e4e",command=savefile)


        # __________ SelectFilter:- _button is using to show check button Of filter_____
        self.select_filter = ImageTk.PhotoImage(file="Select_Filter.png")
        Show_Filter_button = Button(self.User_Dashboard_Window, image=self.select_filter,borderwidth=0,activebackground="#4e4e4e", bg="#4e4e4e", command=Filter_show)


        # __________Select_More:- button is using to get more filters ______
        '''self.more2= ImageTk.PhotoImage(file="More_Filter.png")
        select_More = Button(self.User_Dashboard_Window, image=self.more2, bg="#4e4e4e", borderwidth=0, command=more_Filter)

        #????????????????This line May generating error???????????????'''

        # _____ Hide_Filter:-  butten is using to hide the check buttons _____
        self.more1 = ImageTk.PhotoImage(file="Hide_Filter.png")
        hide_button = Button(self.User_Dashboard_Window, image=self.more1, bg="#4e4e4e",activebackground="#4e4e4e", borderwidth=0, command=Hide_the_chk_buttons)

        # _____Download:- Creating button to generate data set==============================
        self.generate = ImageTk.PhotoImage(file="Download.png")
        Generate_Sample = Button(self.User_Dashboard_Window, image=self.generate, bg="#4e4e4e", activebackground="#4e4e4e",borderwidth=0, cursor="hand2", command=download_Button)


User_Dashboard_Window=Tk()
User_Dash_Board_Object=User_Dash_Board_Class(User_Dashboard_Window)
User_Dashboard_Window.resizable(False, False)
User_Dashboard_Window.mainloop()
