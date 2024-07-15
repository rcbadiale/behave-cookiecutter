# Behave cookie cutter

A simple project with basic setup for creating tests with
[Behave](https://behave.readthedocs.io/en/stable/) library.

## Table of contents
[TOC]

## Executing tests

- To execute all the test scenarios, use the following command:
```shell
behave features/
```

- To execute only one feature, use the following command:
```shell
behave features/example.feature
```

- To execute only the scenario that starts at line 13, use the following command:
```shell
behave features/example.feature:13
```

## Useful things already setup

- A global logger is available and set up in the context as `context.logger`.
- A profiler is set up for registering scenario execution times.
- Linter, gitignore, and isort are set up for common cases of behave projects.
