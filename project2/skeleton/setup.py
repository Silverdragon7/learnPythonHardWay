try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mój projekt',
    'author': 'Moje nazwisko',
    'url': 'Adres URL, z którego można go pobrać',
    'download_url': 'Gdzie go można pobrać.',
    'author_email': 'Mój emil',
    'version': '0,1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'nazwa projektu'
}

setup(**config)