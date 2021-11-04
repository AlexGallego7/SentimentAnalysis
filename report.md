# ML Project Report
**Project** | **Details**
--------|--------
Date    | Thu, 04 Nov 2021 20:05:55 +0100 
Path    | `/home/alex/Desktop/SentimentAnalysis`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `https://github.com/AlexGallego7/SentimentAnalysis.git`
Git: Commit     | `e4c2965f2a5595af3e8df4011d635c9acf75e60b`
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

### Code Quality (`code-quality`) — **56.7**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 40.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 0.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
 | _Total_ | | | 
❌ | **56.7**% | | Code Quality | `code-quality`

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


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **28** issues with your project:

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

## Errors

1 error(s) occurred while analysing your project:
- ❌ **Code Quality** - 1 error occurred:
	* Pylint failed to run: error parsing Pylint output 'Traceback (most recent call last):
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/bin/pylint", line 8, in <module>
    sys.exit(run_pylint())
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/__init__.py", line 21, in run_pylint
    from pylint.lint import Run as PylintRun
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/lint/__init__.py", line 76, in <module>
    from pylint.lint.parallel import check_parallel
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/lint/parallel.py", line 8, in <module>
    from pylint import reporters
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/reporters/__init__.py", line 26, in <module>
    from pylint import utils
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/utils/__init__.py", line 46, in <module>
    from pylint.utils.ast_walker import ASTWalker
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/pylint/utils/ast_walker.py", line 7, in <module>
    from astroid import nodes
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/astroid/__init__.py", line 51, in <module>
    from astroid.nodes import node_classes, scoped_nodes
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/astroid/nodes/__init__.py", line 27, in <module>
    from astroid.nodes.node_classes import (  # pylint: disable=redefined-builtin (Ellipsis)
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/astroid/nodes/node_classes.py", line 47, in <module>
    from astroid import decorators, mixins, util
  File "/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/astroid/decorators.py", line 36, in <module>
    from typing_extensions import ParamSpec
ImportError: cannot import name 'ParamSpec' from 'typing_extensions' (/home/alex/.local/share/virtualenvs/SentimentAnalysis-CHIzAvV2/lib/python3.8/site-packages/typing_extensions.py)
': invalid character 'T' looking for beginning of value


