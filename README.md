<p align="center">
<img src="https://avatars.githubusercontent.com/u/157958039?s=200&v=4" width=15%><br>
Solution to increase users' disaster literacy<br>
<strong>SafeLine</strong>
</p>

# SafeLine-Server

> This `README` is written in English, with a [Korean version(한국어)](#safeline-server-한국어-해설) below.

This repository contains the backend server code for the SafeLine project. This document contains a brief description of the project and instructions for running it.

## 📖 Overview

> Many people are not prepared for disasters. Current disaster warning systems and responses have limitations.

**SafeLine** is a solution aimed at improving users' disaster literacy.

- It generates instructions considering the user's location and situation (characteristics of the place, age, disabilities, etc.) and guides them to shelters.
- It creates intuitive images to accurately convey instructions even to users who find it difficult to understand text.
- It utilizes generative AI to respond to nex and complex disasters (such as climate change).
- By providing essay quizzes and feedback, it allows users to interact with the system and learn response methods.

## ⚙️ How to Run  

> 1. Before running, make sure the following requirements are met:
> `Python 3.11` (or versions 3.8 and above)
> 2. Additionally, smooth execution of the project requires setting up BigQuery table configurations and inserting data. This is not documented here due to data permission issues.
> 3. The content after step 3 of these instructions can only be executed after contacting our team and having a certain level of environment set up.

1. Clone this repository.

```bash
git clone https://github.com/SafeLine-KU/SafeLine-Server.git
```

2. This project uses `fastapi`, `uvicorn`,`google-cloud-storage`, `google-cloud-bigquery`, `google-generativeai`, `python-dotenv`, `openai`. Install the libraries with the following command:

```bash
pip install -r requirements.txt
```

3. Setting up some environment variables is necessary for running this project. Create a `.env` file in the `/app` directory and write the environment variables.

```bash
#External_API_KEYs
GOOGLE_GEMINI_KEY={Gemini API Key}
GOOGLE_MAPS_KEY={Google Maps Platform Key}
OPENAI_KEY={OpenAI Service Key}

#Bigquery Configs
GCP_SERVICE_ACCOUNT={File path for GCP Service account json file}
GCP_BIGQUERY_DATASET_ID={ID for BigQuery dataset}
GCP_BUCKET_NAME={Bucket name for Cloud Storage}
```

4. Navigate to `app/` (the folder where main.py is located) and run the uvicorn server.

```bash
cd app/
uvicorn main:app --reload
```

## 💻 Products/Platforms Used

- `Flutter`
- `Google Maps`
- `Google Cloud Platform`
  - `Cloud Run`
  - `Cloud Storage`
  - `BigQuery`
- Generative AI
  - `Gemini`(Pro 1.0 model)
  - `DALL·E 3`
- `FastAPI`

## ⚖️ License Notice

This project is licensed under the `MIT` License.
```text
MIT License

Copyright (c) 2024 SafeLine-KU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Additionally, as a sign of respect for the libraries used, their licenses are listed below.

| Package | License |
|:---|:---:|
|`Python Client for Google Cloud Storage API`|Apache License 2.0|
|`python-dotenv`|BSD 3-Clause|
|`uvicorn`|BSD 3-Clause|
|`FastAPI`|MIT|
|`openai`|MIT|

---

# SafeLine-Server 한국어 해설

이 레포지토리는 SafeLine 프로젝트의 백엔드 서버 코드입니다.  
본 문서는 프로젝트에 대한 간단한 설명과 실행에 관한 내용을 담고 있습니다.  

## 📖 개요  

> 많은 이는 재난 속에서 원활히 대응하지 못한다. 지금의 재난 경고 시스템과 대응법에 한계가 있다.  

**SafeLine**은 사용자의 재난 문해력을 향상시키기 위한 솔루션입니다.  

- 사용자의 위치와 상황(장소의 특성, 나이, 장애 등)을 고려해 행동요령을 생성하고, 대피소와 함께 안내합니다.
- 직관적인 이미지를 생성하여, 글을 이해하기 어려운 사용자에게도 정확하게 행동요령을 전달합니다.  
- 생성형 AI를 활용해, 신종,복합재난(기후변화 등)까지 대응합니다.
- 주관식 방식의 퀴즈와 피드백을 제공함으로써 사용자가 시스템과 상호작용하며, 대응법을 익힐 수 있도록 합니다.

## ⚙ 실행방법

> 1. 실행 전, 아래 요구사항이 만족되는지 확인해주세요:
> `Python 3.11` (또는 3.8 이상의 버전)
> 2. 또한, 프로젝트의 원활한 실행을 위해서는 `BigQuery` 테이블 설정 및 데이터 삽입이 필요합니다. 데이터 권한의 문제로 이는 여기에 작성되지 않았습니다.  
> 3. 본 실행지침의 3번 이후의 내용은 저희 팀에게 연락하여, 일정 수준의 환경이 구축된 이후에서만 동작이 가능합니다.

1. 본 레포지토리를 clone해주세요.

```bash
git clone https://github.com/SafeLine-KU/SafeLine-Server.git
```

2. 본 프로젝트는 `fastapi`, `uvicorn`,`google-cloud-storage`, `google-cloud-bigquery`, `google-generativeai`, `python-dotenv`, `openai`를 사용합니다. 아래 명령어를 통해 라이브러리를 설치해주세요:

```bash
pip install -r requirements.txt
```

3. 이 프로젝트의 실행을 위해서는 몇 가지 환경변수의 설정이 필요합니다. `/app` 폴더에 `.env`를 생성해 환경변수를 작성해주세요.

```bash
#External_API_KEYs
GOOGLE_GEMINI_KEY={Gemini API Key}
GOOGLE_MAPS_KEY={Google Maps Platform Key}
OPENAI_KEY={OpenAI Service Key}

#Bigquery Configs
GCP_SERVICE_ACCOUNT={File path for GCP Service account json file}
GCP_BIGQUERY_DATASET_ID={ID for BigQuery dataset}
GCP_BUCKET_NAME={Bucket name for Cloud Storage}
```

4. `app/`(main.py가 위치한 폴더)으로 이동한 뒤, `uvicorn` 서버를 동작하세요.

```bash
cd app/
uvicorn main:app --reload
```

## 💻 사용한 제품/플랫폼  
- `Flutter`
- `Google Maps`
- `Google Cloud Platform`
  - `Cloud Run`
  - `Cloud Storage`
  - `BigQuery`
- Generative AI
  - `Gemini`(Pro 1.0 model)
  - `DALL·E 3`
- `FastAPI`

## ⚖️ 라이센스 고지

본 프로젝트는 `MIT`라이센스에 따라 자유롭게 이용할 수 있습니다.  
```text
MIT License

Copyright (c) 2024 SafeLine-KU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

또한 사용한 라이브러리에 대한 존중의 의미로 아래에 라이선스를 명시합니다.

| 이름 | 라이센스 |
|:---|:---:|
|`Python Client for Google Cloud Storage API`|Apache License 2.0|
|`python-dotenv`|BSD 3-Clause|
|`uvicorn`|BSD 3-Clause|
|`FastAPI`|MIT|
|`openai`|MIT|
