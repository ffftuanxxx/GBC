from deoldify import device
from deoldify.device_id import DeviceId

device.set(device=DeviceId.GPU0)

from deoldify.visualize import *
plt.style.use('dark_background')
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_video_colorizer()

#NOTE:  Max is 44 with 11GB video cards.  21 is a good default
render_factor=21
#NOTE:  Make source_url None to just read from file at ./video/source/[file_name] directly without modification
source_url=None
file_name = 'images'
file_name_ext = file_name + '.mp4'
result_path = None

if source_url is not None:
    result_path = colorizer.colorize_from_url(source_url, file_name_ext, render_factor=render_factor)
else:
    result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)
