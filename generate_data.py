import data_generation_utils as dgu

dgu.generate_instances(filename="instances.txt",
                      n_instances=1,
                      n_tasks=7,
                      n_processors=2,
                      release_range=(0,6),
                      length_range=(1,12),
                      weight_range=(1,12),
                      correlation="none")

import math
def procs_for_k(k):
    return int(k/25 + math.log2(k))


for k in range(4, 26):
    dgu.generate_instances(filename=f"data/{k}_tasks.txt",
                      n_instances=100,
                      n_tasks=k,
                      n_processors=procs_for_k(k),
                      release_range=(0,k//2),
                      length_range=(1,k),
                      weight_range=(1,k),
                      correlation="none")
