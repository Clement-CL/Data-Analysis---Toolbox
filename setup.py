from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='clem_tools',
      version="1.0",
      description="usefull functions for data viz and preprocessing",
      packages=find_packages(),
      test_suite = 'tests',
      requirements = requirements,
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/clem_toolbox-run'],
      zip_safe=False)
