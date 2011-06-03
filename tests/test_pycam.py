from uc480 import pycam

def test_open_camera():
	camera = pycam()
	del camera

class Test_camera(object):

	def setUp(self):
		self.camera = pycam()

	def tearDown(self):
		del self.camera

	def test_image_size(self):
		foo = (500,500)
		self.camera.image.size = foo
		assert self.camera.image.size == foo 

	def test_image_size_fail(self):
		foo = (-1,-1)
		try:
			self.camera.image.size = foo
		except Exception as e:
			assert e.args[0] == "An invalid parameter was specified"

	def test_image_position(self):
		foo = (0,0)
		self.camera.image.position = foo
		assert self.camera.image.position == foo 
	
	def test_image_position_fail(self):
		foo = (1,0)
		try:
			self.camera.image.position = foo
		except Exception as e:
			assert e.args[0] == "An invalid parameter was specified"
		assert self.camera.image.position == (0,0)