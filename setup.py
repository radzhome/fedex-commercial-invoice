from setuptools import setup, find_packages


setup(
    name='fedex_commercial_invoice',
    version='0.1',
    author_email='radzhome@gmail.com',
    packages=find_packages(),
    install_requires=['reportlab'],
    include_package_data=True,
    url='https://github.com/radlws/fedex-commercial-invoice/',
    license='',
    description='Fedex Commercial Invoice generator.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
