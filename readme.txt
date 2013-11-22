Author: Andy Shaw
Date: 11/22/2013
Course: CSE 3521 - Survey of Artificial Intelligence, Assignment04

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

------------------------------------Compilation/Running---------------------------------------------
This program is compatible with Python 2.6 (runs on the OSU Linux machines)

To run the learning agent, invoke the command:
$ python learner.py <places_file> <transitions_file> [SILENT]
    -> SILENT is an optional flag to display the iteration output or not
    -> Provided files for the lab are in the Input_Files directory
    
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

---------------------------------------Known Errors-------------------------------------------------
The program does not remember when all of the states converge, so there is no output for that
    statistic.  
    
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

------------------------------------------Notes-----------------------------------------------------
The program is compatible with running both Deterministic and Non-deterministic transitions by 
    only changing the input file.  There is no requirement of the user to use flags or anything.
    
The program will currently do 1000 iterations, and by then, all points in the provided files have 
    converged.