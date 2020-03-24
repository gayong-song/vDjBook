### Django를 활용한 쉽고 빠른 웹 개발 "파이썬 웹프로그래밍" 실전편 예제 따라해보기
---
## 실행하는 법
```
(vDjBook) $ python3 manage.py runserver 0.0.0.0:8000 #linux에서는 0:8000도 가능
```
### 뼈대 잡기
> 프로젝트 생성
```
./Scripts/activate
(vDjBook) $ django-admin startproject mysite
```
> 기본 테이블 생성
```
(vDjBook) $ python3 manage.py migrate
```
> 슈퍼 유저 생성
```
(vDjBook) $ python3 manage.py createsuperuser
```
> 애플리케이션 생성
```
(vDjBook) $ python3 manage.py startapp [app_name]
```
앱 등록 하는 법은 settings.py에 INSTALLED_APPS에 'bookmark.apps.BookmarkConfig'와 같이 추가해주면 된다.
> 데이터 베이스에 반영하는 법 - models.py에 테이블을 정의하거나 수정한 후
```
(vDjBook) $ python3 manage.py makemigrations [app_name(optional)]
(vDjBook) $ python3 manage.py migrate
```
### 코딩 순서
1. 뼈대 만들기
  1.1. startproject
  1.2. settings.py
  1.3. migrate
  1.4. createsuperuser
  1.5. startapp
  1.6. settings.py
2. 모델 코딩하기
  2.1. models.py
  2.2. admin.py
  2.3. makemigrations -> migrate ( 변경 사항을 DB에 반영 )
3. URLconf 코딩하기
  3.1. urls.py
4. 뷰 코딩하기
  4.1. views.py
5. 템플릿 코딩하기
  4.2. templates 디렉터리
