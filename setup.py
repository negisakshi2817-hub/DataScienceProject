from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:#this function will return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()#read the file and return the list of requirements
        requirements = [req.replace("\n","") for req in requirements]#replace the newline with empty string
    return requirements 
setup(
    name = 'data science',
    version = '0.0.1',
    author = 'SakshiNegi',
    author_email = 'negisakshi2817@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt'),
    url = 'https://github.com/negisakshi2817/data-science',
    description = 'A package for data science',
    long_description = 'A package for data science',
    long_description_content_type = 'text/markdown',
    classifiers = ['Programming Language :: Python :: 3'],
)