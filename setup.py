
from setuptools import setup

setup(
    name="oakwilt",
    version=0.1.0,
    packages=["backend"],
    include_package_data=True,
    install_requires=[
        "Flask == 3.0.3",
        "Flask-Cors == 5.0.0",
        "Pillow == 11.0.0",
        "Werkzeug == 3.0.4",
        "click== 8.1.7",
        "itsdangerous == 2.2.0",
        "Typing",
        "Pandas == 2.2.3",
        "piexif == 1.1.3",
        "tensorflow == 2.17.0",
        "opencv-python == 4.10.0.84",
    ],
)
