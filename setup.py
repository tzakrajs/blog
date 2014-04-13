#!/usr/bin/env python

import blog

from setuptools import setup, find_packages

setup(
        name='blog',
        version=blog.__version__,

        description='a very simple blog framework',
        long_description=open('README.rst').read(),

        author='Thomas Zakrajsek',
        author_email='tzakrajs@gmail.com',

        url='https://github.com/tzakrajs/blog',

        scripts=['run_server.py', ],

        include_package_data=True,
        packages=['blog'],
        package_dir={'blog': 'blog'},
        package_data={'blog': ['views/*.tpl',
                               'static/js/*.js',
                               'static/css/*.css',
                               'static/img/*.png',
                               'static/img/*.gif',
                               'controllers/*.py',
                               'models/*.py']},

        license=open('LICENSE').read(),

        install_requires=[
                    'bottle >= 0.12',
                ],

        keywords='blog framework software',
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2.7',
                    'Framework :: Bottle',
                    'Operating System :: OS Independent',
                    'Environment :: Console',
                    'Intended Audience :: Information Technology',
                    'Natural Language :: English',
                    'Topic :: Communications :: Telephony',
                    'License :: OSI Approved :: Apache Software License',
                ],
)
