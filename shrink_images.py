from PIL import Image
import glob
import os

for raw_path in glob.glob('images_raw/*.*'):
    img = Image.open(raw_path)
    fname = os.path.splitext(os.path.basename(raw_path))[0]
    width, height = img.size
    landscape = width > height
    factor = 400.0 / width if landscape else 400.0 / height
    img = img.resize((int(factor*width), int(factor*height)))
    print(raw_path, '-', img.size)
    img.save('images/{}.JPEG'.format(fname))
