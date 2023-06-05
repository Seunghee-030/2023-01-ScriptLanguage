'''
setup.py
distutils 모듈을 사용해 배포 파일을 생성하는 파일
'''
from distutils.core import setup, Extension

module_cLink = Extension('cLink', sources = ['cLinkModule.c'])

setup(
    name='BBus',
    version='1.0',

    py_modules=['book_mark', 'graph', 'link', 'map', 'server', 'telegram_bot', 'telegram', 'BBus'],

    packages=['image', 'font'],
    package_data={
        'image': ['*.png', '*.html','*.jpg','*.gif'],
        'font': ['*.ttf']},
    ext_modules=[module_cLink]
)