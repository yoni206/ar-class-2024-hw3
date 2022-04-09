# HW 2
The tasks for this HW are found in hw2.pdf.

## Details about Question 1
### How to Implement?
The solver should be implemented in `uf_solver.py`. 
The main functionality should be implemented in `flat_cube_uf_solver`.
Of course, using helper functions for modularity is recommended.
`flat_cube_uf_solver` is currently a dummy implementation: 
it only verifies that the formula is indeed a flat cube, and then returns True.

Notice that `uf_solver.py` imports utility functions from `utils.py`. 
Feel free to use the them.

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
* The directory benchmarks includes several smt2 files as examples.
* Your implementation will be tested on a super-set of these benchmarks.
* You are free to implement everything within `uf_solver.py` or use other files and import them. In the latter case, make sure to include them in your submission. The test script will always call `uf_solver.py`.
It is highly recommended to compare your results to an off-the-shelf SAT solver, such as `z3` in order to check that your results are correct. When testing your implementation, I plan to compare your results to `z3's` results. `z3` can be found here: https://github.com/Z3Prover/z3
