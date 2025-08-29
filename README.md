# Image to PDF CLI Tool

모든 이미지 파일 하나의 pdf로 합치기

## 사용법
- Python 가상환경 생성
- 프로젝트 내 폴더 생성하기
- 코드
```bash
# Python 가상환경 생성
python -m venv venv
source venv/bin/activate 
# Windows: source venv/Scripts/activate

# 의존성 설치
pip install -r requirements.txt

# 기본 파일명으로 저장 (images.pdf)
python convert_to_pdf.py images/

# 파일명을 직접 지정
python convert_to_pdf.py images/ -o result.pdf 
```