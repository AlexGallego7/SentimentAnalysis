# ML Project Report
**Project** | **Details**
--------|--------
Date    | Thu, 04 Nov 2021 18:23:10 +0100 
Path    | `/home/alex/Desktop/SentimentAnalysis`
Config  | `pyproject.toml`
Default | Yes
Number of Python files | 3
Lines of Python code   | 171

---

## Reports

### Version Control (`version-control`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Git | `version-control/code/git`
❌ | 0.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
❌ | 0.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
❌ | 0.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
❌ | 0.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
❌ | 0.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
 | _Total_ | | | 
❌ | **0.0**% | | Version Control | `version-control`

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **49.5**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 40.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 0.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
❌ | 0.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 56.1% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **49.5**% | | Code Quality | `code-quality`

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

Pylint reported **36** issues with your project:

- `src/collect.py:16,16` - _(W1514)_ Using open without explicitly specifying an encoding
- `src/collect.py:19,8` - _(E1101)_ Instance of 'API' has no 'search' member
- `src/model.py:50,15` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:50,26` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:50,36` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/model.py:13,0` - _(W0404)_ Reimport 'Dropout' (imported line 12)
- `src/model.py:39,0` - _(C0116)_ Missing function or method docstring
- `src/model.py:43,28` - _(W0108)_ Lambda may not be necessary
- `src/model.py:50,0` - _(C0103)_ Constant name "cleanse_re" doesn't conform to UPPER_CASE naming style
- `src/model.py:53,0` - _(C0116)_ Missing function or method docstring
- `src/model.py:66,24` - _(W0108)_ Lambda may not be necessary
- `src/model.py:129,0` - _(C0103)_ Constant name "history" doesn't conform to UPPER_CASE naming style
- `src/model.py:148,0` - _(C0116)_ Missing function or method docstring
- `src/model.py:157,0` - _(C0116)_ Missing function or method docstring
- `src/model.py:158,4` - _(W0621)_ Redefining name 'X_test' from outer scope (line 80)
- `src/model.py:159,4` - _(W0621)_ Redefining name 'score' from outer scope (line 140)
- `src/model.py:158,4` - _(C0103)_ Variable name "X_test" doesn't conform to snake_case naming style
- `src/model.py:171,23` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/model.py:172,21` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/model.py:4,0` - _(W0611)_ Unused Counter imported from collections
- `src/model.py:6,0` - _(W0611)_ Unused matplotlib.pyplot imported as plt
- `src/predict.py:28,15` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:28,26` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:28,36` - _(W1401)_ Anomalous backslash in string: '\S'. String constant might be missing an r prefix.
- `src/predict.py:1,0` - _(C0114)_ Missing module docstring
- `src/predict.py:14,24` - _(R1732)_ Consider using 'with' for resource-allocating operations
- `src/predict.py:28,0` - _(C0103)_ Constant name "cleanse_re" doesn't conform to UPPER_CASE naming style
- `src/predict.py:31,0` - _(C0116)_ Missing function or method docstring
- `src/predict.py:31,20` - _(W0621)_ Redefining name 'text' from outer scope (line 70)
- `src/predict.py:43,24` - _(W0108)_ Lambda may not be necessary
- `src/predict.py:49,0` - _(C0116)_ Missing function or method docstring
- `src/predict.py:58,0` - _(C0116)_ Missing function or method docstring
- `src/predict.py:58,12` - _(W0621)_ Redefining name 'text' from outer scope (line 70)
- `src/predict.py:59,4` - _(C0103)_ Variable name "X_text" doesn't conform to snake_case naming style
- `src/predict.py:3,0` - _(W0611)_ Unused pi imported from math
- `src/predict.py:1,0` - _(R0801)_ Similar lines in 2 files
	```python
	==model:[57:69]
	==predict:[34:48]
	            if stem:
	                tokens.append(stemmer.stem(token))
	            else:
	                tokens.append(token)
	
	    return " ".join(tokens)
	
	
	df.text = df.text.apply(lambda x: preprocess_text(x))
	
	## Split dataset into train and test
	
	```


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **39** issues with your project:

- `src/predict.py:5,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/predict.py:6,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/predict.py:7,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/predict.py:8,1` - Error: Skipping analyzing "matplotlib": found module but no type hints or library stubs  [import]
- `src/predict.py:9,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/predict.py:31,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/predict.py:43,35` - Error: Call to untyped function "preprocess_text" in typed context  [no-untyped-call]
- `src/predict.py:49,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/predict.py:58,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/predict.py:61,13` - Error: Call to untyped function "decode_prediction" in typed context  [no-untyped-call]
- `src/predict.py:71,11` - Error: Call to untyped function "predict" in typed context  [no-untyped-call]
- `src/model.py:6,1` - Error: Skipping analyzing "matplotlib.pyplot": found module but no type hints or library stubs  [import]
- `src/model.py:6,1` - Error: Skipping analyzing "matplotlib": found module but no type hints or library stubs  [import]
- `src/model.py:7,1` - Error: Skipping analyzing "nltk": found module but no type hints or library stubs  [import]
- `src/model.py:8,1` - Error: Skipping analyzing "numpy": found module but no type hints or library stubs  [import]
- `src/model.py:9,1` - Error: Skipping analyzing "pandas": found module but no type hints or library stubs  [import]
- `src/model.py:10,1` - Error: Skipping analyzing "gensim.models": found module but no type hints or library stubs  [import]
- `src/model.py:11,1` - Error: Skipping analyzing "keras.callbacks": found module but no type hints or library stubs  [import]
- `src/model.py:12,1` - Error: Skipping analyzing "keras.layers": found module but no type hints or library stubs  [import]
- `src/model.py:13,1` - Error: Skipping analyzing "keras.layers.core": found module but no type hints or library stubs  [import]
- `src/model.py:14,1` - Error: Skipping analyzing "keras.models": found module but no type hints or library stubs  [import]
- `src/model.py:15,1` - Error: Skipping analyzing "keras.preprocessing.sequence": found module but no type hints or library stubs  [import]
- `src/model.py:16,1` - Error: Skipping analyzing "keras.preprocessing.text": found module but no type hints or library stubs  [import]
- `src/model.py:17,1` - Error: Skipping analyzing "nltk.corpus": found module but no type hints or library stubs  [import]
- `src/model.py:18,1` - Error: Skipping analyzing "nltk.stem": found module but no type hints or library stubs  [import]
- `src/model.py:19,1` - Error: Skipping analyzing "sklearn.model_selection": found module but no type hints or library stubs  [import]
- `src/model.py:20,1` - Error: Skipping analyzing "sklearn.preprocessing": found module but no type hints or library stubs  [import]
- `src/model.py:39,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/model.py:43,39` - Error: Call to untyped function "decode_target" in typed context  [no-untyped-call]
- `src/model.py:53,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/model.py:66,35` - Error: Call to untyped function "preprocess_text" in typed context  [no-untyped-call]
- `src/model.py:148,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/model.py:157,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/model.py:160,13` - Error: Call to untyped function "decode_prediction" in typed context  [no-untyped-call]
- `src/model.py:166,11` - Error: Call to untyped function "decode_prediction" in typed context  [no-untyped-call]
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
- `src/predict.py:1` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/predict.py:14` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)


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

No test report was provided.

Please update the `testing.report` setting in your project's `mllint` configuration to specify the path to your project's test report.

When using `pytest` to run your project's tests, use the `--junitxml=<filename>` option to generate such a test report, e.g.:
```sh
pytest --junitxml=tests-report.xml
```


#### Details — Project provides a test coverage report — ❌

No test coverage report was provided.

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to specify the path to your project's test coverage report.

Generating a test coverage report with `pytest` can be done by adding and installing `pytest-cov` as a development dependency of your project. Then use the following command to run your tests and generate both a test report as well as a coverage report:
```sh
pytest --junitxml=tests-report.xml --cov=path_to_package_under_test --cov-report=xml
```


#### Details — Tests should be placed in the tests folder — ✅

While no tests were detected in your project, it's good that your project already has a `tests` folder!

### Continuous Integration (`ci`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
❌ | **0.0**% | | Continuous Integration | `ci`

