**Read-write-files**
====================

Description
-----------
This project is a simple messaging system using queues. The workflow is as follows:

#. Read a line from a file 
#. Write it to a queue service 
#. Read it back from the queue service 
#. Write it back to a file 
 
The process takes place as 2 asynchronous workers exchanging information using a queue. 

The project has been developed using Ubuntu 16.04LTS and Pycharm 2017 (python 3.5).

It has two deployment strategies:

#. One using Pyinstaller to create a one folder containing the executable compatible intended to be compatible with Linux, Windows, and Mac.

#. Another one using a Docker container.


Installation
------------

- To install Pyinstaller follow the instructions found at Pyinstaller_.

- To install docker in Ubuntu:

.. code-block:: bash

   sudo apt-get install docker


- To install coverage to calculate the test coverage of our code:

.. code-block:: bash   

   $ pip3 install coverage


.. _Pyinstaller: http://www.pyinstaller.org/


Usage
-----

**Using the executable created with Pyinstaller**

.. code-block:: bash

   $ cd <folder_path>/scripts/dist/read_write_files
   $ ./read_write_files 


**Using the Docker container**

To build the docker container run:

.. code-block:: bash

   $ cd <path-to-project-folder>
   $ docker build -t <CHOOSE_NAME> .

Run the docker container:

.. code-block:: bash

   $ docker run <CHOSEN_NAME>

The docker container automatically runs our script.

**Using test coverage**

.. code-block:: bash

   $ coverage run read_write_files.py
   $ comverage report -m
   $ coverage html

Credits
-------


License
-------
