from distutils.core import setup

setup(
    name="fastapi-storages",
    version="0.3.1",
    description="fastapi-storages",
    author="",
    author_email="",
    packages=[
        "fastapi_storages",
    ],
    install_requires=[
        "boto3~=1.25",
        "peewee>=3",
        "pillow~=9.4",
        "sqlalchemy>=1.4",
    ],
)
