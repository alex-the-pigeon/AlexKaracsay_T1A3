# Terminal Application 

### **Overview**
I have created a 'madlibs' style game that contains a menu showing four different stories to choose from. The user will select the story they'd like to play and it will ask some questions. Once the user input has been collected, the words will be inserted into the story and it will print on the screen. There will be an option to go back to the menu so the game can be played again. 

### **Related links**
- [Trello board (project planning)](https://trello.com/b/snhvaaXb/terminal-application)
- [GitHub repository](https://github.com/alex-the-pigeon/AlexKaracsay_T1A3)
- presentation video (YouTube)

### **Installation**

- Python 3
- PyPi packages: Art 5.9, Colored 1.4.4, Clear 2.0.0

Information on how to install program here:

1. Follow GitHub link above and click on green code button (insert screenshot here)
2. Download ZIP file
3. Open the terminal (mac) / cmd (windows)
4. Run the run.sh file commands by copy/pasting them from the file into the open terminal on your computer. What each command will do is noted here on the screenshot. (insert screenshot)
5. The Silly Libs game will run and you can play


### **Features**
 An interactive menu utelising loops: 
 - Player is presented with multiple options that have a corresponding number. When user input is collected, the appropriate response will run. For example, player selects option 1 and story 1 will run. 

User input:
- Upon entering a story the player will be asked several questions and prompted to answer in the terminal. This input is collected and then **output** to the story at the end.

Individual stories to play:
- There are four separate stories for the user to play, each with their own set of questions to be asked. Each story file is separate to **main.py** and linked through a **functions** file. These files are then imported into the main file and run when called upon by the user.

- Each question linked to a user input() is assigned to a variable which is then used within the story string. Each variable is named with a prefix of the story it belongs to and then a short desciptive word. For example: 

    ```s1_vehicle = input("Name a type of vehicle: ")```

- Once all the user input has been collected it is then inserted into the story f string with curly braces {variable_name} so it prints in the correct places in the story.

Aesthetic features:
- Utelisation of PyPi package **Colored** to change text colour for variety and added snazziness.

- ASCII art text header made with **Art** package which changes randomly each time the program is run.

### **Style guide**
The style guide used in this project is PEP 8 to make the code as readable as possible. Please find reference link here:
[PEP8 Guide](https://peps.python.org/pep-0008/)