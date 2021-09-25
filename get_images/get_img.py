import subprocess
import cv2
from bs4 import BeautifulSoup
import requests
import os
#================create folder=============
def create_dir(images, pth):
    os.mkdir(pth)

url = "https://www.prothomalo.com/"
html = requests.get(url).text # get the html
soup = BeautifulSoup(html, "lxml") # give the html to soup
images = soup.findAll('img')
pth = 'images'
create_dir(images, pth)

#============== to resize images=================
def resize_img(img_dir):
    save_dir = 'preprocessed/'
    for img_name in os.listdir(img_dir):
        pth_to_img = img_dir+'/'+img_name
        img = cv2.imread(pth_to_img)
        img = cv2.resize(img, (224, 224))
        cv2.imwrite(save_dir+img_name, img)


url = 'https://www.prothomalo.com/'#"https://example.site/page/with/images"
html = requests.get(url).text # get the html
soup = BeautifulSoup(html, "lxml") # give the html to soup

# get all the anchor links with the custom class 
# the element or the class name will change based on your case
imgs = soup.findAll("a", {"class": "envira-gallery-link"})
for img in imgs:
    imgUrl = img['href'] # get the href from the tag
    cmd = [ 'wget', imgUrl ] # just download it using wget.
    subprocess.Popen(cmd) # run the command to download
    # if you don't want to run it parallel;
    # and wait for each image to download just add communicate
    subprocess.Popen(cmd).communicate()