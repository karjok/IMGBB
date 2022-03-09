<img src="https://simgbb.com/images/logo.png" width="300px">

## IMGBB Image Uploader

A simple program to automatically upload images to https://imgbb.com

### Benefit

* Free (but illegal)
* Can upload images from local storage or URL
* No need to register any account
* Can upload multiple images in bulk

Unfortunately, I didn't add 'auto delete' to this tool, but you can contribute to this project to add it.

### Why IMGBB
imgbb.com is a free image hosting service that allows us to save images online and accessible to the public so that we can share them on websites, social networks, etc.

But, if you want to use their API, you have to buy a pro account.

With this tool, you don't need it because we can upload multiple images for free!

**This tool is free but illegal. So please use this tool wisely.**


### You should know
The imgbb file has one class called `imgBB`. 

**Parameter**
* `image_source`
Image file path, can be from local storage or URL


**Attributes**

* `json`
All responses from imgbb.com server

* `url`
Public URL for the image we uploaded
* `thumbnail`
As the name suggests, it returns a thumbnail URL
* `filename`
Same as thumbnail, but only filename string


### Usage
Before using this tool, you must install the `requests` module

> pip install request

Code snippet to upload image from our local storage


**Single image**
```
from imgbb import imgBB
import json

image = "my-image.jpg"
result = imbBB(image)
print(json.dumps(result,indent=2))
```

The code above will print formatted json from response result


**Multiple images**
```
from imgbb import imgBB as uploadImage
import os, time


list_images = os.listdir("images_folder")
for image_path in list_images:
	result = uploadImage(image_path)
	print(result.url)
	time.sleep(10)
```
And the code above will display the url of each photo uploaded to imgbb
