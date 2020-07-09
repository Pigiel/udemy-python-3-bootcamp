#/usr/bin/env python3
from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print('Word Matrix size: ' + str(word_matrix.size))
print('Mask size: ' + str(mask.size))

mask = mask.resize((1015, 559))
print('Mask after resize: ' + str(mask.size))
mask.putalpha(128)

word_matrix.paste(im=mask, box=(0,0), mask=mask)

print('Solution saved to file: solution.png')
word_matrix.save('solution.png')