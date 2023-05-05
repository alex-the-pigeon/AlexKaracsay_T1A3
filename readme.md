# Terminal Application 

### **Overview**
I have created a 'madlibs' style game that contains a menu showing three different stories to choose from. The user will select the story they'd like to play and it will ask some questions. Once the user input has been collected, the words will be inserted into the story and it will print on the screen. There will be an option to go back to the menu so the game can be played again. 

### **Related links**
- Trello board (project planning)
- insert github link here
- presentation video (YouTube)

### **Installation**

- Python 3
- PyPi packages: Art, Colored, CSV, rich.prompt

Information on how to install program here:

### **Features**
 An interactive menu utelising loops: 
 - Player is presented with multiple options that have a corresponding number. When user input is collected, the appropriate response will run. For example, player selects option 1 and   story 1 will run. 

User input:
- Upon entering a story the player will be asked several questions and prompted to answer in the terminal. This input is collected and then **output** to the story at the end.

Individual stories to play:
- There are four separate stories for the user to play, each with their own set of questions to be asked. Each story file is separate to **main.py** and linked through a **functions** file. These files are then imported into the main file and run when called upon by the user.

Aesthetic features:
- Utelisation of PyPi package **Colored** to change text colour for variety and added snazziness.

