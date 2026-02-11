from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """

    This function reads the requirements.txt file and returns a list of dependencies.

    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from the file
            lines= file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Shivam Sawarn',
    author_email='sawarnshivam9895@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)