# HW 2
The tasks for this HW are found in hw2.pdf.

## Details about Question 1
### How to Implement?
The solver should be implemented in `uf_solver.py`. 
The main functionality should be implemented in `uf_solver`.
Of course, using helper functions for modularity is recommended.

Notice that `uf_solver.py` imports utility functions from `utils.py`. 
Feel free to use the them, as well as any other function from `utils.py`.
Functions from `pysmt` are also imported, feel free to use them as well as any other function from `pysmt`.

### The Expected Output
If the formula is sat, just print `sat` to the screen.
Otherwise, print `unsat`, following by a separating line `----`,
and then print the list of literals that were actually
used to find out that the formula is unsatisfiable -- each
literal in a separate line (the file `uf_solver.py`
already has code to do this printing).
For example, if the input formula is `x=y/\z=w/\f(x)!=f(y)`,
then depending on the derivation that you found,
it could be that you never relied on `z=w`. In that case,
print only the first and last literals.
If your derivation happened to use z=w (e.g. for a redundant TOP-LEVEL application), then it will also be included in the output.

You should aim that for at least some inputs, the output is
a strict subset of the input.


### How to Run?
This is how your implementation should be called:
```
python3 uf_solver.py <path-to-smt2>
```
where `<path-to-smt2>` is a path to an smt2 file.

For example,

```
python3 uf_solver.py benchmarks/uf1.smt2
```
The result should be `unsat`.

No other output is allowed, as the implementation will be tested using scripts.

Remarks:
* The directory `benchmarks` includes several smt2 files as examples.
* Your implementation will be tested on a super-set of these benchmarks.
* You are free to implement everything within `uf_solver.py` or use other files and import them. In the latter case, make sure to include them in your submission. The test script will always call `uf_solver.py`.
* It is highly recommended to compare your results to an off-the-shelf SMT solver, such as `z3`, in order to check that your results are correct. When testing your implementation, I plan to compare your results to `z3's` results. `z3` can be found here: https://github.com/Z3Prover/z3
