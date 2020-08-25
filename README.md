<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
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


![kibana](https://user-images.githubusercontent.com/49490703/90717826-75d05180-e2eb-11ea-9874-1e57caba3b26.gif)

You can use it for free :point_right: [Demo](https://search-tremo-fenkliifb7hs34jlbmtzcz7jbq.ap-northeast-2.es.amazonaws.com/_plugin/kibana/app/kibana#/dashboard/df78d420-d6f9-11ea-a5ed-b305e0c58646?_g=(filters%3A!()%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-2h%2Cto%3Anow)))



Dashboard that can analyze/monitor the trends of entertainment characteristics occurring in complex situations


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
```sh
Python >= 3
```


### Installation 

* Install package via pip [https://pypi.org/project/tremo/](https://pypi.org/project/tremo/) in your local or virtual envrionment
```sh
pip install tremo
```


* Homebrew
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* ElasticSearch, Kibana
```sh
brew install elasticsearch, kibana
```


<!-- USAGE EXAMPLES -->
## Usage

* Run with/without ElasticSearch
```sh
from tremo.run import run


result = run(elastic_search=False)
```
The run function collects trends, news data, and keywords from the top 10.
The data type of result is list of 10 lengths of the dictionary.

* Example of result data
```sh
from tremo.run import run


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

* Repeat with/without ElasticSearch
```sh
from tremo.run import repeat


repeat(elastic_search="localhost:9200", interval_second=600)
```
The repeat function executes the run function by thread timer every interval_second

elastic_search and interval_second default value is False and 600

If you set elastic_search to `{{YOUR_PATH_TO_ES}}`, You can use the dashboard visualized in Kibana for the data stored in ElasticSearch.


* import kibana dash board

You can import our JSON file from Kibana UI under Management > Saved Objects > Import. 

```
1. Click Import.
2. Navigate to the JSON file that represents the objects to import.
3. Import ./kibana_import/{version}.ndjson file
4. Indicate whether to overwrite objects already in Kibana.
5. Click Import.
```

If you import json file, you can use dash board like [this](#about-the-project)


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
