from setuptools import setup, find_packages
from typing import List
def get_requirements(path:str) ->List[str]:
    data =[]
    HYPHEN_E_DOT = "-e ."
    with open(path) as f:
        data = f.readlines()
        data = [d.replace("\n", "")for d in data]
        if HYPHEN_E_DOT in data:
            data.remove(HYPHEN_E_DOT)
        return data
    
setup(
name="RAG",
author="jck",
author_email="jck@maurices.com",
package_dir={"": "src"},
packages=find_packages(where="src"),
install_requires=get_requirements('requirements.txt')
)