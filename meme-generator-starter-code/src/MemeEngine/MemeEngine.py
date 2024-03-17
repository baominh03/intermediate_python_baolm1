from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine():
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def make_meme(self, img_path, text, author, width=500):
        if width >= 500:
            width = 500
        try:
            print(img_path)
            img = Image.open(img_path)
        except Exception:
            raise Exception("Invalid image path")
        
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        
        # Remove ' character
        text = text.replace("\u2019","")
        author = author.replace("\u2019","")

        font_size = int(img.height/20)

        rand_x = random.randint(0, int(width/4))
        rand_y = random.randint(0, int(img.height-font_size*2))
        font = ImageFont.truetype("./_data/font/VNARIS.ttf", int(img.height/15))
        
        draw = ImageDraw.Draw(img)
        draw.text((rand_x, rand_y), text, font=font, fill='red')
        draw.text((int(rand_x * 1.2), (rand_y + font_size)), ('   -'+author), font=font, fill='white')
        
        out_file = (self.output_dir+'/'+str(random.randint(0, 1000))+'.jpg')

        img.save(out_file,"JPEG")

        return (out_file)