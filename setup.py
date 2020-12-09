from setuptools import setup, find_packages

setup(
    name='chronological',
    version='0.0.6',
    description='Chain GPT calls like a pro!',
    url='https://github.com/bramses/chronology.git',
    author='Otherside AI',
    author_email='bram@othersideai.com',
    license='unlicense',
    packages=find_packages(),
    install_requires=['openai', 'python-dotenv'],
    zip_safe=False,
    python_requires='>=3.7',
)