# imports 
from PIL import Image, ImageDraw, ImageFont 
import pandas as pd
   
def certificates(names: list, certificate: str, font_path: str): 
   
    for name in names: 
          
        # adjust the position according to  
        # your sample 
        text_y_position = 335
   
        # opens the image 
        img = Image.open(certificate, mode ='r') 
          
        # gets the image width 
        image_width = img.width 
          
        # gets the image height 
        # image_height = img.height  
   
        # creates a drawing canvas overlay  
        # on top of the image 
        draw = ImageDraw.Draw(img) 
   
        # gets the font object from the  
        # font file (TTF) 
        font = ImageFont.truetype( 
            font_path, 
            54 # change this according to your needs 
        ) 
   
        # fetches the text width for  
        # calculations later on 
        text_width, _ = draw.textsize(name, font = font) 
   
        draw.text( 
            ( 
                # this calculation is done  
                # to centre the image 
                (image_width - text_width) / 2, 
                text_y_position 
            ), 
            name,
            fill="#43668F",
            font = font        ) 
   
        # saves the image in png format 
        img.save("recognition/{}.png".format(name))  
  
# Driver Code 
if __name__ == "__main__": 
   
    # some example of names 
    df = pd.read_excel('outstanding-dataset.xlsx', sheet_name=0) # can also index sheet by name or fetch all sheets
    NAMES = df['Nombre completo'].tolist()
    print(f"Creando {len(NAMES)} certificados de Python Summer Coding Camp...")
      
    # path to font 
    FONT = "C:/Users/Sharif/AppData/Local/Microsoft/Windows/Fonts/PlayfairDisplay-Italic-VariableFont_wght.ttf"
      
    # path to sample certificate 
    CERTIFICATE = "recognition-certificate-pscc.png"
   
    certificates(NAMES, CERTIFICATE, FONT)
    print("Done!")