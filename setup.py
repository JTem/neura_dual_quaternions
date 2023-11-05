from setuptools import setup, find_packages

setup(
    name='neura_dual_quaternions',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    
    # Other metadata
    author='Jens Temminghoff',
    author_email='jens.temminghoff@neura-robotics.com',
    description='A simple package for Dualquaternion and Quaternion maths',
    keywords=['quaternion', 'dualquaternion', 'robotics', 'geometric algebra', 'kinematics'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
