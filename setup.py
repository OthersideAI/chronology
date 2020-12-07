from setuptools import setup

setup(
    name='chronological',
    version='0.0.3',
    description='Chain GPT calls like a pro!',
    url='git@github.com:bramses/chronology-ai.git',
    author='Otherside AI',
    author_email='bram@othersideai.com',
    license='unlicense',
    install_requires=['openai', 'python-dotenv'],
    zip_safe=False,
)