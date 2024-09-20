# REsQue 백엔드

REsQue(Requirements Management Tool) 프로젝트의 백엔드 레포지토리입니다.

## 목차

- [기술 스택](#기술-스택)
- [시작하기](#시작하기)
  - [필요 조건](#필요-조건)
  - [설치](#설치)
- [개발](#개발)
  - [환경 설정](#환경-설정)
  - [실행](#실행)
  - [테스트](#테스트)
- [Poetry 사용법](#poetry-사용법)
  - [의존성 관리](#의존성-관리)
  - [스크립트 실행](#스크립트-실행)
- [기여하기](#기여하기)
- [라이선스](#라이선스)

## 기술 스택

- Python 3.11.9
- FastAPI
- Poetry (의존성 관리)
- pytest (테스팅)

## 시작하기

### 필요 조건

- Python 3.11.9
- Poetry

### 설치

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/your-repo/resque-backend.git
   cd resque-backend
   ```

2. Poetry를 설치합니다 (아직 설치하지 않은 경우):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. 프로젝트 의존성을 설치합니다:
   ```bash
   poetry install
   ```

## 개발

### 환경 설정

Poetry 가상 환경을 활성화합니다:

```bash
poetry shell
```

### 실행

개발 서버를 실행합니다:

```bash
poetry run start
```

### 테스트

테스트를 실행합니다:

```bash
poetry run test
```

## Poetry 사용법

### 의존성 관리

- 새 패키지 추가:
  ```bash
  poetry add <package-name>
  ```

- 개발 의존성 추가:
  ```bash
  poetry add --dev <package-name>
  ```

- 의존성 업데이트:
  ```bash
  poetry update
  ```

### 스크립트 실행

`pyproject.toml`에 정의된 스크립트를 실행합니다:

```bash
poetry run <script-name>
```

예: `poetry run start`, `poetry run test`

## 기여하기

프로젝트에 기여하고 싶으시다면 CONTRIBUTING.md 문서를 참조해 주세요.

## 라이선스

이 프로젝트는 [라이선스 이름] 하에 있습니다. 자세한 내용은 LICENSE 파일을 참조하세요.