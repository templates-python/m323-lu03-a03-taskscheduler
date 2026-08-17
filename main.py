"""Task Scheduler.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu03/aufgaben/taskscheduler
"""

import time


def task1():
    print('Task 1 executed!')


def task2():
    print('Task 2 executed!')


def task_scheduler(tasks, delay):
    for task in tasks:
        task()
        time.sleep(delay)


def task_scheduler_expert(tasks, delays):
    for task, delay in zip(tasks, delays):
        task()
        time.sleep(delay)


if __name__ == '__main__':
    demo_tasks = [task1, task2]
    demo_delay = 2
    demo_delays = [2, 3]
    task_scheduler(demo_tasks, demo_delay)
    task_scheduler_expert(demo_tasks, demo_delays)
