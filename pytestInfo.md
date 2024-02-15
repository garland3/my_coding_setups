# pytest
* pytest lets you run unit and integration test in python

## SETUP
* install pytest
* make a folder to put your test suite `test`
* in the folder make some python files that start with `test` like `test_database.py`
* run with `pytest test` to test all the test in the folder
* to run a specific tile, just do `pytest test/test_database.py`

  ## actual test
  * each function in the test file that starts with `test` is a test that will be run
  * like, `test_user_creation` is a test
  * `my_cool_function` is NOT a test

# more info
when calling pytest do
* `-s ` to all stdout, which is quite helpful if you have some print statement
* `-v` or `-vv` to be verbose, also helpful
* `-k test_user_creation` to test the specific test

