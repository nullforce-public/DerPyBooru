# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [1.0.0]
### Added
- Now uses the API introduced with Philomena

### Removed
- Older derpibooru API calls

## [0.10.0]
### Added
- Image class now has an `image_json` property to get to the underlying JSON
  field (`image` still returns `representations["full"]` but will change to
  the JSON value in a future version).

### Fixed
- Updated `Search` methods to use `q=` params:
  - `faves` uses `my:faves`
  - `upvotes` uses `my:upvotes`
  - `uploads` uses `my:uploads`
  - `watched` uses `my:watched`


## [0.9.3]
### Fixed
- Encoding error in setup.py when running Python 2.7

### Other
- Added badges to README and other document changes
- Adopt tox for package install testing


## [0.9.2]
### Fixed
- Use shared VERSION file.


## [0.9.1]
### Fixed
- Add missing dependency on `deprecation` package.
- Removed unknown `__version__`.


## [0.9.0]
### Added
- Add support for the `updated_at`, `first_seen_at`, and `tag_count` sort options.

### Deprecated
- Mark `Search` methods that appear to be no longer supported as deprecated:
  - `faves`
  - `uploads`
  - `upvotes`
  - `watched`


## [0.8.0]
### Added
- Add support for the `wilson` and `width` sort options.


## [0.7.3] and [Earlier Versions]

See [joshua-stone/DerPyBooru](https://github.com/joshua-stone/DerPyBooru).


[Unreleased]: https://github.com/nullforce-public/DerPyBooru/compare/0.10.0...HEAD
[0.10.0]: https://github.com/nullforce-public/DerPyBooru/compare/0.9.3...0.10.0
[0.9.3]: https://github.com/nullforce-public/DerPyBooru/compare/0.9.2...0.9.3
[0.9.2]: https://github.com/nullforce-public/DerPyBooru/compare/0.9.1...0.9.2
[0.9.1]: https://github.com/nullforce-public/DerPyBooru/compare/0.9.0...0.9.1
[0.9.0]: https://github.com/nullforce-public/DerPyBooru/compare/0.8.0...0.9.0
[0.8.0]: https://github.com/nullforce-public/DerPyBooru/compare/0.7.3...0.8.0

[0.7.3]: https://github.com/joshua-stone/DerPyBooru/releases/tag/0.7.3
[Earlier Versions]: https://github.com/joshua-stone/DerPyBooru/releases
