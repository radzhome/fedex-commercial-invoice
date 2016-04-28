from setuptools import setup, find_packages

import fedex_invoice

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'fedex commercial invoice generator using reportlab'

setup(
    name='fedex-invoice',
    version=fedex_invoice.__version__,
    author='radzhome',
    author_email='radzhome@gmail.com',
    maintainer='radzhome',
    packages=find_packages(),
    install_requires=['reportlab'],
    include_package_data=True,
    download_url='TODO',
    url='https://github.com/radzhome/fedex-commercial-invoice/',
    license='BSD',
    description='Fedex Commercial Invoice generator, invoice templating using reportlab',
    long_description=open('README.md').read(),
    platforms=['Platform Independent'],
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
)
