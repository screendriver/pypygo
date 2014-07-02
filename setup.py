from setuptools import setup

setup(
    name='pypygo',
    description='A Python wrapper for the DuckDuckGo instant answer API',
    version='0.1.0',
    author='RaspberryRice',
    author_email='christian@echooff.de',
    license='MIT',
    url='https://github.com/ScreenDriver/pypygo',
    packages=['pypygo'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='duckduckgo ddg ddgo search engine privacy',
    install_requires=['requests>=2.3.0']
)
