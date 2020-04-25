import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qt_nmr",
    version="0.1.0",
    author="Geoffrey M. Sametz",
    author_email="sametz@udel.edu",
    description="Simulation of First-Order, Second-Order, and Dynamic NMR spectra.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/sametz/qt_nmr",
    packages=setuptools.find_packages(
        where='src',
        exclude=['tests']
    ),
    package_dir={"": "src"},
    include_package_data=True,  # so MANIFEST is recognized
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords='NMR simulation spectra spectrum',
    python_requires='>=3.6',
    install_requires=['nmrsim==0.4.0rc1',
                      'pyside2',
                      'pyqtgraph==0.11.0rc0'
                      ],
    extras_require={
        'dev': [
            'flake8',
            'pytest',
            'pyfakefs',
            'pytest-qt',
            # for testing packaging:
            'beeware',
        ]
    }
)
