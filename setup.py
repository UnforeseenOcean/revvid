from setuptools import setup
from pathlib import Path
import platform

CURRENT_DIR = Path(__file__).parent

def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()

install_requires = [
    "moviepy==1.0.0",
    "praw==6.2.0",
    "click"
]

if platform.system() == 'Darwin':
    install_requires.append("pyttsx3==2.71")
else:
    install_requires.append("gTTS")


setup(
    name="revvid",
    version="0.1.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=['revvid']
    url="https://github.com/kyb3r/revvid",
)

