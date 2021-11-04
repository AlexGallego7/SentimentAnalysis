# ML Project Report
**Project** | **Details**
--------|--------
Date    | Thu, 04 Nov 2021 19:22:44 +0100 
Path    | `/home/alex/Desktop/SentimentAnalysis`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `https://github.com/AlexGallego7/SentimentAnalysis.git`
Git: Commit     | `50a3dd0c83c9200a85e4302c4580af5e2741f8ca`
Git: Branch     | `master`
Git: Dirty Workspace?  | Yes
Number of Python files | 3
Lines of Python code   | 169

---

## Reports

### Version Control (`version-control`) — **28.6**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
❌ | 0.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
❌ | 0.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
❌ | 0.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
❌ | 0.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
❌ | 0.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
 | _Total_ | | | 
❌ | **28.6**% | | Version Control | `version-control`

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **50.9**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 40.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 11.2% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
❌ | 0.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 55.6% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **50.9**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ❌

Linters detected:

- isort
- Pylint


However, these linters were **missing** from your project:

- Mypy
- Black
- Bandit


We recommend that you start using these linters in your project to help you measure and maintain the quality of your code.

This rule will be satisfied, iff for each of these linters:
- **Either** there is a configuration file for this linter in the project
- **Or** the linter is a dependency of the project

Specifically, we recommend adding each linter to the development dependencies of your dependency manager,
e.g. using `poetry add --dev mypy` or `pipenv install --dev mypy`


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **15** issues with your project:

- `src/collect.py:16,16` - _(W1514)_ Using open without explicitly specifying an encoding
- `src/collect.py:19,8` - _(E1101)_ Instance of 'API' has no 'search' member
- `src/model.py:44,15` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:44,26` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:44,36` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:39,28` - _(W0108)_ Lambda may not be necessary
- `src/model.py:62,24` - _(W0108)_ Lambda may not be necessary
- `src/model.py:150,23` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/model.py:151,21` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/predict.py:25,15` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:25,26` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:25,36` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:42,24` - _(W0108)_ Lambda may not be necessary
- `src/predict.py:56,24` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/predict.py:1,0` - _(R0801)_ Similar lines in 2 files
	```python
	==model:[53:63]
	==predict:[33:44]
	            if stem:
	                tokens.append(stemmer.stem(token))
	            else:
	                tokens.append(token)
	
	    return " ".join(tokens)
	
	
	df.text = df.text.apply(lambda x: preprocess_text(x))
	
	```


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **24** issues with your project:

- `src/predict.py:7,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/predict.py:8,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/predict.py:9,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/predict.py:10,1` - Error: Skipping analyzing "matplotlib": found module but no type hints or library stubs  [import]
- `src/predict.py:11,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/predict.py` - 59: error: Missing type parameters for generic type "typing.Dict"  [type-arg]
- `src/model.py:6,1` - Error: Skipping analyzing "nltk": found module but no type hints or library stubs  [import]
- `src/model.py:7,1` - Error: Skipping analyzing "numpy": found module but no type hints or library stubs  [import]
- `src/model.py:8,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/model.py:9,1` - Error: Skipping analyzing "gensim.models": found module but no type hints or library stubs  [import]
- `src/model.py:10,1` - Error: Skipping analyzing "keras.callbacks": found module but no type hints or library stubs  [import]
- `src/model.py:11,1` - Error: Skipping analyzing "keras.layers": found module but no type hints or library stubs  [import]
- `src/model.py:12,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/model.py:13,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/model.py:14,1` - Error: Skipping analyzing "keras.preprocessing.text": found module but no type hints or library stubs  [import]
- `src/model.py:15,1` - Error: Skipping analyzing "nltk.corpus": found module but no type hints or library stubs  [import]
- `src/model.py:16,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/model.py:17,1` - Error: Skipping analyzing "sklearn.model_selection": found module but no type hints or library stubs  [import]
- `src/model.py:18,1` - Error: Skipping analyzing "sklearn.preprocessing": found module but no type hints or library stubs  [import]
- `src/model.py` - 135: error: Missing type parameters for generic type "typing.Dict"  [type-arg]
- `src/collect.py:5,1` - Error: Skipping analyzing "tweepy": found module but no type hints or library stubs  [import]
- `src/collect.py:5,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/collect.py:16,6` - Error: "_writer" has no attribute "__enter__"  [attr-defined]
- `src/collect.py:16,6` - Error: "_writer" has no attribute "__exit__"  [attr-defined]


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **3** issues with your project:

- `src/model.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/predict.py:3` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/predict.py:56` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)


### Testing (`testing`) — **25.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **25.0**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There are **0** test files in your project, but `mllint` was expecting at least **1**.

#### Details — Project passes all of its automated tests — ❌

A test report was provided, namely `tests-report.xml`, but this file could not be found.

Please update the `testing.report` setting in your project's `mllint` configuration to fix the path to your project's test report. Remember that this path must be relative to the root of your project directory.

#### Details — Project provides a test coverage report — ❌

A test coverage report was provided, namely `coverage.xml`, but this file could not be found or opened (error: `did not find a file matching coverage.xml in folder /home/alex/Desktop/SentimentAnalysis: file does not exist`).

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to fix the path to your project's test report. Remember that this path must be relative to the root of your project directory.

#### Details — Tests should be placed in the tests folder — ✅

While no tests were detected in your project, it's good that your project already has a `tests` folder!

### Continuous Integration (`ci`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
❌ | **0.0**% | | Continuous Integration | `ci`

