import os 
from PIL import Image
from shutil import copy2
localappdata = os.environ['LOCALAPPDATA']
srcPath = fr'{localappdata}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
destPath = fr'{os.getcwd()}\pics'

fileList = os.listdir(srcPath)
os.makedirs(destPath, exist_ok = True)

for item in fileList:
	im=Image.open(srcPath + '\\' + item)
	copy2(srcPath + '\\' + item, destPath + '\\' + item + '.jpg')
	print('成功拷到一个图片~~')