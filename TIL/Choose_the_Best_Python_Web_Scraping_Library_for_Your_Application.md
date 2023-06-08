# Choose the Best Python Web Scraping Library for Your Application [Link](https://towardsdatascience.com/choose-the-best-python-web-scraping-library-for-your-application-91a68bc81c4f)
<ol>
<li>Scrapy : 가장 인기 많은 파이썬 웹 스크래핑 라이브러리 중 하나이다. 오픈소스 프레임워크이며 완전한 도구이다. 다른 도구들에 비해 CPU와 memory 효율적이다. 큰 규모의 웹 스크래핑 혹은 다중 테스트를 자동화할 때 가장 유용하다. 하지만, 단순한 스크래핑에는 추천하지 않는다. 불필요하게 복잡하다.</li><br>
<li>Request : 가장 정직한 HTTP 라이브러리이다. HTTP 서버에 request를 하여 HTML 혹은 JSON의 형태로 응답받는다. API가 있는 경우에 이상적인 선택이다. 스크래핑하려는 웹페이지가 자바스크립트 기반일 때 사용하는 것을 피하여라. 정확한 정보를 parsing하지 못할 수 있다.</li><br>
<li>Urllib : HTTP 혹은 FTP 프로토콜로부터 정보를 열거나 parsing하는 라이브러리이다. requests보다 약간 복잡하지만, 더 나은 통제를 원할 때 추천한다.</li><br>
<li>Beatiful soup : XML과 HTML 파일로부터 정보를 추출하는 데 사용하는 라이브러리이다. parser 라이브러리이며, 그것은 HTML로부터 데이터를 얻는 것을 돕는다. 만약 방금 웹 스크래핑 혹은 크롤링을 시작했다면, beautiful soup이 가장 좋은 선택이다. 구조화되지 않은 문서를 스크래핑하는 경우에도 훌륭하다. 큰 규모의 프로젝트를 하는 경우에는 현명한 옵션이 아니다. 유연하지 못하고 사이즈를 키우기에 불편하다.</li><br>
<li>Selenium : 오픈소스 웹 기반 도구이다. Selenium은 웹 드라이버로 웹페이지를 열고 버튼을 클릭하고 결과를 얻는 데에 사용할 수 있다. 초보자에게 친숙한 도구이며, 사람의 행동을 흉내내는 코드를 가능하게 한다. 웹 스크래핑이 처음이라면 확장가능하고 유연한, 강력한 도구이다. 몇 개의 페이지를 스크래핑하는 데 좋은 선택이긴 하나, 당신이 필요한 정보는 자바스크립트 내에 있다.</li>