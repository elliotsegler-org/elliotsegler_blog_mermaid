from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='elliotsegler_blog_mermaid',
    version='0.0.1',
    author='Elliot Segler',
    author_email='github@elliotsegler.com',
    description='Python-Markdown extension to add support for mermaid graph inside markdown file. Based on md_mermaid',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/elliotsegler-org/elliotsegler_blog_mermaid',
    py_modules=['elliotsegler_blog_mermaid'],
    install_requires = ['markdown>=2.5'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
