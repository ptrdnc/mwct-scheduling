import data_generation_utils as dgu

dgu.generate_instances(filename="instances.txt",
                      n_instances=1,
                      n_tasks=7,
                      n_processors=2,
                      release_range=(0,6),
                      length_range=(1,12),
                      weight_range=(1,12),
                      correlation="none")
