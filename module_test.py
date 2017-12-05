import random
# import urllib.request

#import urllib2.urlopen
import urllib

#from urllib2 import urlopen

x = random.randrange(1, 1000)

print x

print random.randrange(1, 1000)
print random.randrange(1, 1000)

print random.randrange(1, 1000)
print random.randrange(1, 1000)
print random.randrange(1, 1000)
 #######################################

def download_image(url):
    file_name = "image_"+str(random.randrange(100, 1000))+".jpg"
    urllib.urlretrieve(url, file_name)

download_image("https://media.licdn.com/mpr/mpr/AAIA_wDGAAAAAQAAAAAAAArJAAAAJGVlMGVmNDZjLTk5NWEtNGI2NC04NzU4LTQzYWQ1YzEwNzJkNg.jpg")
