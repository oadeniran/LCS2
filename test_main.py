def func(x):
  return x + 1

def func2(x):
  return x + 2

def func3(x):
  return x + 3

def test_func():
  assert func(3) == 4

def test_func2():
  assert func2(3) == 9
  
def test_func3():
  assert func3(3) == 6
