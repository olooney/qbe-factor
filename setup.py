from setuptools import setup


def grab_version():
    with open("qbe_factor/version.py") as file:
        line = file.readline().rstrip()
        version = line.split(" = ")[1].replace('"', "")
    return version


setup(
    name="qbe_factor",
    version=grab_version(),
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
    scripts=["scripts/run_server.py"],
)
