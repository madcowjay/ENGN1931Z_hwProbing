# hwProbing
OBD-II Queries Homework Assignment for ENGN1931Z

You want to use a low-cost CAN-bus reader to query relevant vehicle information through [OBD-II PID](https://en.wikipedia.org/wiki/OBD-II_PIDs) requests. To make sure you understand the command syntax, you decide to first query the available [Mode 1 PIDs](https://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_01) on your own car.

To do this, you have setup a web app that can send CAN commands to your car, and then returns the CAN responses. To simplify the format, your web app automatically handles the CAN address and frame process, so that you can send commands as 8 bytes of hexadecimal encoded data. Responses are also returned as 8 bytes of hexadecimal data, but a single query may return zero, one, or two responses from different ECUs. So a response can consist of 0, 8, or 16 bytes of hex-encoded data. (*Note that it may help to look at the [example PID query and response information here](https://en.wikipedia.org/wiki/OBD-II_PIDs#CAN_.2811-bit.29_bus_format)*)

**The URL for the simulated OBD system is: https://script.google.com/macros/s/AKfycbw24E3r_y1Gq3IpFWUZtfx3chNr1uYgz8kKp6DgHx_4dOoKXlM/exec?, and you can pass your queries as a hexadecimal encoded 8-byte string to the parameter `query`(e.g., `.../exec?query=1A20304050607080`)**

Please write a python script that performs the following actions:

* a. Finds the supported Mode 01 PIDs by sequentially sending the "supported PIDs" commands (e.g. `00`, `20`, `40`, ... `A0`, `C0`,`E0`) as described [here](https://en.wikipedia.org/wiki/OBD-II_PIDs), parses the [bit-encoded responses](https://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_1_PID_00), and return a list of all supported PIDs. *NB: You can double check the validity of your code by seeing if the supported PIDs actually work, but you cannot brute force a solution - credit will only be given for correctly parsing the reply data from the Support PIDs queries.)

* b. Queries the Ambient Air Temperature and prints the value in degrees Celsius.

* c. Queries the Control Module Voltage and prints the value in Volts for each responding ECU. (*Hint: these values should be greater than 12 Volts.*)

`hw_probing.py` is a template code for the assignment. **Please review the comments at the top of that file.**  `submit.py` is the script that will submit your code to the autograder.

Please note you are welcome to try this assignment as many times as you would like. (There is no penalty for failed attempts, because I wanted to encourage you to practice, test, and debug.) **However, please make sure to obey the class collaboration policy --- do not share your code with others; please write and debug on your own!**
