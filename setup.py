from setuptools import setup, find_packages
from os import path

this = path.abspath(path.dirname(__file__))
with open(path.join(this, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='trend-monitoring',
    version='0.0.1',
    description='Real-time Trend Data Analysis/Monitoring System',
    author='Jihoon Kang',
    author_email='jihoon522@naver.com',
    url='https://github.com/thisishoon/trend-monitoring',
    # download_url='https://github.com/doorBW/pypi_deploy_test/archive/master.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires=['requests', 'bs4'],
    # 등록하고자 하는 패키지를 적는 곳입니다.
    # 우리는 find_packages 라이브러리를 이용하기 때문에 아래와 같이 적어줍니다.
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적어줍니다.
    packages=find_packages(exclude=[]),
    # 패키지의 키워드를 적습니다.
    keywords=['trend', 'monitering'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    python_requires='>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함시켜야 합니다.
    package_data={},
    # 위의 package_data에 대한 설정을 하였다면 zip_safe설정도 해주어야 합니다.
    zip_safe=False,
    # PyPI에 등록될 메타 데이터를 설정합니다.
    # 이는 단순히 PyPI에 등록되는 메타 데이터일 뿐이고, 실제 빌드에는 영향을 주지 않습니다.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
