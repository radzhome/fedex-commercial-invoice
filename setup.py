from setuptools import setup, find_packages


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
    name='FedexInvoice',
    version='0.1',
    author='Radzhome',
    author_email='radzhome@gmail.com',
    packages=find_packages(),
    install_requires=['reportlab'],
    include_package_data=True,
    url='https://github.com/radlws/fedex-commercial-invoice/',
    license='BSD',
    description='Fedex Commercial Invoice generator.',
    long_description=open('README.md').read(),
    platforms=['Platform Independent'],
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
)
