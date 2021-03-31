import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ros2setup",
    version="1.1",
    author="Frederic",
    description="Python library for the ROS2 module setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Frederic98/ros2_setup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
