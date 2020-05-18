import setuptools

setuptools.setup(
    name="frankenpoem", # Replace with your own username
    version="7.0.0",
    author="Kyelee Fitts",
    author_email="kyelee.fitts@gmail.com",
    description="Generate poems cobbled together from the remains of older, better poems, with a particular emphasis on rhyme and meter consistency.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruthlee/frankenpoems",
    packages=setuptools.find_packages(),
    install_requires = ['pandas', 'pronouncing'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data = True,
    package_data = {"": ["data.pkl.compress"]}
)