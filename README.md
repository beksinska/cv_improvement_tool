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
6. **Metrics** 
I used Sonarcube to make sure that the code follows the best practices. It gave me two suggestions:

First issue was a redundant field:

<img width="397" alt="Image" src="https://github.com/user-attachments/assets/b768d5e1-c4c8-4eba-94f1-d8189c8e0bd6" />

Modified:

<img width="354" alt="Image" src="https://github.com/user-attachments/assets/75adc8a5-7306-4d94-b37a-048860fe8e03" />

Second issue was an unnecessary escape character:

<img width="795" alt="Image" src="https://github.com/user-attachments/assets/dff0f610-2988-4cdb-b526-193d41074d12" />

Modified:

<img width="676" alt="Image" src="https://github.com/user-attachments/assets/e7de69a8-1a83-438b-aefe-f09ca2f70f6c" />

Those were the only issues. Good!

7. **Clean Code Development:**

I made sure the code follows the clean code principles:
- No negative conditionals
- Clear naming
- Followed naming convention
- Functions have no side-effects

8. **REFACTORING**: 

OPENAI_API_KEY was not validated for existence before being used. This could lead to runtime errors if the environment variable is not set.

<img width="395" alt="Image" src="https://github.com/user-attachments/assets/3ecf0067-3a4d-4a99-868d-d459d4f74df2" /> 

Added a check to ensure the key is present.

<img width="534" alt="Image" src="https://github.com/user-attachments/assets/4921e248-4c55-4b8d-a104-bb4b33569a47" />

The function uploadPDFToVectorStore did not check for failures in file upload or vector store initialization.

<img width="652" alt="Image" src="https://github.com/user-attachments/assets/58209c7d-7ff2-4853-a824-f9dfde44aa77" />

This could also lead to errors. To ensure my code follows best practices, I added checking.

<img width="638" alt="Image" src="https://github.com/user-attachments/assets/f0216516-901b-4470-a536-7353c3bef4a5" />

9. **BUILD** Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could also be disconnected from the project just to learn a build tool!) => to be merged with 7!

For build management I decided to use Parcel because it has a good documentation. I created a small web application to test it.
First I created src directory, added my index.html file there and ran npx parcel src/index.html. Then I added scripts to package.json file.

10. **CONTINOUS DELIVERY:** 

I used GitHub Actions to configure my CICD pipeline.
First I added the configuration file [here](https://github.com/beksinska/ciwi/blob/main/.github/workflows/main.yml) \
Then I reorganised my project structure to make it more clean and logical:

<img width="217" alt="Image" src="https://github.com/user-attachments/assets/5f37b301-aea3-4e43-9da3-e10c395cd51e" />

Finally, I pushed the changes to main and it worked! [Amazing](https://github.com/beksinska/ciwi/actions)

<img width="854" alt="Image" src="https://github.com/user-attachments/assets/08198638-a865-4f43-a0c5-77fc8f366234" />

Even app start verification passed!

<img width="513" alt="Image" src="https://github.com/user-attachments/assets/c6fd66e2-5a19-47e4-a115-4b81ae3be46e" />

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
