from PIL import Image

im = Image.open('foto.png')

print("format file: " + im.format)
print("ukuran file: " + str(im.size))
print("mode file: " + im.mode)

im.show()