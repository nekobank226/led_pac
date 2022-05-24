from setuptools import setup

package_name = 'led_pac'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kawamuralab-rspi4',
    maintainer_email='103983489+nekobank226@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_key_node = led_pac.pub_key:main',
            'sub_key_node = led_pac.sub_key:main',
            'sub_joy_node = led_pac.sub_joy:main'
        ],
        
    },
)
