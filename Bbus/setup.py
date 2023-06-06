'''
setup.py
distutils 모듈을 사용해 배포 파일을 생성하는 파일
'''
from distutils.core import setup, Extension

module_cLink = Extension('cLink', sources = ['cLinkModule.c'])

setup(
    name='BBus',
    version='1.0',

    py_modules=[ 'BBus', 'book_mark', 'graph', 'link', 'map', 'server', 'noti', 'teller'],

    packages=['image', 'font', 'telelog'],
    package_data={
        'image': ['*.png', '*.html','*.jpg','*.gif'],
        'font': ['*.ttf'],
        'telelog': ['*.db']},
    ext_modules=[module_cLink]
)