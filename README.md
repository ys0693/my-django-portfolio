# 김영식 자기소개 웹 애플리케이션

이 프로젝트는 Django 프레임워크를 기반으로 한 개인 포트폴리오 웹사이트입니다.  
자기소개, 관심 분야, 개발 실적, 취미 등 다양한 정보를 담고 있으며, Django의 기본 구조와 HTML 템플릿을 활용해 구성되어 있습니다.

---

##실행 방법

#1. 저장소 클론

```bash
git clone https://github.com/ys0693/my-django-portfolio.git
cd my-django-portfolio
```

#2. 가상환경 생성 및 활성화

```bash
python -m venv venv
```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

#4. 서버 실행

```bash
python manage.py runserver
```

브라우저에서 아래 주소를 입력하여 접속합니다:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

#프로젝트 구조

```
my-django-portfolio/
├── intro/             # 자기소개 앱
├── mysite/            # Django 프로젝트 설정
├── static/            # 정적 파일(css, 이미지 등)
├── templates/         # HTML 템플릿
├── db.sqlite3         # 기본 DB (개발용)
├── requirements.txt   # 필수 패키지 목록
├── manage.py          # Django 실행 스크립트
```

---

#주요 기능

- 자기소개 (이름, 관심 분야, 목표)
- 개발 실적 소개
- 취미: 수영, 러닝 / 목표: 바이크 타고 알프스 투어
- 기본 HTML + Django Template 시스템 적용

---

#개발 환경

- Python 3.x
- Django 4.x
- 개발 OS: Windows 10

---

#GitHub Repository

[https://github.com/ys0693/my-django-portfolio](https://github.com/ys0693/my-django-portfolio)
