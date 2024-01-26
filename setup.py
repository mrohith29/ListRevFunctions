from setuptools import setup, find_packages

setup(
    name="ListRevFnctions",
    version="0.1",
    description="Using this package you can petform various operations on two lists with second list reversed like addition, subtraction, multiplication, division, floor division, modulo, power, and, or",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    author="Mariyala Rohith",
    author_email="mariyalarohith29@gmail.com",
    url="https://github.com/mrohith29/ListRevFunctions",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    # install_requires=[
    #     "numpy",  # Example dependency
    #     # Add more dependencies as needed
    # ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)