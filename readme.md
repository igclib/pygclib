## [![logo](https://raw.githubusercontent.com/igclib/assets/master/img/banner/pygclib_banner.svg?sanitize=true)](https://teobouvard.github.io/)

---

## Important

## `pygclib`, formerly `igclib`, is under a heavy transition phase. Expect things to be broken.

The developement is currently focused on [`igclib`](https://github.com/igclib/igclib), the C++ port of `pygclib`. Once `igclib` is stable, Python bindings will be introduced for `pygclib` and legacy code will be deleted. For the moment, use at your own risk.

---

`pygclib` is a Python package and a command line tool designed for the analysis of paragliding flights and competitions. Its main purpose is to serve as backend to [Task Creator](https://github.com/julien66/meteor-task-creator).

## Get started

```shell
sudo apt-get install libspatialindex-dev
git clone https://github.com/igclib/pygclib.git
cd pygclib
make install
```

For a quick guide on how to use this library, take a look at the [documentation](https://igclib.readthedocs.io/en/latest/).

## Interesting links

[Solving the task optimization problem using Quasi-Newton methods](https://teobouvard.github.io/2019/10/20/task_optimization.html)

## Requirements

- Python 3.5 or higher
- libspatialindex-dev
