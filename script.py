from PIL import Image

import pytesseract


imgname = "18-40-00_E35.jpg"
im = Image.open(imgname)



crop_rectangle = (262, 655, 348, 675)
cropped_im = im.crop(crop_rectangle)

freq = pytesseract.image_to_string(cropped_im).strip().replace(',','.') 

crop_rectangle = (365, 655, 450, 675)
cropped_im = im.crop(crop_rectangle)

freqerr = pytesseract.image_to_string(cropped_im).strip().replace(',','.')



print(freq, ' GHz' , ' +/- ' , freqerr, ' kHz') 


#cropped_im.show()




