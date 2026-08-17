"""Task Scheduler.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu03/aufgaben/taskscheduler
"""

def task1():
    """
    Eine einfache Funktion, die eine Meldung ausgibt, um zu signalisieren, dass Task 1 ausgeführt wurde.
    """
    pass


def task2():
    """
    Eine einfache Funktion, die eine Meldung ausgibt, um zu signalisieren, dass Task 2 ausgeführt wurde.
    """
    pass


def task_scheduler(tasks, delay):
    """
    Führt eine Liste von Tasks mit einer festen Zeitverzögerung zwischen jedem Task aus.

    Args:
    tasks (list): Eine Liste von Funktionen, die ausgeführt werden sollen.
    delay (int): Die Zeitverzögerung in Sekunden zwischen den einzelnen Tasks.

    Returns:
    None
    """
    pass


def task_scheduler_expert(tasks, delays):
    """
    Führt eine Liste von Tasks mit unterschiedlichen Zeitverzögerungen zwischen jedem Task aus.

    Args:
    tasks (list): Eine Liste von Funktionen, die ausgeführt werden sollen.
    delays (list): Eine Liste von Zeitverzögerungen in Sekunden für die jeweiligen Tasks.

    Returns:
    None
    """
    pass


if __name__ == '__main__':
    demo_tasks = [task1, task2]
    demo_delay = 2
    demo_delays = [2, 3]
    task_scheduler(demo_tasks, demo_delay)
    task_scheduler_expert(demo_tasks, demo_delays)
