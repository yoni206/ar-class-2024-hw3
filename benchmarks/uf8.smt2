(set-logic QF_UF)
(declare-sort S 0)
(declare-fun f (S S S) S)
(declare-fun x1 () S)
(declare-fun x2 () S)
(declare-fun x3 () S)

(assert (= x1 (f x2 x2 x1)))
(assert (= x2 (f x1 x1 x2)))
(assert (distinct x3 x1))
(check-sat)