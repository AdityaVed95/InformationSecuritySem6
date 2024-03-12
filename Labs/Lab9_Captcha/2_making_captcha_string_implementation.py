# Import the following modules
from captcha.image import ImageCaptcha

import random
mapping_dictionary = {
1: 'a',
2: 'b',
3: 'c',
4: 'd',
5: 'e',
6: 'f',
7: 'g',
8: 'h',
9: 'i',
10: 'j',
11: 'k',
12: 'l',
13: 'm',
14: 'n',
15: 'o',
16: 'p',
17: 'q',
18: 'r',
19: 's',
20: 't',
21: 'u',
22: 'v',
23: 'w',
24: 'x',
25: 'y',
26: 'z'
}

captcha_string = ""

r1 = random.randint(1, 9)

for i in range(r1):
    r2 = random.randint(1,9)

    if r2<6:
        # next symbol is digit
        r3 = random.randint(0,9)
        captcha_string += str(r3)

    else:
        # next symbol is alphabet
        r3 = random.randint(1,26)
        captcha_string += mapping_dictionary[r3]

# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

# generate the image of the given text
data = image.generate(captcha_string)

image.write(captcha_string,"captcha.png")