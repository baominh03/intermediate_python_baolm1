from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine():
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def make_meme(self, img_path, text, author, width=500):
        img = Image.open(img_path)
        
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        
        # Remove ' character
        text = text.replace("\u2019","")
        author = author.replace("\u2019","")

        rand_x = random.randint(0, int(width/2))
        rand_y = random.randint(0, int(height/2))
        font = ImageFont.truetype("./_data/font/VNARIS.ttf", int(img.height/15))
        
        draw = ImageDraw.Draw(img)
        draw.text((rand_x, rand_y), text, font=font, fill='red')
        draw.text((rand_x, (rand_y+50)), ('   -'+author), font=font, fill='white')
        
        out_file = (self.output_dir+'/'+str(random.randint(0, 1000))+'.jpg')

        img.save(out_file,"JPEG")

        return (out_file)