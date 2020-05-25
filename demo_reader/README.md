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

* :file_folder: **project_name**
  * :page_facing_up: `README.rst`
  * :file_folder: **docs**
  * :file_folder: **src**
    * :file_folder: **package_name**
      * :page_facing_up: `__init__.py`
      * :page_facing_up: `some_source.py`
      * :file_folder: **subpackage1**
        * :page_facing_up: `__init__.py`
  * :file_folder: **tests**
    * :page_facing_up: `test_code.py`
  * :page_facing_up: `setup.py`

## Package Distributions

### Source Distributions

### Built Distributions

### Uploading Packages to a Package Server

* Use Twine to upload.
  * `python -m pip install --user --upgrade twine`
  * `twine upload dist/package_name-stuff.whl`
