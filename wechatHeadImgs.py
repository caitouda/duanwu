#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# __author__='阳光流淌007'
# __date__ = '2018-03-06'
import itchat
import os
from math import sqrt
from PIL import Image

itchat.auto_login()
os.makedirs("C:\\images\\headImages\\")
for friend in itchat.get_friends(update=True)[0:]:
    # 可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
    print(friend['NickName'], friend['RemarkName'], friend['Sex'], friend['Province'], friend['Signature'])
    img = itchat.get_head_img(userName=friend["UserName"])
    path = "C:/images/headImages/" + friend['NickName'] + "(" + friend['RemarkName'] + ").jpg"
    try:
        with open(path, 'wb') as f:
            f.write(img)
    except Exception as e:
        print(repr(e))


# path是存放好友头像图的文件夹的路径
path = 'C:/images/headImages/'
path2 = 'C:/images/'
pathList = []
for item in os.listdir(path):
    imgPath = os.path.join(path, item)
    pathList.append(imgPath)
total = len(pathList)  # total是好友头像图片总数
line = int(sqrt(total))  # line是拼接图片的行数（即每一行包含的图片数量）
NewImage = Image.new('RGB', (128 * line, 128 * line))
x = y = 0
for item in pathList:
    try:
        img = Image.open(item)
        img = img.resize((128, 128), Image.ANTIALIAS)
        NewImage.paste(img, (x * 128, y * 128))
        x += 1
    except IOError:
        print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
        x -= 1
    if x == line:
        x = 0
        y += 1
    if (x + line * y) == line * line:
        break
NewImage.save(path2 + "final.jpg")
itchat.run()