"""Smoke test — verifica que el entorno Python está correctamente configurado."""
import sys


def test_python_version():
    assert sys.version_info >= (3, 12), f"Se requiere Python 3.12+, encontrado: {sys.version}"


def test_imports_basicos():
    import os
    import pathlib
    assert os.path and pathlib.Path


def test_import_davidsan():
    import davidsan

    assert davidsan.__version__ == "0.1.0"
