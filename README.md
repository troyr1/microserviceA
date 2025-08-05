This microservice queries a text file called requests.txt to either save a dream or retrieve a dream from either a specific user or all saved dreams into a text file response.txt.

To request date from this microservice and engage with its functionality, below is a sample call written to requests.txt:

Saving Dream:Troy
I felt like I was flying!

Once this has been written to requests.txt, the dream is saved under the user after "Saving Dream:" with the dream being the second line in the text file written.
This saves the dream and text to dreams.txt which can be retrieved at any point with the following call:

Requesting Dream:Troy

When "Requesting Dream:Troy" is written to the requests.txt file, all dreams with the user listed as Troy are recorded and written to response.txt for further use.

All dreams of all users can be retrieved from the following call:

Requesting Dream:ALL DREAMS

This will print every dream previously saved to the response.txt file for futher use.

This microservice will need to be locally hosted and called, with text written to the requests.txt file in its working directory and the response retrieved from the response.txt file in the working directory. 
