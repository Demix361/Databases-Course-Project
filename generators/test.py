
image_f = '10_2_sjdhbf'
color = image_f[0:image_f.find('_')]
var = image_f[len(color) + 1:image_f[len(color) + 1:].find('_') + len(color) + 1]
print(len(color) + 1)
print(image_f[len(color) + 1:].find('_'))

print(color, var)