# 마약범죄 형량 및 판례 조회 서비스

## 개요
마약이 우리 사회 전체로 급속히 확산하고 있는 양상이다.
최근 정부에서는 '마약과의 전쟁'을 선포할만큼 이 문제를 심각히 여기고 있다.
경찰청에 따르면 2018년 12,613명이었던 마약사범은 2021년에는 16,153명으로 크게 증가한 것으로 나타났다.
하지만 이렇게 급증하는 마약범죄에도 불구하고, 사람들은 유명인 또는 재벌 '마약 스캔들'에만 주목할 뿐 그 이상 관심을 두지 않는듯 하다.
많은 언론에서도 마약혐의에 대해서만 집중적으로 보도할 뿐, 후에 어떤 처벌을 받았는지 또는 형량이 적절했는지에 대해서는 다루고 있지 않다.
본 서비스는 이와 같은 사회적 분위기 속에서 출발했다.
본 서비스의 목적은 먀약범죄에 관한 형량 및 판례 데이터 제공에 있다.
마약범죄 형량 및 판례 조회 서비스는 과거 마약에 관한 판례 데이터를 수집하고, 수집한 데이터를 바탕으로 사용자의 입력에 따른 판례 데이터의 마약별 형종, 형량 분포와 판례 원문을 제공한다.
따라서, 본 서비스를 통해 특정 마약 사범이 어떤 처벌을 받게 될지 또는 형량이 적절했는지를 과거 사례들로부터 확인할 수 있다.
 
## 개발 환경
 * Python 3.8.15
 * Django 4.0.3
 
## 주요 내용
 ### 1. 데이터 수집
 * 데이터는 국내 최다 판례 조회 사이트인 빅케이스(<https://bigcase.ai>)에서 수집을 진행했다.
 * Selenium 패키지를 사용해 판례 원문을 크롤링하여 데이터 수집을 진행했다.
 * 사이트로부터 7,259개의 판례 원문 데이터를 수집했다.
 * 사이트에서 총 10가지의 마약의 이름을 키워드로 검색하여 판례 원문 데이터를 수집했다.
 * 형량이 명시된 1심 판례에 한해 데이터 수집을 진행했다.
 
 ### 2. 데이터 전처리
 * 서비스 주요 기능을 구현하기 위해 판례 원문으로부터 다음 5가지 속성을 정의했다.
 1) 사건번호: 판례 고유 번호
 2) 취급마약: 판례가 어떤 마약에 관한 판례인지를 나타냄.
 3) 형량: 선고된 형량
 4) 형종: 선고된 형량의 종류
 5) 형량범위: 형량의 범위
 6) 범죄사실: 선고에 적용된 범죄사실을 나타냄.
 * 데이터 전처리 결과, 수집한 7,259개의 데이터 중 3,162개의 데이터를 활용할 수 있는 형태로 처리했다.
 * 데이터 전처리에 관한 자세한 내용은 preprocessing.ipynb 파일을 참고
 <img width="1280" alt="데이터 전처리 예시1" src="https://user-images.githubusercontent.com/121072239/217197711-607ed1d1-82fa-42a2-bd02-c8973f056a46.png">
 <img width="1280" alt="데이터 전처리 예시2" src="https://user-images.githubusercontent.com/121072239/217197767-4f31219e-9ca5-4a9f-ba41-fedafc4d66ac.png">
 <img width="1280" alt="데이터 테이블" src="https://user-images.githubusercontent.com/121072239/212743274-4c37842c-075f-47cd-ac03-1db76795afc0.png">

 ### 3. 서비스 구현
 * 본 서비스는 Django 프레임워크를 사용해 웹 서비스로 구현했다.
 * 사용자의 입력값을 다음 페이지로 전송하기 위해 HTML form을 사용했다.
 * 여러 페이지에서 사용하기 위해 사용자의 입력값에 만족하는 데이터를 세션에 저장했다.
 * 서비스 구현을 위해 구성한 페이지는 다음과 같다.
 1) 홈페이지
 2) 마약별 데이터 분포 페이지
 3) 검색 페이지
 4) 형종별 데이터 분포 페이지
 5) 형량별 데이터 분포 페이지
 6) 판례 원문 페이지

 ### 4. 서비스 주요 기능
 * 사이트 내 존재하는 판례 데이터의 마약별 분포를 조회한다.
 * 사용자가 선택한 마약과 관련된 판례 데이터를 검색한다.
 * 검색한 판례 데이터의 형종별, 형량별 분포를 조회한다.
 * 사용자의 입력값에 따라 분포에 해당하는 판례 원문을 조회한다.

## 구동 방법
 * 본 서비스는 정식으로 배포되지 않았기 때문에, 로컬 서버에서만 구동이 가능하다.
 * 구동 방법은 다음과 같다.
 1) 업로드된 전체 파일을 다운받는다.
 2) 개발환경과 동일한 가상환경을 셋팅한다.
 3) 가상환경을 활성화한다.
 4) 터미널의 경로를 myweb 폴더로 변경한다.
 5) 터미널에 python manage.py runserver 명령을 입력한다.
 6) 웹 브라우저를 통해 출력된 로컬 서버로 접속한다.

## 결과
* 구현한 서비스의 모습은 다음과 같다.
<img width="1280" alt="홈페이지" src="https://user-images.githubusercontent.com/121072239/218307831-9ab6c751-df05-4277-8ee1-a01532089873.png">
<img width="1280" alt="마약별 데이터 분포 페이지" src="https://user-images.githubusercontent.com/121072239/218307820-6ae9b646-d430-4745-8f85-2d66412ab4f5.png">
<img width="1280" alt="검색 페이지" src="https://user-images.githubusercontent.com/121072239/218307814-03135bb2-20f6-4d3c-9961-02050da1592e.png">
<img width="1280" alt="형종별 데이터 분포 페이지" src="https://user-images.githubusercontent.com/121072239/218307828-81d02f2f-0a57-4105-808d-4326d747d52a.png">
<img width="1280" alt="형량별 데이터 분포 페이지" src="https://user-images.githubusercontent.com/121072239/218307826-98bfa0a0-9867-4987-bf46-942bd2ab501b.png">
<img width="1280" alt="판례 원문 페이지" src="https://user-images.githubusercontent.com/121072239/218307821-dfa160c6-7b8d-4e7e-89eb-b9c90bf40ddd.png">
