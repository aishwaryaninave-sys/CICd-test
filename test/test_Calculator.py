from app.calculator import add,substractor
'''
  from app ->folder
  calcu;ator -> filename
  import add,substract (function)
  '''
def test_add():
  assert add(2,3) == 5

def test_substract():
  assert substract (5,3) == 2
