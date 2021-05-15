import setuptools


setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    # author="Alexander Juda",
    # author_email="alexanderjuda@gmail.com",
    packages=setuptools.find_packages(
        include=["{{cookiecutter.package_name}}", "{{cookiecutter.package_name}}.*"],
        where="src",
    ),
    package_dir={"": "src"},
    install_requires=[
        # Add prod deps here
    ],
    extras_require={
        "dev": [
            # Add optional dev deps here
            "pytest",
        ],
    },
)
