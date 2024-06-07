import os
import subprocess

# 기존 requirements.txt 파일이 존재하는지 확인하고 있다면 삭제합니다.
if os.path.exists("requirements.txt"):
    os.remove("requirements.txt")

# 새로운 requirements.txt 파일을 생성합니다.
subprocess.run(["pip", "freeze"], stdout=open("requirements.txt", "w"))
