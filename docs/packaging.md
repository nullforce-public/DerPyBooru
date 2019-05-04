# Packaging

Before starting, read: [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

## Steps for Packaging

### Prepare the code
- Run the tests with `pytest`
- On a branch:
  - Verify the CHANGELOG notes are correct
  - Update the version in:
    - derpibooru/VERSION
    - README.md
  - If this is a major, minor, or patch release:
    - `git tag <major>.<minor>.<patch>`

### Test the package installation
- Run `tox` or `tox -e py37`
- Did it pass?

### Merge changes into master
- Merge the branch back to `master` and push changes and tags
- Update the release notes for the tag in github

### Create a release package
- Clean up the `dist/` folder
- Create Source distribution: `python setup.py sdist`
- Create Universal wheel: `python setup.py bdist_wheel --universal`

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
