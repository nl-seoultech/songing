# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
]

test_requires = [
    'pytest >= 2.3.5'
]

setup(name='songing',
      description=u'좋아하는 노래를 분석하는 프로그램',
      author='Bongyong Choi, Kyungsun Park',
      author_email='exe91@naver.com, asinta@naver.com',
      packages=find_packages(),
      install_requires=install_requires,
      test_require=test_requires)
