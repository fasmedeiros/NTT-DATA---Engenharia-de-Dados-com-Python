from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1.0',
    description='Um pacote simples para processamento de imagens em Python.',
    author='Fabrício de Medeiros',
    author_email='gannba@hotmail.com',
    packages=find_packages(),
    install_requires=['Pillow'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
