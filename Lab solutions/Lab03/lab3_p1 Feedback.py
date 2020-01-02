import math

inp = input('Enter USB size (GB): ')

inpbyte = 100000*int(inp)

pixel = inpbyte / 8 / 6

gif = math.floor(pixel / (8 / 8) * 5)
jpeg = math.floor(pixel / (24 / 8) * 25)
png = math.floor(pixel / (24 / 8) * 8)
tiff = math.floor(pixel / (48 / 8))

print(format(gif, '>5'), 'images in GIF format can be stored')
print(format(jpeg, '>5'), 'images in JPEG format can be stored')
print(format(png, '>5'), 'images in PNG format can be stored')
print(format(tiff, '>5'), 'images in TIFF format can be stored')

# Feedback : -1 wrong coding style : missing comment
