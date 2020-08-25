from setuptools import setup, find_packages
from os import path


def file(path: str) -> str:
    with open('README.md', encoding='utf8') as f:
        description = f.read()
    return description


setup(
    name='tremo',
    version='0.3.2',
    description='Real-time Trend Data Analysis/Monitoring System',
    author='Jihoon Kang',
    author_email='jihoon522@naver.com',
    url='https://github.com/thisishoon/trend-monitoring',
    # 해당 패키지를 사용하기 위해 필요한 패키지
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires=['bs4', 'konlpy', 'krwordrank', 'elasticsearch', 'newspaper3k', 'requests'],
    #.find_packages 라이브러리를 사용하여 등록하고자 하는 패키지
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적어줍니다.
    packages=find_packages(exclude=[]),
    # 패키지의 키워드를 적습니다.
    keywords=['trend', 'tremo', 'monitoring', 'analysis', 'portal', 'search_word'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    python_requires='>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함시켜야 합니다.
    package_data={},
    # 위의 package_data에 대한 설정을 하였다면 zip_safe설정도 해주어야 합니다.
    zip_safe=False,
    # PyPI에 등록될 메타 데이터
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description=file('README.md'),
    long_description_content_type='text/markdown',
)
