from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='chronological',
    version='0.1.0',
    description='Chain GPT calls like a pro!',
    url='https://github.com/OthersideAI/chronology',
    author='Otherside AI',
    author_email='bram@othersideai.com',
    license='unlicense',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['openai', 'python-dotenv', 'loguru'],
    zip_safe=False,
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)