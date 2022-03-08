![](https://simgbb.com/images/logo.png)
# IMGBB Uploader

Simple program for auto uploading image to imgbb.com

### Bennefits

* Free (but illegal)
* Can upload image from local storage or URL
* Don't need register any account
* Can uploading many image massively

Saddly, i don't add 'auto delete' to this tool, but you can contribute to this project to add it.

### Why IMGBB
imgbb.com is a free image hosting service that allow us save our image online and accessible for public so we can share it in website, social network etc.
But, if you want to use they API, you must purchase pro account.
With this tool, you don't need that because we can upload many images with no charge !

**This tool is free but illegal**
So, please use this tool wisely.


### You must know
imgbb file have one class caled imgBB.
**paramenter**
* `image_source`
image file path, can from local storage or URL

**attributes**
* `json`
All response from imgbb.com server
* `url`
Public URL for our uploaded image
* `thumbnail`
Like it name, it return the thumbnail URL
* `filename`
Same as thumbnail, but it just file name string

### Usage
Before using this tool, you must installing `requests` module
> pip install requests

Code snippet to uploading few images from our local storage
```
from imgbb import imgBB as uploadImage
import os, time


list_images = os.listdir("images_folder")
for image_path in list_images:
	result = uploadImage(image_path)
	print(result.url)
	time.sleep(10)
```
