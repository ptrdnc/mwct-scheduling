import data_generation_utils as dgu

import heapq
import copy

def modified_greedy(instance):
    objective = 0
    order = []
    schedule = []

    tasks = copy.deepcopy(instance.tasks)
    
    processors = [(0, i) for i in range(instance.n_processors)]
    heapq.heapify(processors)
    
    while tasks:
        current_time, processor_id = heapq.heappop(processors)

        def h(task):
            if (task.r <= current_time):
                return task.w / (current_time + task.l)
            else:
                return task.w / (task.r + task.l)
        
        task = max(tasks, key=h)
        
        if (task.r > current_time):
            current_time = task.r

        tasks.remove(task)
        finish_time = current_time + task.l
        heapq.heappush(processors, (finish_time, processor_id))
        
        objective = objective + finish_time * task.w
        order.append(task)
        schedule.append((task.id, processor_id, current_time, finish_time))

    return objective, order, schedule



def greedy(instance):
    objective = 0
    order = []
    schedule = []
    tasks = copy.deepcopy(instance.tasks)
    
    processors = [(0, i) for i in range(instance.n_processors)]
    heapq.heapify(processors)

    while tasks:
        current_time, processor_id = heapq.heappop(processors)
        available_tasks = [task for task in tasks if task.r <= current_time]
        if (not available_tasks):
            # if there aren't any available tasks fetch the earliest released
            min_release = min(tasks, key=lambda x: x.r).r
            current_time = min_release
            earliest_released = [task for task in tasks if task.r == min_release]
            task = max(earliest_released, key=lambda t: t.w/(current_time + t.l))
        else:
            task = max(available_tasks, key=lambda t: t.w/(current_time + t.l))

        tasks.remove(task)
        finish_time = current_time + task.l
        heapq.heappush(processors, (finish_time, processor_id))

        objective = objective + finish_time * task.w
        order.append(task)
        schedule.append((task.id, processor_id, current_time, finish_time))
        
    return objective, order, schedule
