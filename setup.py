from setuptools import setup


setup(
    name='wideq',
    version='0.0.1',
    description='LG SmartThinQ API client',
    author='Per-Arne Hellarvik',
    author_email='duckboot@gmail.com',
    url='https://github.com/phellarv/wideq',
    license='MIT',
    platforms='ALL',
    install_requires=['requests'],
    py_modules=['wideq'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
