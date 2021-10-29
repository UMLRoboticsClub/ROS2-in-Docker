from setuptools import find_packages
from setuptools import setup

package_name = 'node'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Roshan Ravi',
    author_email='roshan@roshanravi.com',
    maintainer='Roshan Ravi',
    maintainer_email='roshan@roshanravi.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Talker Example'
    ),
    license='MIT License',
    entry_points={
        'console_scripts': [
            'talker = node.topics.talker:main'
        ],
    },
)
