# IMGBB Uploader
# Karjok Pangesty
# March 8th, 2022 9:35 PM

from requests import post

class imgBB:
	def __init__(self,image_source):
		self.image_source = image_source
		self.json = None
		self.url = None
		self.thumbnail = None
		self.filename = None
		self.upload()
	def upload(self):
		# get image name from image path source
		image_name = self.image_source.split("/")[-1]
		# upload data if uploaf image from local storage
		if "http" not in self.image_source:
			form_image = {"source":(image_name,open(self.image_source,"rb"),"multipart/form-data")}
			form_data = {"upload-expiration":"","type":"file","action":"upload"}
			result = post("https://imgbb.com/json",data=form_data,files=form_image).json()

		# and if image source is from url
		else:
			form_data = {"source":self.image_source,"upload-expiration":"","type":"url","action":"upload"}
			result = post("https://imgbb.com/json",data=form_data).json()

		self.json = result
		self.url = result["image"]["url"]
		self.thumbnail = result["image"]["thumb"]["url"]
		self.filename = result["image"]["name"]

if __name__ == "__main__":
	img_source = input("image source: ")
	IMG = imgBB(img_source)
	print(IMG.url)

