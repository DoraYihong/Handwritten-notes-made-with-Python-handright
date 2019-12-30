from PIL import Image, ImageFont
from handright import Template, handwrite

with open("./文字10.txt", "r") as f:  # 打开文件
    text = f.read()
    print(text)

length = 1445
width = 2060
line_num = 22
left = 140
right = 140
top = 162-10
bottom = 133+10
multiple = 6

template = Template(
    background=Image.new(mode="1", size=(length*multiple, width*multiple), color=1),
    font_size=(width-top-bottom)/line_num*0.7*multiple,
    font=ImageFont.truetype("./Fonts/陈旭东字体.ttf"),
    word_spacing=-5*multiple,  # 字符间距
    line_spacing=(width-top-bottom)/line_num*multiple,
    left_margin=left*multiple,
    top_margin=top*multiple,
    right_margin=right*multiple,
    bottom_margin=bottom*multiple
)
images = handwrite(text, template)
i = 23
for im in images:
    assert isinstance(im, Image.Image)
    im.save('./生成/' + str(i) + '.jpg')
    print(str(i)+".jpg generated")
    i += 1
