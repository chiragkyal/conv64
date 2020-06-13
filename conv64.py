import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2


def base2img(base64_string,image_type='opencv'):

	if image_type == 'opencv':
		image_bytes = base64.b64decode(base64_string)
		image_array = np.frombuffer(image_bytes, dtype=np.uint8)
		image = cv2.imdecode(image_array, flags=cv2.IMREAD_COLOR)
		return image 

	
	elif image_type == 'pillow':
		
		image_bytes = base64.b64decode(base64_string)
		image_file_obj = BytesIO(image_bytes)
		image = Image.open(image_file_obj)
		return image

	else:
		print("Unable to Convert to Image: Check Image Type")



def img2base(image,image_type='opencv'):

	##TODO -> Add different file Extension

	if image_type == 'opencv':
		
		#Send Opencv Image 
		#e.g image = cv2.imread("fig.jpg")

		_, image_arr = cv2.imencode('.jpg', image)
		image_bytes = image_arr.tobytes()
		base64_string = base64.b64encode(image_bytes)
		return base64_string

	elif image_type == 'pillow':

		#Send Pillow Image 
		#e.g image = Image.open("fig.jpg")

		image_file = BytestIO()
		image.save(image_file, format="JPEG")
		image_bytes = image_file.getvalue()
		base64_string = base64.b64encode(image_bytes)
		return base64_string
