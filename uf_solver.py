# importing system module for reading files
import sys

# import utility functions
from utils import get_terms, is_flat_cube, get_function_symbols

# import classses for parsing smt2 files
from pysmt.smtlib.parser import SmtLibParser
from six.moves import cStringIO

# import pysmt functions for creating formulas and terms
from pysmt.shortcuts import Not, Equals, Function

# solver for flat cubes
# returns True if flat_cube is satisfiable. 
# Otherwise, returns False
def flat_cube_uf_solver(flat_cube):
  assert is_flat_cube(flat_cube)
  return True

# main function
def main():
  # read path from input
  path = sys.argv[1]
  with open(path, "r") as f:
    smtlib = f.read()
  
  # parse the smtlib file and get a formula
  parser = SmtLibParser()
  script = parser.get_script(cStringIO(smtlib))
  formula = script.get_last_formula()

  # we are assuming `formula` is a flat cube.
  # `cube` represents `formula` as a list of literals
  cube = formula.args()

  # check if sat or unsat and print result
  sat = flat_cube_uf_solver(cube)
  print("sat" if sat else "unsat")

if __name__ == "__main__":
    main()
