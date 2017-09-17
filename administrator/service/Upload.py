
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

class Upload:
  dir = ""

  def __init__(self):

      self.upload  = cloudinary.config(
        cloud_name="dev-tads",
        api_key="923851321941484",
        api_secret="_d9CXIcOB4eB5Le1LSEuUV65bTA"
      )

  def setDir(self, dir):
      self.dir = dir

  def process(self, filePath):
      return cloudinary.uploader.upload(
                settings.MEDIA_ROOT + "/"+ filePath,
                folder= self.dir
             )