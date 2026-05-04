### When starting Github

- On Github.com - Create a repository
a. Provide the repository name
b. Set the privacy
c. Get the repository url on creation

- Start git processes from project terminal
1. Initialising the git folder : git init
2. Connect local project to repo url : git remote add origin <url>
3. Initial adding of files : git add .
4. Make commit : git commit -m "write a commit message"
5. Ensure you have a password token to allow push 
6. Push using token via this command :: git push origin master  -  **Where master is referencing 
the default branch where work will be saved

### To update project repo
- git add .
- git commit -m "commit message here"
- git push -u origin master/main

## To remove items already pushed before -gitignore
- git rm --cached .env
- git commit -m "add"
- git push origin master/main