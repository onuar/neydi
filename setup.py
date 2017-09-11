from setuptools import setup, find_packages
import neydi


def read_me_content():
    with open('README.MD') as f:
        content = f.read()
    f.close()
    return content


setup(
    name='neydi',
    version=neydi.__version__,
    description='Most forgetable console line commands',
    long_description=read_me_content(),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6.2",
        "Topic :: Documentation"
    ],
    keywords='neydi help console commands command line',
    author='Onur Aykac',
    author_email='onuraykac@gmail.com',
    maintainer='Onur Aykac',
    maintainer_email='onuraykac@gmail.com',
    url='https://github.com/onuar/neydi',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'neydi = neydi.neydi:command_line_runner',
        ]
    },
    install_requires=[

    ]
)
