import setuptools

setuptools.setup(
    name="functions",
    version="0.1",
    author="mishka251",
    author_email="mishkabelka251@gmail.com",
    description="Test Calculator functions",
    packages=setuptools.find_namespace_packages(),
    py_modules=['add', 'div', 'get_function', 'mul', 'sub'],
)
