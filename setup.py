from setuptools import setup


setup(
    name="HelloWorld",
    version='1.0.0',
    py_modules=['hello'],
    packages=["clickmc"],
    author="Tony McClay",
    author_email="anthony.mcclay@gmail.com",
    description="This is an example click app",
    license="Apache",
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
        first=clickmc.first:hello
    '''
)
