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
6. **Metrics**: 
I used Sonarcube to make sure that the code follows the best practices. For simplicity I checked my program it locally. It was a pain to use it as it always ran out of memory. Once I gave it enough resources, it finally worked:

<img width="437" alt="Image" src="https://github.com/user-attachments/assets/3e108683-fbaa-44b7-b450-f8108307f92d" />

This was the result of the quality check:

<img width="1198" alt="Image" src="https://github.com/user-attachments/assets/1fe4d396-ea75-4431-a237-178b8a23d1f0" />

We can see that there are no security, maintainability or reliability issues. 

Security:
0 Open Issues: No security vulnerabilities or critical issues are detected in the code.
Rating: A (the best grade possible).

Reliability:
0 Open Issues: No bugs or problems affecting the reliability of the application.
Rating: A.

Maintainability:
0 Open Issues: No identified problems that would make the code hard to maintain or refactor.
Rating: A.

Duplications:
0.0% Duplications: No duplicate code has been found among 433 lines of code analyzed.

Security Hotspots:
4 Hotspots: Areas of the code identified as potentially requiring review for security concerns.
Rating: E (indicating this area needs immediate attention). Needs to be checked.

Of course, tests should be added (I implemented tests in another program, see functional programming directory). 

Also, sonarcube VS code extention gave me a small suggestion:

The issue was a redundant field:

<img width="397" alt="Image" src="https://github.com/user-attachments/assets/b768d5e1-c4c8-4eba-94f1-d8189c8e0bd6" />

Modified:

<img width="354" alt="Image" src="https://github.com/user-attachments/assets/75adc8a5-7306-4d94-b37a-048860fe8e03" />

Those were the only issues. Good!

7. **Clean Code Development:**

I made sure the code follows the clean code principles:
- No negative conditionals
- Clear naming
- Followed naming convention
- Functions mostly only do one thing

My clean code cheet sheet [here](https://github.com/beksinska/cv_improvement_tool/blob/main/software_engineering_tasks/clean_code_cheet_sheet.pdf)


8. **REFACTORING**: 

As checked with SonarQube, there were no redundancies or major maintanence problems. However, there was a room for improvements.

The function uploadPDFToVectorStore was very long and looked like a spagetti code. It was definetely not modular, so I decided to split it into smaller pieces.

<img width="652" alt="Image" src="https://github.com/user-attachments/assets/58209c7d-7ff2-4853-a824-f9dfde44aa77" />

This is how my IDE offered to refactor it: 

<img width="608" alt="Image" src="https://github.com/user-attachments/assets/92a0983f-c6a9-4854-a961-96d22d6bbeab" />

I chose extracting the function in module scope. This is what I got:

<img width="608" alt="Image" src="https://github.com/user-attachments/assets/604f5624-9956-4f67-a2ea-61c23c73d08e" />

I did the same with two other functions. This way it is easier to test and maintain the code. 

<img width="655" alt="Image" src="https://github.com/user-attachments/assets/b44d0f23-9689-4bd4-a681-7f287e2ed137" />

This is what my final function uploadPDFToVectorStore lookes like:

<img width="507" alt="Image" src="https://github.com/user-attachments/assets/8533be7a-b059-48d7-8b9d-7721c1caf110" />

Result:

- Extract Method Pattern: Split the monolithic function into smaller, focused functions that each have a single responsibility:
uploadFile: Handles file upload
createVectorStore: Creates the vector store with the file
updateAssistantWithVectorStore: Updates the assistant

- Improved Error Handling:

Each function now has its own try-catch block with specific error messages
More descriptive error messages for easier debugging

- Better Separation of Concerns:

Each function handles one specific task
The main function orchestrates the process flow
Same level of abstraction
Logging is consistent across all operations

- Improved Readability:

Clear function names that describe their purpose
Sequential steps are clearly visible in the main function
Consistent error handling pattern

- Better Maintainability:

Each function can be tested independently!
Changes to one part of the process won't affect others
New functionality can be added without modifying existing code

This refactoring follows several principles:
- improves code clarity and readability
- reduces method size and complexity
- follows the single responsibility principle
- makes the code more testable
- makes future modifications easier

9. **BUILD**: [here](https://github.com/beksinska/cv_improvement_tool/tree/main/software_engineering_tasks/build)

10. **CONTINOUS DELIVERY:** 

I used GitHub Actions to configure my CICD pipeline.
First I added the configuration file [here](https://github.com/beksinska/ciwi/blob/main/.github/workflows/main.yml) \
Then I reorganised my project structure to make it more clean and logical:

<img width="204" alt="Image" src="https://github.com/user-attachments/assets/1fc54f38-0394-4583-8a84-aaaacad20731" />

Finally, I pushed the changes to main and it worked! [Amazing](https://github.com/beksinska/ciwi/actions)

<img width="854" alt="Image" src="https://github.com/user-attachments/assets/08198638-a865-4f43-a0c5-77fc8f366234" />

Even app start verification passed!

<img width="513" alt="Image" src="https://github.com/user-attachments/assets/c6fd66e2-5a19-47e4-a115-4b81ae3be46e" />

11. Integrate some nice **UNIT TESTS**: [here](https://github.com/beksinska/cv_improvement_tool/tree/main/software_engineering_tasks/functional_programming)

12. **IDE**:

My favorite IDE is IntelliJ, and I have enjoyed using it for many years. However, as I code in multiple languages, I would need to have PyCharm, CLion (they are also nice), and even WebStorm separately. With my small computer, it's a pain. So I had to become fluent with VSCode. It is acceptable and is free! 

My favourite shortcut is SHIFT+OPTION + ↓, which copies the line down on Mac.

13. **AI Coding**:

I set up GitHub copilot as a VSCode extention. So far it helped me refactor my code. For example, 

Original code:
```javascript
async function createThread() {
  const thread = await openai.beta.threads.create()
  console.log(thread)
  threadId = thread.id
  return thread
}
```
Copilot suggestions were:
- The createThread function does not handle errors. If the openai.beta.threads.create() call fails, it will cause the application to crash. Add a try-catch block to handle potential errors.
- The console.log(thread) statement should include a more descriptive message to make the logs clearer.

However, the code that Copilot suggested was a little buggy. I tried to fix it myself following the suggestions: 
```javascript
async function createThread() {
  try {
    const thread = await openai.beta.threads.create()
    console.log(thread)
    threadId = thread.id
    return thread
  } catch (error) {
    console.error('Error creating thread:', error.message)
  }
}
```
Now, the function checks if the error occurred and, if so, returns the error message.

Sometimes, Copilot gives good suggestions that help me learn how to make the code cleaner. However, I do not always trust the code it gives, as it is often quite dummy.

14. **FUNCTIONAL PROGRAMMING:** [here](https://github.com/beksinska/cv_improvement_tool/tree/main/software_engineering_tasks/functional_programming)
