**Libraries**

To get the package dependencies for this project, use:
```powershell
python -m pip install -r requirements.txt

python -m pip list
```

**Build**

This project using pyproject.toml and setup.cfg for build. To build the project, run the following commands:
- delete the existing distribution files
- build the project
- upload to pypi using twine

```powershell
del .\dist\*.*
python -m build
python -m twine upload dist/* --verbose
```

For a manual build (old type), use:

```powershell
python setup.py sdist
python setup.py bdist_wheel
```

To use the built package in another project, use:

```powershell
python -m pip install dist/smart_tools-0.1-py3-none-any.whl
python -m pip uninstall smart_tools
```

To create console files without running a build, use pyinstaller:

```powershell
pyinstaller smart_tools/dissector/main.py --onefile --name dissector
pyinstaller smart_tools/morpher/main.py --onefile --name morpher
```