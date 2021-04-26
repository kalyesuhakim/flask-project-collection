import glob
import imagehash
from PIL import Image

my_image_url = './me/me.jpg'
my_hash = imagehash.average_hash(Image.open(my_image_url))

girls = glob.glob('./pics/*.jpg')
selected = girls[0]
accepted = 30

for girl in girls:
    girl_hash = imagehash.average_hash(Image.open(girl))
    diff = girl_hash - my_hash
    if diff < accepted:
        selected = girl_hash
        accepted = diff

bf_img = Image.open(my_image_url)
gf_img = Image.open(accepted)

couple_img = Image.new('RGB', (bf_img.width + gf_img.width, gf_img.height))
couple_img.paste(gf_img,(0,0))
couple_img.paste(bf_img,(bf_img.width ,0))
couple_img.save('couple.jpg')
couple_img.show()
