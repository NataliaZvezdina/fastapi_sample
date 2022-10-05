from setuptools import setup
import app

setup(
    name="app",
    version=app.__version__,
    author="Natalia Z.",
    author_email="natalia.z@gmail.com",
    description="Simple fast api application",
    install_requires=[
        'fastapi==0.85.0',
        'uvicorn==0.18.3',
        'SQLAlchemy==1.4.41',
        'pytest==7.1.3',
        'requests==2.28.1'
    ],
    scripts=['app/main.py']
)
