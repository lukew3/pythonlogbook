from setuptools import setup, find_packages

setup(
    name='logbook',
    version='1.2',
    description='A simple logbook made with python',
    url='https://github.com/lukew3/logbook',
    author='Luke Weiler',
    author_email='lukew25073@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['logbook=logbook.addentry'] #add combine logs when you can
    )
)
