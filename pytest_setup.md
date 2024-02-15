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

# fixture
* often you want common info sent to all test.
* This is called a fixture.
* Like setting up an object or database.
* to let the other function use the fixture, pass in the name of the function as an arg. 

```python
@pytest.fixture
def setup_db():
  # called to initially setup Db, passed into the other functions
  return make_db()

def test_make_user(setup_db):
  # NOTE: how I used the name of the fixture function
  db = setup_db # just to make my life easier, I'll just make an alias of db
  db.make_user("bob", "bob@bob.com")
  # test if it worked
  user = db.get_user("bob@bob.com")
  assert user, "User was none which is not expected"
  assert user.email == "bob@bob.com", "Got the wrong user, or the user was not saved properly"
  assert user.name == "bob", "The user's name is not right. Either saving the info or retrival failed"
  

```
