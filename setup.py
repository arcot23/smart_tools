from setuptools import setup, find_packages

setup(
    name='smart_tools',
    version='0.2',
    description='A variety of smart tools to make analytics easy.',
    author='Prabhuram Venkatesan',
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
        # List your project dependencies here
    ],
    data_files=[
        ('config', ['config/dissector_config.yaml', 'config/iban_config.yaml']),
    ],
    python_requires='>=3.8',
)
