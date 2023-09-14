from setuptools import find_packages , setup

from typing import List
def get_requirements(filepath:str)->List[str]:

    '''Function returns the list of requirements'''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if "-e ." in requirements:
            requirements.remove('-e .')
    return requirements

setup(

    name="mlproject",
    version="0.0.1",
    author="Kamalesh",
    author_email='kmgowda1512@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)