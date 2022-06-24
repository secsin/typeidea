# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/14 23:00
# @File : setup
# @Project : typeidea
# coding:utf-8
from setuptools import setup, find_packages

setup(
    name='typeidea',
    # version='${version}',
    version='0.1',
    description='Blog System base on Django',
    author='secsin',
    author_email='cjc6319@gmail.com',
    url='',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    # package_data={'': [    # 打包数据文件，方法一
    # 'themes/*/*/*/*',  # 需要按目录层级匹配
    # ]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'django==1.11.17',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'xadmin==0.6.1',
        'mysqlclient==2.0.3',
        'django-ckeditor==5.6.1',
        'djangorestframework==3.10.0',
        'django-redis==4.7.0',
        'django-autocomplete-light==3.9.4',
        'Markdown==3.3.7',
        'Pillow==5.3.0',
        'coreapi==2.3.3',
        'hiredis==2.0.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django-silk==2.0.0',
    ],
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

)
