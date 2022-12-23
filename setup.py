from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        packages=find_packages(),
        package_data={"pontypg": ["py.typed"]},
        name="pontypg",
        version="0.2.2",
        license="BSD",
        url="https://github.com/csira/pontypg",
        description="Basic async postgres utils. Extends ponty.",
        install_requires=[
            "asyncpg==0.21.0",
            "ponty>=0.2.2",
            "typing-extensions==4.2.0",
        ],
        python_requires=">=3.8",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Framework :: AsyncIO",
            "Intended Audience :: Developers",
            "License :: Freely Distributable",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Typing :: Typed",
        ]
    )
