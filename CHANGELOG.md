# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-22

### Fixed
- **Critical**: Fixed `__setitem__` key inversion bug where keys were mapped incorrectly in the internal structure
- **Critical**: Fixed infinite recursion bug in `popitem()` method
- **Critical**: Fixed `get()` method raising KeyError instead of returning default value
- **Critical**: Fixed inheritance from typing.Dict to collections.abc.MutableMapping
- **Critical**: Fixed `update()` method not properly mapping keys through internal structure
- Fixed `setdefault()` method to correctly handle new keys and default values

### Added
- Comprehensive test suite with 52 tests covering all functionality and edge cases
- Missing dict methods: `copy()`, `fromkeys()`, `__or__()` (union operator), `__ior__()` (in-place union)
- GitHub Actions CI/CD pipeline testing on Python 3.8-3.12 across multiple OS platforms
- Type checking configuration with mypy
- Development tooling configuration (pytest, ruff, black)
- `.gitignore` file for Python projects
- Comprehensive README with badges, installation instructions, and development guide

### Changed
- Modernized packaging from `setup.py` to `pyproject.toml`
- Updated Python version requirement from 3.6+ to 3.8+
- Simplified counter mechanism by replacing custom `I` class with `itertools.count()`
- Improved code documentation and type hints
- Updated version to 0.1.0 (from 0.0.2)

### Improved
- Clearer internal structure documentation with inline comments
- Better error messages and exception handling
- 98% code coverage with comprehensive tests

## [0.0.2] - Previous Release
- Initial functionality for mutable key dictionary support

