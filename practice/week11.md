# Week 11 실습

## 오늘 한 것
- PyInstaller 설치 및 빌드
- resource_path() 함수 추가
- --add-data 옵션으로 에셋 포함
- .exe 실행 확인
- 
## resource_path() 를 써야 하는 이유
단순 상대 경로가 아닌 실행 환경을 감추는 역 

## 빌드 명령어
pyinstaller --onefile game.py
pyinstaller --onefile --windowed game.py
pyinstaller --onefile --windowed --add-data "assets;assets" --name MyGame oyt_game.py

## AI 활용 내역
resource_path()을 쓰기엔 복잡한 구조로 되어 있어 resource_path()를 사용할 수 있게 코드를 수정해 달라고 하였다
