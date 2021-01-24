# demo_reader

This folder contains the results of the **Core Python: Organizing Larger Programs** course.

* :file_folder: **compressed** - The compressed sub-package

The `__init__.py` file is optional in Python 3.3+ *(required for earlier versions)*, but explicit is better than implicit.

* **Absolute** vs **Relative** imports
* **Namespace** packages may **not** have `__init__.py` files and cannot have any package level executed code.
* **Executable Directories** - Add `__main__.py` to a directory and call any other modules.
* **Executable Zip Files** - The `.zip` file takes the place of a directory.
* **Executable Packages** - 

## Recommended Project Layout

* 📂 **project_name**
  * 📄 `README.rst`
  * 📂 **docs**
  * 📂 **src**
    * 📂 **package_name**
      * 📄 `__init__.py`
      * 📄 `some_source.py`
      * 📂 **subpackage1**
        * 📄 `__init__.py`
  * 📂 **tests**
    * 📄 `test_code.py`
  * 📄 `setup.py`

## Package Distributions

### Source Distributions

### Built Distributions

### Uploading Packages to a Package Server

* Use Twine to upload.
  * `python -m pip install --user --upgrade twine`
  * `twine upload dist/package_name-stuff.whl`
