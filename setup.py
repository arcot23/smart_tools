from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='smart_tools',
    version='0.8',
    description='A variety of smart tools to make analytics easy.',
    author='Prabhuram Venkatesan',
    readme = "README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dissector=smart_tools.dissector.main:main',
            'morpher=smart_tools.morpher.main:main',
        ],
    },
    install_requires=[
        'pandas==2.2.2',
        'pyyaml==6.0.1',
        'xlsxwriter==3.2.0',
        'requests==2.32.3',
        # List your project dependencies here
    ],
    data_files=[
        ('config', ['config/dissector_config.yaml', 'config/iban_config.yaml']),
    ],
    python_requires='>=3.8',
    project_urls = {
        'Home': 'https://pypi.org/project/smart-tools/',
        'Github': 'https://github.com/arcot23/smart_tools',
    },
)
