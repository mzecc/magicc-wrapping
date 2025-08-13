Generally very helpful resources:

- https://fortran-lang.org/packages/programming/
- https://fortran-lang.org/learn/best_practices/floating_point/

Docs:

- https://forddocs.readthedocs.io/en/stable/user_guide/writing_documentation.html
- great example: https://toml-f.github.io/toml-f/module/tomlf_structure.html
    - try and get docs building like this and deployed on RtD asap

Meson specifics:

- https://mesonbuild.com/meson-python/tutorials/introduction.html
    - try and package and release asap to test distribution on different OS
    - example CI workflow: https://fortran-lang.discourse.group/t/python-wheels-on-github-actions-using-fortran-f2py-numpy-meson-and-cibuildwheel/5609/6

Run the script:

`make clean; uv run -Cbuild-dir=build --no-editable --reinstall-package example python scratch.py`
