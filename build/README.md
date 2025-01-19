For build management I decided to use Parcel because it has a good documentation. I created a small web application to test it.
First I created src directory, added my index.html file there and ran npx parcel src/index.html. Then I added scripts to package.json file, so I can start the app by running npm start. Then I added main.js file for logic and main.scss for styles.
The benefit of Parcel is that it will transform scss files on it's own. It creates dist directory where the built code goes, so if we need some server to use the code, we should point a server to that directory. This is what it lookes like:

<img width="290" alt="Image" src="https://github.com/user-attachments/assets/44848ac8-d7f1-4f95-a903-d295212a0b75" />

To run the project

- Clone the repository:

```
git clone https://github.com/beksinska/cv_improvement_tool
```

- Go to the project directory:

```
cd build
```

- Install dependencies

```
npm install
```

- Run the program:

```
npm start
```
