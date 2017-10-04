try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Import data from documents by learning to read a person\'s specific handwriting.',
        'author': 'Zach Woodward',
        'url': 'zach-woodward.com',
        'download_url': 'zach-woodward.com/does_not_exist/',
        'author_email': 'zachw38@gmail.com',
        'version': '0.1',
        'install_requires': ['nose', 'cv2', 'numpy'],
        'packages': ['docreader'],
        'scripts': [],
        'name': 'DocReader'
}

setup(**config)
