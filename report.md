# ML Project Report
**Project** | **Details**
--------|--------
Date    | Sat, 15 Jan 2022 21:08:27 +0100 
Path    | `/home/alex/Desktop/SentimentAnalysis`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `https://github.com/AlexGallego7/SentimentAnalysis.git`
Git: Commit     | `05c996f16c959551482973446035b9a9c5d057c4`
Git: Branch     | `master`
Git: Dirty Workspace?  | Yes
Number of Python files | 4
Lines of Python code   | 218

---

## Reports

### Version Control (`version-control`) — **92.9**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
 | _Total_ | | | 
✅ | **100.0**% | | Version Control | `version-control`

#### Details — Project should not have any large files in its Git history — ❌

Your project's Git history contains the following files that are larger than 10 MB:
- **74 MB** - commit `094d0fbf21a6610f5eaf7185dbce35a6121e79c7` - `data/model.w2v`
- **23 MB** - commit `3fe6791f05f7761c5866f8ba46b7d72903ab8efb` - `data/features/tokenizer.pkl`

These files may not necessarily be in your project right now, but they are still stored inside your project's Git history.
Thus, whenever your project is downloaded (with `git clone`), all these unnecessary files have to be downloaded as well.

See [this StackOverflow answer](https://stackoverflow.com/a/46615578/8059181) to learn how to remove these files from your project's Git history.

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **73.9**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
✅ | 100.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
 | _Total_ | | | 
✅  | **73.9**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Pylint
- Mypy
- Black
- isort
- Bandit


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **2** issues with your project:

- `src/predict.py:41,24` - _(W0108)_ Lambda may not be necessary
- `tests/test_positive.py:1,0` - _(R0801)_ Similar lines in 2 files
	```python
	==model:65
	==predict:32
	            if stem:
	                tokens.append(STEMMER.stem(token))
	            else:
	                tokens.append(token)
	
	    return " ".join(tokens)
	
	
	```


#### Details — Mypy reports no issues with this project — ✅

Congratulations, Mypy is happy with your project!

#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **10** issues with your project:

- `src/model.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/predict.py:3` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/predict.py:55` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/predict.py:56` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `tests/test_negative.py:13` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)
- `tests/test_negative.py:14` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)
- `tests/test_negative.py:15` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)
- `tests/test_positive.py:13` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)
- `tests/test_positive.py:14` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)
- `tests/test_positive.py:15` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html)


### Testing (`testing`) — **75.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project has automated tests | `testing/has-tests`
✅ | 100.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **75.0**% | | Testing | `testing`

#### Details — Project has automated tests — ✅

Great! Your project contains **2** test files, which meets the minimum of **1** test files required.

This equates to **50%** of Python files in your project being tests, which meets the target ratio of **20%**

#### Details — Project passes all of its automated tests — ✅

Congratulations, all **2** tests in your project passed!

#### Details — Project provides a test coverage report — ❌

A test coverage report was provided, namely `coverage.xml`, but this file could not be found or opened (error: `did not find a file matching coverage.xml in folder /home/alex/Desktop/SentimentAnalysis: file does not exist`).

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to fix the path to your project's test report. Remember that this path must be relative to the root of your project directory.

### Continuous Integration (`ci`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
❌ | **0.0**% | | Continuous Integration | `ci`

