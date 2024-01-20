from setuptools import find_packages, setup

package_name = 'person_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pragya',
    maintainer_email='pragya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "person_follower_py=person_follower.person_follower:main",
            "Person=person_follower.Person:main",
            "Person_follower_IS=person_follower.Person_follower_IS:main"
        ],
    },
)
