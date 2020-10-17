# Author ： comma
# 日期 : 2020/10/17  15:04

# 一键抠图
from removebg import RemoveBg
import os

picture=os.listdir('/Users/sun/Pictures/Python')    # 获取该目录下的所有图片的名称，结果是一个列表
rmbg=RemoveBg('Jv9gx9WpMiRLZbxaJJgwaZsh','error.log')
for pic in picture:
    rmbg.remove_background_from_img_file('/Users/sun/Pictures/Python/'+pic)     # 结果图片存放路径