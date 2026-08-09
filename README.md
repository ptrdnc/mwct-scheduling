# mwct-scheduling

### INSTANCE

Set $T$ of tasks, number $m$ of identical processors, and for each task
$t \in T$:

- release time $r(t) \in \mathbb{Z}^+$
- length $l(t) \in \mathbb{Z}^+$
- weight $w(t) \in \mathbb{Z}^+$

### SOLUTION

An $m$-processor schedule for $T$ that obeys the resource constraints
and the release times.

Formally, a function

$$
f : T \rightarrow \mathbb{N} \times [1..m]
$$

such that, for all $u \geq 0$ and for each processor $i$, if $S(u,i)$ is
the set of tasks $t$ for which

$$
f(t)_1 \leq u < f(t)_1 + l(t)
\quad\text{and}\quad
f(t)_2 = i,
$$

then

$$
|S(u,i)| = 1
$$

and, for each task $t$,

$$
f(t)_1 \geq r(t).
$$

### MEASURE

The weighted sum of completion times:

$$
\sum_{t \in T} w(t)\left(f(t)_1 + l(t)\right)
$$
