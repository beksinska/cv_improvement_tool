# Ciwi

## TASKS

1. **22 Oct**: Name, Project (little description) and GitHub [5 Points] - Done
2. **01st Dec**: First Deliverable with good content [15 Points] - Done
3. **20th Jan**: Final GitHub with all Tasks

**A) Write a small pet project to get into coding again. The code in GitHub can be relatively simple (e.g., a game with console output). The doc can be short! (in contrast to the one below)** - Done: [here](https://github.com/beksinska/ciwi)

**B**) Make sure each person has applied the following topics on the code which have been taught in the lecture:

1. Use and understand **Git!** Be able to apply the basic commands. Can you experiment with time travelling or branches/merges? **Done.**
2. **UML**: [here](https://github.com/beksinska/cv_improvement_tool/tree/main/software_engineering_tasks/uml)
3. **Requirements**: [here](https://vintage-snowboard-5bd.notion.site/Requirements-17ac7d8ad36180f0b780fd1889f39b9d?pvs=4)
4. **Analysis**: [here](https://github.com/beksinska/cv_improvement_tool/blob/main/software_engineering_tasks/Analysis.pdf)
5. **DDD**: [here](https://github.com/beksinska/cv_improvement_tool/tree/main/software_engineering_tasks/ddd)
6. **Metrics** at least two. Sonarcube would be great. Other non-trivial metrics are also fine.
I used Sonarcube to make sure that the code follows the best practices. It gave me two suggestions:\
First issue was a redundant field:

<img width="397" alt="Image" src="https://github.com/user-attachments/assets/b768d5e1-c4c8-4eba-94f1-d8189c8e0bd6" />

Modified:

<img width="354" alt="Image" src="https://github.com/user-attachments/assets/75adc8a5-7306-4d94-b37a-048860fe8e03" />

Second issue was an unnecessary escape character:

<img width="795" alt="Image" src="https://github.com/user-attachments/assets/dff0f610-2988-4cdb-b526-193d41074d12" />

Modified:

<img width="676" alt="Image" src="https://github.com/user-attachments/assets/e7de69a8-1a83-438b-aefe-f09ca2f70f6c" />

Those were the only issues. Good!\
7. **Clean Code Development:** A) At least 5 points you can show me with an explanation of why this is clean code in your code and/or what has improved & B) >>10 points on your personal CCD cheat sheet. E.g. a PDF.
I made sure the code follows the clean code principles:
- No negative conditionals
- Clear naming
- Followed naming convention
- Functions have no side-effects\
8. **REFACTORING**: Show me two (non-trivial) Refactoring Examples of your code! Showing the original content and the refactored code! Explain what happened, why and how it has improved! Again: do not send me pure AI work!
9. **BUILD** Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could also be disconnected from the project just to learn a build tool!) => to be merged with 7!
10. **CONTINOUS DELIVERY:** show me your pipeline using e.g. **Jenkins**, **GitHub Actions**, GitLab CI, etc. E.g. you can also use Jenkins Pipelining or BlueOcean, etc. But at least insert more than 2 script calls as done in the lecture! (e.g. also call Ant or Gradle or something else).
11. Integrate some nice **UNIT TESTS** in your Code to be integrated into the Build!
12. Use a good **IDE** and get fluent with it: e.g. VSCode, IntelliJ. What are your favourite key shortcuts?!
13. **AI Coding**: Set Up an AI-coding environment on your computer like ZED, Aider, free Cursor / Windsurf programs, etc. Show your steps and personal experiences! ([ref](https://newsletter.pragmaticengineer.com/p/ide-that-software-engineers-love))
14. **FUNCTIONAL PROGRAMMING:** prove that you have covered all functional aspects in your code as:
    - only final data structures
    - (mostly) side-effect-free functions
    - the use of higher-order functions
    - functions as parameters and return values
    - use closures / anonymous functions
    
    You can also do it outside of your project. Even in other languages such as F#, Clojure, Julia, etc.
