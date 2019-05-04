# Packaging

Before starting, read: [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

## Steps for Packaging

### Prepare the code:
- Run the tests
- On a branch:
  - Verify the CHANGELOG notes are correct
  - Update the version in:
    - derpibooru/VERSION
    - README.md
  - If this is a major, minor, or patch release:
    - `git tag <major>.<minor>.<patch>`

### Create a preliminary package:
- Clean up the `dist/` folder
- Create Source distribution: `python setup.py sdist`
- Create Universal wheel: `python setup.py bdist_wheel --universal`

### Test the package installation:
- Use a [temporary virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
- `mktmpenv`
- `pip install dist/<package>`
- Run the tests

### Merge changes into master
- Merge the branch back to `master` and push changes and tags
- Update the release notes for the tag in github

### Upload the package to PyPI
If you're manually uploading to PyPI do this; otherwise, let the CI/CD pipeline
do its job.

- [Optional]
  - Upload to the Test PyPI `twine upload --repository testpypi dist/*`
  - Inspect the package at http://test.pypi.org
- Upload to PyPI: `twine upload --repository pypi dist/*`

### Using the CI/CD Pipeline for Packaging
- Nothing more to do here

### Finally
- Update the release notes for the tag in github
