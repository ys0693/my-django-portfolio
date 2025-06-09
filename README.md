# 김영식 자기소개 웹 애플리케이션

이 프로젝트는 Django 프레임워크를 기반으로 한 개인 포트폴리오 웹사이트입니다.  
자기소개, 관심 분야, 개발 실적, 취미 등을 포함하고 있으며, Django의 기본 구조와 HTML 템플릿을 활용해 구성되어 있습니다.

---

#사전 설치 조건 (다른 컴퓨터 실행 가능 기준)

아래 항목들이 설치되어 있어야 이 프로젝트가 실행됩니다.

#1. Python 3.8 이상  
- 다운로드: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
- 설치 시 **"Add Python to PATH" 체크** 필수  
- 설치 확인:
  ```bash
  python --version
  ```

### 2. pip (Python 패키지 관리자)  
- 보통 Python 설치 시 자동 포함  
- 확인:
  ```bash
  pip --version
  ```

### 3. Git (코드 복제용)  
- 다운로드: [https://git-scm.com/downloads](https://git-scm.com/downloads)  
- 확인:
  ```bash
  git --version
  ```

📌 위 3가지가 모두 설치되어 있어야 아래 실행 방법이 정상 작동합니다.

---

## ✅ 프로젝트 실행 방법 (다른 사람이 처음부터 따라 할 수 있게)

### ▶ 1단계: GitHub 저장소 복제

```bash
git clone https://github.com/ys0693/my-django-portfolio.git
cd my-django-portfolio
```

> Git이 없다면 저장소 페이지에서 "Code > Download ZIP" 후 압축 해제

---

### ▶ 2단계: 가상환경 생성 및 활성화

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

> 가상환경이 활성화되면 `(venv)` 같은 표시가 나옴

---

### ▶ 3단계: 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

> 설치 과정에서 오류 없이 진행돼야 실행이 가능합니다.

---

### ▶ 4단계: 서버 실행

```bash
python manage.py runserver
```

> 정상 실행되면 아래와 같은 메시지가 출력됩니다:
```
Starting development server at http://127.0.0.1:8000/
```

---

# ▶ 5단계: 브라우저에서 접속

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
입력하면 자기소개 웹페이지가 나타납니다.

---

##실행 확인 테스트 안내 

- Python 3.10, pip, Git이 설치된 윈도우 환경에서 테스트
- 가상환경 생성 및 `pip install -r requirements.txt` 정상 작동
- `python manage.py runserver`로 웹 서버 실행 성공
- 브라우저에서 포트 `8000` 접속 정상 확인

---

## 📁 프로젝트 폴더 구조

```
my-django-portfolio/
├── intro/             # 자기소개 앱
├── mysite/            # Django 프로젝트 설정
├── static/            # 정적 파일(css, 이미지 등)
├── templates/         # HTML 템플릿
├── db.sqlite3         # 개발용 DB
├── requirements.txt   # 패키지 목록
├── manage.py          # Django 실행 파일
```

---

## 주요 기능

- 자기소개 페이지 구성
- 관심 분야 및 개발 실적 표시
- 취미: 수영, 러닝 / 목표: 바이크 타고 알프스 투어
- Django 템플릿과 URL 라우팅 적용

---

## GitHub Repository

[https://github.com/ys0693/my-django-portfolio](https://github.com/ys0693/my-django-portfolio)
