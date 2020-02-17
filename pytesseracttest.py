try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import os
import re 


directory = '/Users/pvaloyi/projects/python/wordFinder/testImages'
#img='testImages/test1.jpg'
findThis= '^(Verizon)$'


#results= re.findall(findThis, d['text'])
#print(results)


for pics in os.listdir(directory):
   if pics.endswith(".jpg") or pics.endswith(".png"):
     picsResult= os.path.join(directory, pics)
     #print(picsResult)
     d= pytesseract.image_to_data(picsResult, output_type=Output.DICT)
     thisDict = len(d['text'])
for i in range(thisDict):
        if re.match(findThis , d['text'][i]):
            print(i)