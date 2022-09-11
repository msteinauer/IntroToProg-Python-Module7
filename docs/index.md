Mike Steinauer
9/09/2022
Foundations of Programming: Python
Module 7
Here is my GitHub link for Assignment07
https://github.com/msteinauer/IntroToProg-Python

Pickling and Error Handling

1	Intro

This document shows how I used error handling and pickling to create the assigned starter script into a fully working script.

2	Processing

I put together the processing section using psedudocode and creating functions to save, read and input data.  You will notice at the top of the script that import of pickle is used, this was part of the starter script.
Figure 1 shows the setup of the script with the first function that saves data to a file.  Notice that this is saves as binary using the “ab” trigger. 
 https://github.com/msteinauer/IntroToProg-Python-Module7/blob/main/docs/Figure1.png
Figure 1: Function to save_data_to_file



















Figure 2 shows the read_data_from_file function. The data is read into memory using the load option in pickle.  Once loaded into memory, we can use it as needed to add to it or save to file. Error handling is used in this function to let the user know that the file is empty.

 
Figure 2: Function to read data from a file.

Figure 3 shows the id_name_input function. This allows the user to input new data which is saved into the txt and dat files thus showing pickle in all it’s glory.  If the user tries to use anything besides a number for the ID, error handling is set in place to remind them to use a number.

 
Figure 3: Function to input data.


3	Presentation
Figure 4 Saves and prints data to the file. In the presentation section we not only save data to the file; we print out what has been saved for the user to confirm. 


 
Figure 4: Saving and printing of data.
 
2	Summary
In summary, Assignment07 used Structured Error Handling and Pickling.
The pickling process was very simple way to add data to a file that encrypts it in an unsecure manner. Structured error handling is a great tool to allow you to keep the user informed of what is needed from them in case the move away from the type of data needed to run the script.
