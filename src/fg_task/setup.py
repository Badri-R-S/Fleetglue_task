from setuptools import find_packages, setup

package_name = 'fg_task'

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
    maintainer='badri',
    maintainer_email='badrinarayanan008@gmail.com',
    description='TODO: Package description',
    license='Apace-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "task_publisher = fg_task.task_publisher:main",
            "rn1 = fg_task.rn1:main",
            "rn2 = fg_task.rn2:main",
        ],
    },
)
