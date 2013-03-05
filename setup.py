from setuptools import setup


VERSION = '0.0.1'
NAME = 'gh'

install_requires = [
    'PyGithub'
]


if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        author='Matthew Hooker',
        author_email='mwhooker@gmail.com',
        url='https://github.com/mwhooker/gh',
        description='GitHub API CLI tool.',
        license='Apache License 2.0',
        zip_safe=False,
        install_requires=install_requires,
        include_package_data=True
    )
