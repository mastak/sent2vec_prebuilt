import sys
import tokenize
from setuptools import setup
from distutils.extension import Extension

import numpy
from Cython.Build import cythonize


try:
    _detect_encoding = tokenize.detect_encoding
except AttributeError:
    pass
else:
    def detect_encoding(readline):
        try:
            return _detect_encoding(readline)
        except SyntaxError:
            return 'latin-1', []

    tokenize.detect_encoding = detect_encoding


long_description = """
## Unofficial prebuilt binary for Linux and MacOS
The repo that builds this project can be found here: 
[https://github.com/mastak/sent2vec_prebuilt](https://github.com/mastak/sent2vec_prebuilt)
"""


source_files = [
    'sent2vec/src/sent2vec.pyx',
    'sent2vec/src/fasttext.cc',
    'sent2vec/src/args.cc',
    'sent2vec/src/dictionary.cc',
    'sent2vec/src/matrix.cc',
    'sent2vec/src/shmem_matrix.cc',
    'sent2vec/src/qmatrix.cc',
    'sent2vec/src/model.cc',
    'sent2vec/src/real.cc',
    'sent2vec/src/utils.cc',
    'sent2vec/src/vector.cc',
    'sent2vec/src/real.cc',
    'sent2vec/src/productquantizer.cc',
]

compile_opts = ['-std=c++0x', '-Wno-cpp', '-pthread', '-Wno-sign-compare']


ext = [
    Extension(
        '*',
        source_files,
        extra_compile_args=compile_opts,
        language='c++',
        include_dirs=[numpy.get_include()],
    )
]


setup(
    name='sent2vec_prebuilt',
    ext_modules=cythonize(ext, language_level=str(sys.version_info[0])),
    version='0.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/epfml/sent2vec',
    author='Pagliardini, Matteo and Gupta, Prakhar and Jaggi, Martin',
    license='BSD',
    setup_requires=[
        'Cython',
        'numpy',
        'wheel',
    ],
    install_requires=['numpy'],
    scripts=['sent2vec/fasttext'],
    zip_safe=False,
    classifiers=[
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3.5',
     'Programming Language :: Python :: 3.6',
     'Programming Language :: Python :: 3.7'
    ],
)
