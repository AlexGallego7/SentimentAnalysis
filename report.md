# ML Project Report
**Project** | **Details**
--------|--------
Date    | Thu, 04 Nov 2021 20:33:31 +0100 
Path    | `/home/alex/Desktop/SentimentAnalysis`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `https://github.com/AlexGallego7/SentimentAnalysis.git`
Git: Commit     | `844600b7f6ea6382460dcf39f6b92100b3a44ca4`
Git: Branch     | `master`
Git: Dirty Workspace?  | Yes
Number of Python files | 5
Lines of Python code   | 183

---

## Config

**Note** — The following rules were disabled in `mllint`'s configuration:
- `version-control/data/dvc-has-remote`
- `version-control/data/dvc-has-files`
- `code-quality/bandit/no-issues`

## Reports

### Version Control (`version-control`) — **71.4**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
 | _Total_ | | | 
❌ | **71.4**% | | Version Control | `version-control`

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **59.7**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 18.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
❌ | 0.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
 | _Total_ | | | 
❌ | **59.7**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Pylint
- Mypy
- Black
- isort
- Bandit


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **15** issues with your project:

- `src/collect.py:16,16` - _(W1514)_ Using open without explicitly specifying an encoding
- `src/collect.py:19,8` - _(E1101)_ Instance of 'API' has no 'search' member
- `src/model.py:38,28` - _(W0108)_ Lambda may not be necessary
- `src/model.py:61,24` - _(W0108)_ Lambda may not be necessary
- `src/model.py:149,23` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/model.py:150,21` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/predict.py:41,24` - _(W0108)_ Lambda may not be necessary
- `src/predict.py:55,24` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `tests/test_negative.py:1,0` - _(C0114)_ Missing module docstring
- `tests/test_negative.py:5,0` - _(C0413)_ Import "from predict import predict" should be placed at the top of the module
- `tests/test_negative.py:8,0` - _(C0116)_ Missing function or method docstring
- `tests/test_positive.py:1,0` - _(C0114)_ Missing module docstring
- `tests/test_positive.py:5,0` - _(C0413)_ Import "from predict import predict" should be placed at the top of the module
- `tests/test_positive.py:8,0` - _(C0116)_ Missing function or method docstring
- `tests/test_positive.py:1,0` - _(R0801)_ Similar lines in 2 files
	```python
	==model:[52:62]
	==predict:[32:43]
	        if stem:
	            tokens.append(stemmer.stem(token))
	        else:
	            tokens.append(token)
	
	    return " ".join(tokens)
	
	
	df.text = df.text.apply(lambda x: preprocess_text(x))
	
	
	```


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **28** issues with your project:

- `src/predict.py:6,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/predict.py:7,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/predict.py:8,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/predict.py:9,1` - Error: Skipping analyzing "matplotlib": found module but no type hints or library stubs  [import]
- `src/predict.py:10,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/predict.py:58,27` - Error: Implicit generic "Any". Use "typing.Dict" and specify generic parameters  [type-arg]
- `src/model.py:5,1` - Error: Skipping analyzing "nltk": found module but no type hints or library stubs  [import]
- `src/model.py:6,1` - Error: Skipping analyzing "numpy": found module but no type hints or library stubs  [import]
- `src/model.py:7,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/model.py:8,1` - Error: Skipping analyzing "gensim.models": found module but no type hints or library stubs  [import]
- `src/model.py:9,1` - Error: Skipping analyzing "keras.callbacks": found module but no type hints or library stubs  [import]
- `src/model.py:10,1` - Error: Skipping analyzing "keras.layers": found module but no type hints or library stubs  [import]
- `src/model.py:11,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/model.py:12,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/model.py:13,1` - Error: Skipping analyzing "keras.preprocessing.text": found module but no type hints or library stubs  [import]
- `src/model.py:14,1` - Error: Skipping analyzing "nltk.corpus": found module but no type hints or library stubs  [import]
- `src/model.py:15,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/model.py:16,1` - Error: Skipping analyzing "sklearn.model_selection": found module but no type hints or library stubs  [import]
- `src/model.py:17,1` - Error: Skipping analyzing "sklearn.preprocessing": found module but no type hints or library stubs  [import]
- `src/model.py:134,27` - Error: Implicit generic "Any". Use "typing.Dict" and specify generic parameters  [type-arg]
- `src/collect.py:5,1` - Error: Skipping analyzing "tweepy": found module but no type hints or library stubs  [import]
- `src/collect.py:5,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/collect.py:16,6` - Error: "_writer" has no attribute "__enter__"  [attr-defined]
- `src/collect.py:16,6` - Error: "_writer" has no attribute "__exit__"  [attr-defined]
- `tests/test_positive.py:8,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_positive.py:8,1` - Note: Use "-> None" if function does not return a value
- `tests/test_negative.py:8,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_negative.py:8,1` - Note: Use "-> None" if function does not return a value


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

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

This equates to **40%** of Python files in your project being tests, which meets the target ratio of **20%**

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

