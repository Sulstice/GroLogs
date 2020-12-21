GroLogs: A log reader for the software GROMACS
==============================================

![Python](https://img.shields.io/badge/python-3.6-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![saythanks](https://img.shields.io/badge/GROMACS-5.1-ff69b3.svg)](https://www.computchem.org/)
[![saythanks](https://img.shields.io/badge/Lab-Shen%20Group-ff69b4.svg)](https://www.computchem.org/)

GroLogs was started out of a need to quickly check thet status update of molecular dynamic simulations using GROMACS. By
reading the log files and the steps within the log files we can calculate the time in nanoseconds of the simulation using
this simple formula

```

nanoseconds = steps / 500,000

```

and output to a beautiful table.

Quick Start
===========

First you will need authentication to the cluster or server running the Molecular Dynamics simulation for GROMACS.

First is simple 

1. Register your RSA key with the dedicated server so you don't have to be password prompted when SSH'ing into the server

`GroLogs` class takes 4 arguments

- **target_directory** - target directory where all your log files for this particular experiment will be
- **log_file_name** - the name of the log file. Traditionally, I have everything called as `md_3.log`
- **username** - the username registered on the cluster or particular machine
- **hostname** - the hostname or ip address of the target server that we want to extrapolate information.

Initialize the class like so:

```

log_reader = GroLogs('target_directory/*', 'md_3.log', username, hostname)

```

and then generate a table to output the results

```

log_reader.generate_table()

```

and here is an example of the output:

```

+-------------------------------------------------------+----------+-----------+
|                   --- File Path ---                   |   Step   | Time (ns) |
+-------------------------------------------------------+----------+-----------+
|  file/path/to/experiment/trial_2/                     | 60947999 |  121.896  |
+-------------------------------------------------------+----------+-----------+
|  file/path/to/experiment/trial_3/                     | 68454999 |  136.91   |
+-------------------------------------------------------+----------+-----------+
|  file/path/to/experiment/trial_3/                     | 28107999 |  56.216   |
+-------------------------------------------------------+----------+-----------+

```


Announcements
=============

-   Work has began! Dec 4th
-   0.0.1 version released Dec 4th LogReader
-   0.0.2 version released -> authentication can be passed in and name changed to GroLogs, more documentation!

Installation 
============

GroLogs is going to be distribute via PyPi and as the content store grows we can expand it to other pieces of software
making it accessible to all regardless of what you use. Alternatively, you could have a glance at the source code and copy/paste
it yourself.

To install the reader 

```

python -m pip install grologs

```

Structure ofGroLogs
=======================

Currently, the main subpackages are:

- **grologs**: logreader main class. 


Genesis
=======

LogReader was created because I noticed I was using the same variable across multiple scripts and figure it would be useful
for folk to have.

- Lead Developer [Suliman Sharif](http://sulstice.github.io/)


* * * * *

External links
==============


