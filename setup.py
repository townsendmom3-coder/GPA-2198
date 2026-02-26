from setuptools import setup, find_packages

setup(
    name='GPA-2198',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add your package dependencies here
    entry_points={
        'console_scripts': [
            'fidelity_plotter=your_module_name:main',  # Replace 'your_module_name:main' with the actual module and function
        ],
    },
)