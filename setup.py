from setuptools import setup

setup(
    name="fast_api_sample",
    version="0.0.1",
    author="Natalia Z.",
    author_email="natalia.z@gmail.com",
    description="Simple fast api application",
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests=2.26.0'
    ],
    scripts=[]
)
