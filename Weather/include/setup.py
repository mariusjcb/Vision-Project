from distutils.core import setup

VERSION = '0.0.1'
PACKAGES = ['WeatherAPI']

setup(
    name = 'WeatherAPI',
    version = VERSION,
    author = 'Marius Ilie - Vision Proj.',
    author_email ='marius@iliemarius.ro',
    description = 'This module contains a couple of functions to talk with APIXU API as client',
    packages = PACKAGES,
    include_package_data = True,
    install_requires = [
        'requests'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers'
    ],
)
