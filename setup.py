from setuptools import setup


setup(
    name="HelloWorld",
    version='1.0.0',
    py_modules=['hello'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)
