#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


VERSION = '0.1.0'
PACKAGE_NAME = 'Project_hello'
DESC = """Gdsdasda.
"""
ENTRY_POINTS = {
    'trac.plugins': [
        'project_hello.project_hello = project_hello.project_hello',
    ],
}
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="GoldCap dfsdf Box Plugin.",
    author='Charlie Tian',
    author_email='charlie.tian@spsoft-cn.com',
    license='BSD',
    url="http://www.spsoft-cn.com/",
    requires=['trac'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests*']),
    package_data={
        'project_hello': [
            'templates/*.html',
            'htdocs/js/*.js',
            'htdocs/css/*.*',
            'htdocs/css/images/*.*',
            'locale/*/LC_MESSAGES/*.mo',
        ]
    },
    zip_safe=True,
    include_package_data=True,
    entry_points=ENTRY_POINTS,
    long_description=DESC,
    extras_require={'Babel': 'Babel>= 0.9.5'},
)
