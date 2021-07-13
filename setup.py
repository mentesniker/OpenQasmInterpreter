from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='oqi',
    version='1.0.5',
    description='Open Qasm interpreter.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Luis Mtz.',
    author_email='mentesniker@gmail.com',
    keywords=['OpenQasm', 'QuantumComputing', 'QuantumSimulator'],
    url='https://github.com/mentesniker/OpenQasmInterpreter',
    download_url='https://pypi.org/project/oqi/'
)
install_requires = [
    'qiskit'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires,    
    entry_points = {
        'console_scripts': ['oqi=oqi.oqi:main'],
    })