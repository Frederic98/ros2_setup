# Ros2Setup

This project is a tiny python library made for ROS2 modules to simplify the packaging process.  
Instead of having two files -`setup.py` and `package.xml`- with the same duplicated information, this module makes it easy dynamically import the information from the `package.xml` into the python setup file.

This way, only the _package.xml_ file has to be edited, to prevent having the two files with conflicting information.
## Installing
Either install with `pip install ros2setup`, or copy _ros2setup.py_ next to your _setup.py_ so that it is accessible from there.

## Usage
```python
from setuptools import setup
from ros2setup import Ros2Setup

package_name = Ros2Setup.tag('name')
setup(
    name=package_name,
    version=Ros2Setup.tag('version'),
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer=Ros2Setup.tag('maintainer'),
    maintainer_email=Ros2Setup.attrib('maintainer', 'email'),
    description=Ros2Setup.tag('description'),
    license=Ros2Setup.tag('license'),
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'streamer = mypackage.submodule:main',
        ],
    },
)
```
