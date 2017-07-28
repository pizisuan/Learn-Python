from PIL import Image
from PIL import ImageFilter
im = Image.open("One_Peace.png")
em = im.filter(ImageFilter.EMBOSS)
om = im.filter(ImageFilter.CONTOUR)
sm = im.filter(ImageFilter.SHARPEN)
em.save("One_Peace_EMBOSS.png")
om.save("One_Peace_CONTOUR.png")
sm.save("One_Peace_SHARPEN.png")
