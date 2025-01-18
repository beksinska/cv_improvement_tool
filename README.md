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

My clean code cheet sheet [here](https://github.com/beksinska/cv_improvement_tool/blob/main/software_engineering_tasks/clean_code_cheet_sheet.pdf)


8. **REFACTORING**: 

OPENAI_API_KEY was not validated for existence before being used. This could lead to runtime errors if the environment variable is not set.

<img width="395" alt="Image" src="https://github.com/user-attachments/assets/3ecf0067-3a4d-4a99-868d-d459d4f74df2" /> 

Added a check to ensure the key is present.

<img width="534" alt="Image" src="https://github.com/user-attachments/assets/4921e248-4c55-4b8d-a104-bb4b33569a47" />

The function uploadPDFToVectorStore did not check for failures in file upload or vector store initialization.

<img width="652" alt="Image" src="https://github.com/user-attachments/assets/58209c7d-7ff2-4853-a824-f9dfde44aa77" />

This could also lead to errors. To ensure my code follows best practices, I added checking.

<img width="638" alt="Image" src="https://github.com/user-attachments/assets/f0216516-901b-4470-a536-7353c3bef4a5" />

9. **BUILD**: Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could also be disconnected from the project just to learn a build tool!) => to be merged with 7!

For build management I decided to use Parcel because it has a good documentation. I created a small web application to test it.
First I created src directory, added my index.html file there and ran npx parcel src/index.html. Then I added scripts to package.json file.

10. **CONTINOUS DELIVERY:** 

I used GitHub Actions to configure my CICD pipeline.
First I added the configuration file [here](https://github.com/beksinska/ciwi/blob/main/.github/workflows/main.yml) \
Then I reorganised my project structure to make it more clean and logical:

<img width="204" alt="Image" src="https://github.com/user-attachments/assets/1fc54f38-0394-4583-8a84-aaaacad20731" />

Finally, I pushed the changes to main and it worked! [Amazing](https://github.com/beksinska/ciwi/actions)

<img width="854" alt="Image" src="https://github.com/user-attachments/assets/08198638-a865-4f43-a0c5-77fc8f366234" />

Even app start verification passed!

<img width="513" alt="Image" src="https://github.com/user-attachments/assets/c6fd66e2-5a19-47e4-a115-4b81ae3be46e" />

11. Integrate some nice **UNIT TESTS** in your Code to be integrated into the Build!

For test I used a populat tool Jest. First I updated package.json to include test scripts.
Then I updated configuration file for GitHub Action workflow to run tests.

12. **IDE**:

My favorite IDE is IntelliJ, and I have enjoyed using it for many years. However, as I code in multiple languages, I would need to have PyCharm, CLion (they are also nice), and even WebStorm separately. With my small computer, it's a pain. So I had to become fluent with VSCode. It is acceptable and is free! My favourite shortcut is SHIFT+OPTION + ↓, which copies the line down on Mac.

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

14. **FUNCTIONAL PROGRAMMING:** [here]
