from setuptools import setup

setup(
    name='anew_scorer',
    packages=['anew_scorer'],
    entry_points={
        "console_scripts": ['anew_scorer = anew_scorer:main']
    },
    version='0.2',
    description="Lexical scorer built from the ANEW scoring system.",
    author="dark0bserver",
    url="https://github.com/dark0bserver/anew_scorer",
    test_suite="tests",
    include_package_data=True,
    package_data={'anew_scorer': ["anew/*"]},
)
