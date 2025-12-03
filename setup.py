from setuptools import setup, find_packages

setup(
    name='d10z',
    version='0.1.0',
    description='Framework D10Z-TTA (Big Start, TTA, infifotón, etc.)',
    author='Jamil Al Thani',
    author_email='jamil@d10z.org',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
