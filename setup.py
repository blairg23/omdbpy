import os
import setuptools


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as filepath:
        return filepath.read()


def parse_requirements(filename):
    return [line.strip()
            for line in read(filename).strip().split('\n')
            if line.strip()]


pkg = {}
exec(read('src/omdb/__pkg__.py'), pkg)

readme = read('README.md')
requirements = parse_requirements('requirements.txt')

setuptools.setup(
    name=pkg['__package_name__'],
    version=pkg['__version__'],
    url=pkg['__url__'],
    license=pkg['__license__'],
    author=pkg['__author__'],
    author_email=pkg['__email__'],
    description=pkg['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_pacakge_data=True,
    install_requires=requirements,
    keywords='omdb api imdb movies television',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
