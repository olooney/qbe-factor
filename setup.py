from setuptools import setup

setup(
    name="qbe_factor",
    version="0.0.1",
    author="Oran Looney",
    author_email="olooney@gmail.com",
    description="Example FastAPI app for QBE",
    packages=["qbe_factor"],
    package_data={
        "qbe_factor": [
            "data/*.json"
        ],
    },
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
    ],
    extras_require={
        'dev': [
            "pytest",
            "black",
        ],
    },
    python_requires=">=3.11",
)
