def taskAssignment(k, tasks):
    sorted_tasks = sorted(enumerate(tasks), key = lambda task: task[1])

    # Create pairs of tasks with the smallest and largest times
    # to minimize the total time taken to complete all tasks
    # The first task is paired with the last task, the second task with the second last task, and so on.
    return [[sorted_tasks[i][0], sorted_tasks[-i-1][0]] for i in range(k)]

