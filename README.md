TO THE NEXT USERS OF THE ZOT BOT:
#### Pre-Requirements
1. Download Python 3.x
<br>    a. I prefer using [Anaconda](https://www.continuum.io/downloads), but you can download Python any way you want
2. Download latest version of Selenium
<br>    a. If pip is not installed, follow this [link](https://pip.pypa.io/en/stable/installing/) and its instructions.
<br>    b. Input the below code into Command Line/Prompt:
<br>        ```
        python -m pip install selenium
        ```
3. Download Chrome Driver and put it in the folder with the Selenium Bot.
<br>    a. Use this link: "https://sites.google.com/a/chromium.org/chromedriver/downloads"

#### How to run it from command line:
1.  Launch Command Line
2.  In Command Line, go to the folder where "Facebook_Module_Selenium.py" is located.
3.  Run "python Facebook_Module_Selenium.py" and follow with the instructions.
        
#### How to modify which Facebook Groups to Post: 
1.  Open "Facebook_Module_Selenium.py" in an IDE.
2.  In the dictionary, "facebook_groups", add or delete any group that you choose.
3.  You can also comment out groups you do not want to post to and uncomment them in when necessary.
        

        
        
FOR NON-USERS:
Goal Of FB_Poster:
--Be able to mass post to all FB groups that the users desires.
--If the user has access to a FB group, then he should be 
able to automatically post to the group at his own convenience.

Current Version 2/20/2018
    Done!!!!!
    
    Extra Features to consider:
    -User friendly UI
    

Current Version 11/05/2016
Using Selenium:

	Good:
		-Send texts through the text file "messages_to_send.txt"
		
	Still need:
		-Make it portable
		-Yet to do a full-scale test.
		

Current Version 11/04/2016
Using Selenium:

	Good:
		-Finally got multiposting to work (was able to deal with stale elements)
		-Can deal with normal groups and buy/sell groups
		-Learning Xpath really helped.
		
	Still need:
		-Clean up code
		-Make it portable
		-Yet to do a full-scale test.
		
	Note:
		-Update chromedriver continuously as weird bugs happen with older chromes

Current Version 9/26/2016
Using Selenium:
	
	Good:
		-Organize prototype
		-Handles Buy/Sell Groups and Regular Groups
	
	Still Need:
		-Be able to send to multiple groups
		-Figure out the issues w/ "Latency"
		-Be able to post onto regular groups one after another
		-Be able to post onto Buy/Sell Groups one after another

Current Version 9/21/2016
Using Selenium:
	
	Good:
		-Organize prototype
		-Handles Buy/Sell Groups and Regular Groups
	
	Still Need:
		-Eventually will need a clean UI
		-Be able to send to multiple groups


Current Version: 9/13/2016
Using Selenium:
	
	Good:
		-Got Input Working
		-Can now post into groups with relative ease
	
	
	Still Need:
		-Organize prototype
		-Be able to send to multiple groups
		

Will now ignore using Facebook API from now on.

Current Version: 6/11/2016
Using Facebook API:

	Current Progress:
		-Finish up program so that it only posts to open groups.
		-Groups that have privacy = "closed" will not allow me to post on their groups, meaning that I have to find another way to multi-post to groups