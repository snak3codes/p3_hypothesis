# Python 3.8.0 Hypothesis Guide

This repository should help you to get started with Hypothesis. You can find code examples that contributors and I wrote (in **personal**) and code examples taken from various documentations (in **Docs**).



## Installing Hypothesis

```
pip install hypothesis
```



## Quickstart

Use **hypo_template.py** as a template file to implement your test cases.
**PRO TIP:** Turn the template into a VSCode snippet: Command Palette > Preferences: Configure User Snippets > Python
and add this entry in the json file.

```json
  "Hypothesis Template": {
    "prefix": "hypo",
    "body": [
      "from hypothesis import given",
      "from hypothesis.strategies import integers\n",
      "from ${1:filename} import ${2:functions}\n\n",
      "@given(${3:strategy})",
      "def ${4:test}(${5:args}):",
      "\tassert ${0}\n\n",
      "if __name__ == '__main__':",
      "\timport pytest",
      "\tpytest.main(['${TM_FILENAME}'])"
    ]
  }
```

\* For PyCharm snippets check out: https://www.jetbrains.com/help/pycharm/tutorial-creating-and-applying-live-templates-code-snippets.html



## How to run

On PyCharm simply run **PyTest** in the *test file*, if using command line, navigate to directory and run

```
pytest your_test_file.py
```

For simplicity I have defined a few *aliases* in my shell as shortcuts to my common workflow commands.

```bash
alias pt="pytest"
alias ptd="pytest --doctest-modules -v"
alias pths="pytest --hypothesis-show-statistics"
```



## How To Contribute

Contribute into the **personal/contributions** folder. Thank you! 



## Issues

Use the **issues** section to report bugs, request specific test case examples, requesting to add one of your test cases, and more.



## Thank You!