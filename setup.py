try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is Go Fish The Game!',
    'author': 'Cold Sun',
    'url': 'URL to get it at.',
    'download_url': 'No Where!',
    'author_email': 'bikingrox@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['gofish'],
    'scripts': [],
    'name': 'gofish'
}

setup(**config)
