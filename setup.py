from setuptools import setup, find_packages

with open('README.md', 'r') as file_readme:
    long_desc = file_readme.read()

setup(
    name='fViz',
    version='0.0.1',
    maintainer='fastboardAI',
    author='Sampreet Kalita',
    desctiption='A Light-weight Visualization Library',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='http://github.com/fastboardAI/fViz',
    packages= find_packages(),
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
          ],
    license='MIT',
    install_requires=[
        'matplotlib>=3.0',
        'numpy>=1.10',
        'seaborn>=0.10',
        'setuptools>=40.0'
    ],
    python_requires='>=3.7',
    zip_safe=False
)
