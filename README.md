<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
![demo_image](https://user-images.githubusercontent.com/49490703/89879114-6a02d200-dbfd-11ea-97f2-8361ca5c8e3b.png)

Dashboard that can analyze/monitor the trends of entertainment characteristics occurring in complex situations


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
```sh
Python >= 3.8
```


### Installation 

* Homebrew
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* ElasticSearch
```sh
brew install elasticsearch
```

* Kibana
```sh
brew install kibana
```

* Install packages via pip [https://pypi.org/project/monitering/](https://pypi.org/project/monitering/)
```sh
pip install monitoring
```




<!-- USAGE EXAMPLES -->
## Usage

* Run with/without ElasticSearch
```python
from monitoring.run import run
result = run(elastic_search=True)
```
The run function collects trends, news data, and keywords from the top 10.
The data type of result is list of 10 lengths of the dictionary.

* Repeat with/without ElasticSearch
```python
from monitoring.run import repeat
repeat(elastic_search=True, interval_second=600)
```
The repeat function executes the run function by thread timer every interval_second

elastic_search and interval_second default value is True and 600

If you set elastic_search to True, You can use the dashboard visualized in Kibana for the data stored in ElasticSearch.

* Example of result data
```python
from monitoring.run import run
result = run(elastic_search=False)
print(result[0])
```

```json
{
    "ranking": 1,
    "word": "걸캅스",
    "category": [
      "영화"
    ],
    "related_search_word": [
      "영화 걸캅스",
      "걸캅스 주우재",
      "라미란 이성경",
      "이성경",
      "이성경 라미란",
      "위하준",
      "라미란",
      "걸캅스 이레",
      "걸캅스 하정우",
      "정직한 후보"
    ],
    "related_keyword": [
      "사건",
      "라미란",
      "스타트렉",
      "콤비",
      "다크니스",
      "기록",
      "이성",
      "수사",
      "성범죄",
      "검사"
    ],
    "news_title": "[집에서 볼만한 영화추천] 걸캅스, 검사외전, 스타트렉 다크니스&비욘드",
    "timestamp": "2020-08-17T03:35:28.942994"
}
```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/contribution`)
3. Commit your Changes (`git commit -m 'Add some contribution'`)
4. Push to the Branch (`git push origin feature/contribution`)
5. Open a Pull Request 



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jihoon Kang -  jihoon522@sk.com

Project Link: [https://github.com/thisishoon/trend-monitoring](https://github.com/thisishoon/trend-monitoring)
Linkedin: [![LinkedIn][linkedin-shield]][linkedin-url]


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/thisishoon/trend-monitoring/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/thisishoon/trend-monitoring.svg?style=flat-square
[forks-url]: https://github.com/thisishoon/trend-monitoring/network/members
[stars-shield]: https://img.shields.io/github/stars/thisishoon/trend-monitoring.svg?style=flat-square
[stars-url]: https://github.com/thisishoon/trend-monitoring/stargazers
[issues-shield]: https://img.shields.io/github/issues/thisishoon/trend-monitoring.svg?style=flat-square
[issues-url]: https://github.com/thisishoon/trend-monitoring/issues
[license-shield]: https://img.shields.io/github/license/thisishoon/trend-monitoring.svg?style=flat-square
[license-url]: https://github.com/thisishoon/trend-monitoring/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/thisisjihoon/