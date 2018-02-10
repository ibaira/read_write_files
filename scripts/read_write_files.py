#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import queue
import sys
from functools import wraps
from pathlib import Path
from threading import Thread

__author__ = "Ismael Baira"


def create_logger():
    """Create a logger showing a timestamp and a message

    :rtype logging.Logger
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def run_async(func):
    """run_async(func)

    Function decorator, intended to make "func" run in a separate
    thread (asynchronously).
    :rtype Thread object
    """
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl

    return async_func


class Worker(object):
    """Class that identifies an abstract worker"""

    def __init__(self, number=0):
        """Assign a worker to a number

        :type number: int
        """
        self.number = int(number)
        self.extension = ".txt"

    def work(self):
        pass


class ReadingWorker(Worker):
    """ReadingWorker class"""

    def __init__(self, number=0):
        """Assign a reading worker to a input
        file pattern

        :type number: int
        """
        super().__init__(number)
        self.input_folder = "input_files"  # "../input_files"
        self.file_pattern = "input"

    @run_async
    def work(self):
        """This thread reads an input file and adds its lines to a queue"""
        log = create_logger()
        file = self.file_pattern + str(self.number) + self.extension
        origin_path = os.path.join(os.path.dirname(__file__),
                                   self.input_folder, file)

        if Path(origin_path).is_file():
            with open(origin_path, "r") as f:
                for line in f:
                    q[self.number].put(line)
                    # log.info("{}. READ: ".format(self.number) + line)
                # log.info("{}. No more lines to read!".format(self.number))
        else:
            with q[self.number].mutex:
                q[self.number].queue.clear()
            print("input{}.txt does not exist!".format(self.number))
        # stop worker
        q[self.number].put(None)


class WritingWorker(Worker):
    """WritingWorker class

    :type number: int
    """

    def __init__(self, number=0):
        super().__init__(number)
        self.output_folder = "output_files"  # "../output_files"
        self.file_pattern = "output"

    @run_async
    def work(self):
        """This thread reads a queue and writes its content in a file"""
        log = create_logger()
        file = self.file_pattern + str(self.number) + self.extension
        dst_path = os.path.join(os.path.dirname(__file__), self.output_folder, file)
        with open(dst_path, "w") as f:
            while True:
                try:
                    item = q[self.number].get(timeout=5)
                except queue.Empty:
                    # log.info("{}. Queue is empty".format(self.number))
                    q[self.number].task_done()
                    break

                if item is None:
                    # No more lines ready to write
                    continue

                f.write(item)
                # log.info("{}. WRITEN: ".format(self.number) + item)
                q[self.number].task_done()


def main():
    """Main function that runs reading and writing workers
    assigning a queue per pair.
    """
    global q
    q = []
    threads = []
    r_workers = []
    w_workers = []
    num_worker_threads = 20

    for i in range(num_worker_threads):
        q.append(queue.Queue())
        r_workers.append(ReadingWorker(i))
        w_workers.append(WritingWorker(i))

        # Reading and writing workers
        threads.append(r_workers[i].work())
        threads.append(w_workers[i].work())

    # block until all tasks are done
    for q_element in q:
        q_element.join()
    for t in threads:
        t.join()
    for r_obj, w_obj in zip(r_workers, w_workers):
        del r_obj
        del w_obj
    return 0


if __name__ == '__main__':
    main()
    print("END")
