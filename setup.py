from distutils.core import setup
from setuptools import find_packages
from os.path import dirname, join
import re
#
# Explanation of the regular expression:
#     - ['\"] matches either ' or "
#     - (\d+\.\d+\.\d+) matches #.#.# which is how I version
# 
version_regex = re.compile(r"^__version__ = ['\"](\d+\.\d+\.\d+)['\"]")
this_dir_name = dirname(__file__)
version_path = join(this_dir_name, "_version.py")
#
with open(version_path, 'rb') as f:
    version_file_as_string = f.read()
    match = version_regex.search(version_file_as_string)
#
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s" % version_path)
#
setup(name='example-package',
      version=version,
      description='An Example Package Using a Version File',
      author='Jeff Cochran',
      author_email='koenigcochran@gmail.com',
      packages=find_packages()
)