import random

def random_value(lo, hi):
    return random.randint(lo, hi)


def generate_instance(
    n_tasks,
    n_processors,
    release_range=(0, 100),
    length_range=(1, 20),
    weight_range=(1, 20),
    correlation="none"
):
    """
    Generate one MWCT scheduling instance.

    correlation:
        "none"          -> length and weight are independent
        "positive"      -> longer tasks tend to have larger weights
        "negative"      -> longer tasks tend to have smaller weights
    """

    tasks = []

    for i in range(n_tasks):

        release_time = random_value(*release_range)
        length = random_value(*length_range)

        if correlation == "none":
            weight = random_value(*weight_range)

        elif correlation == "positive":
            # Normalize length to [0, 1]
            x = (length - length_range[0]) / (
                length_range[1] - length_range[0]
            )

            # Add some randomness
            noise = random.uniform(-0.25, 0.25)

            normalized_weight = min(max(x + noise, 0), 1)

            weight = round(
                weight_range[0]
                + normalized_weight
                * (weight_range[1] - weight_range[0])
            )

        elif correlation == "negative":
            x = (length - length_range[0]) / (
                length_range[1] - length_range[0]
            )

            noise = random.uniform(-0.25, 0.25)

            normalized_weight = min(max(1 - x + noise, 0), 1)

            weight = round(
                weight_range[0]
                + normalized_weight
                * (weight_range[1] - weight_range[0])
            )

        else:
            raise ValueError(
                "correlation must be 'none', 'positive', or 'negative'"
            )

        tasks.append(
            (i, release_time, length, weight)
        )

    return n_processors, tasks


def generate_instances(
    filename,
    n_instances,
    n_tasks,
    n_processors,
    release_range=(0, 100),
    length_range=(1, 20),
    weight_range=(1, 20),
    correlation="none"
):
    with open(filename, "w") as file:

        for _ in range(n_instances):

            m, tasks = generate_instance(
                n_tasks=n_tasks,
                n_processors=n_processors,
                release_range=release_range,
                length_range=length_range,
                weight_range=weight_range,
                correlation=correlation
            )

            file.write(f"{m} {n_tasks}\n")

            for task_id, r, l, w in tasks:
                file.write(f"{task_id} {r} {l} {w}\n")

            file.write("\n")


def read_instances(filename):
    instances = []

    with open(filename, "r") as file:
        lines = file.readlines()

    i = 0

    while i < len(lines):

        if not lines[i].strip():
            i += 1
            continue

        print(lines[i])
        m, n = map(int, lines[i].split())
        i += 1

        tasks = []

        for _ in range(n):
            task_id, r, l, w = map(int, lines[i].split())
            i += 1

            tasks.append((task_id, r, l, w))

        instances.append({
            "n_processors": m,
            "tasks": tasks
        })

    return instances


generate_instances(
    filename="instances.txt",
    n_instances=1,
    n_tasks=10,
    n_processors=2,
    release_range=(0, 10),
    length_range=(1, 20),
    weight_range=(1, 20),
    correlation="none"
)

print(read_instances("instances.txt"))
