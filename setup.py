from setuptools import setup

setup(
    name="qbe_factor",
    version="0.0.2",
    author="Oran Looney",
    author_email="olooney@gmail.com",
    description="Example FastAPI app for QBE",
    python_requires=">=3.11",
    packages=["qbe_factor"],
    package_data={
        "qbe_factor": ["data/*.json"],
    },
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
        ],
    },
    scripts=[
        'scripts/run_server.py'
    ]
)
