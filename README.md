# mwct-scheduling
Projekat za predmet racunarska inteligencija

MINIMUM WEIGHTED COMPLETION TIME SCHEDULING


INSTANCE: Set T of tasks, number m of identical processors, for each task $t\in T$ a release time $r(t)\in Z^+$, a length $l(t)\in Z^+$, and a weight $w(t)\in Z^+$.

SOLUTION: An m-processor schedule for T that obeys the resource constraints and the release times, i.e., a function $f : T \rightarrow N \times
[1..m]$ such that, for all $u \geq 0$ and for each processor i, if S(u,i) is the set of tasks t for which $f(t)_{1} \leq u <
f(t)_{1}+l(t)$ and $f(t)_{2}=i$, then $\vert S(u,i)\vert = 1$ and for each task t, $f(t)_{1} \geq r(t)$.

MEASURE: The weighted sum of completion times, i.e. $\sum_{t\in T} w(t)(f(t)_1+l(t))$
