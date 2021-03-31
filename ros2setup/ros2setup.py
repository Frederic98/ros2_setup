import xml.etree.ElementTree as ET
import os
import inspect
from typing import Dict


class Ros2Setup:
    _module_file = os.path.abspath(__file__)
    _xml_files = {}         # type: Dict[str, ET.Element]

    @classmethod
    def _get_caller_fn(cls):
        for frame in inspect.stack():
            frame_fn = os.path.abspath(frame[1])
            if frame_fn != cls._module_file:
                return frame_fn

    @classmethod
    def _get_xml(cls):
        frame_fn = cls._get_caller_fn()
        xml_fn = os.path.join(os.path.dirname(frame_fn), 'package.xml')
        if xml_fn not in cls._xml_files:
            tree = ET.parse(xml_fn)
            cls._xml_files[xml_fn] = tree.getroot()
        return cls._xml_files[xml_fn]

    @classmethod
    def _get_element(cls, tag: str):
        return cls._get_xml().find(tag)

    @classmethod
    def tag(cls, tag: str) -> str:
        """Get the content of the specified tag"""
        return cls._get_element(tag).text

    @classmethod
    def attrib(cls, tag: str, name: str) -> str:
        """Get the value of an attribute of the specified tag"""
        return cls._get_element(tag).get(name)

    @classmethod
    def readme(cls, filetype='md'):
        """Get the contents of the README file.
        filetype can be one of ['md', 'rst', 'txt'], and should be the file extension of the README file"""
        readme_fn = os.path.join(os.path.dirname(cls._get_caller_fn()), 'README.'+filetype)
        with open(readme_fn, "r", encoding="utf-8") as f:
            return f.read()
