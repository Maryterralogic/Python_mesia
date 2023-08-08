# Python_mesia

To install Jenkins, follow these steps:
1. Go to the official Jenkins website: [https://www.jenkins.io/](https://www.jenkins.io/)
2. Download the installer suitable for your operating system (Windows, macOS, or Linux).
3. Follow the installation instructions for your operating system.

Setup and Configuration:
1. Start Jenkins after installation.
2. Access Jenkins using your web browser at [http://localhost:8080](http://localhost:8080).
3. Retrieve the initial admin password from Jenkins logs or the setup wizard.
4. Follow the setup wizard to complete the initial configuration.

Freestyle Project in Jenkins:
1.Create New Freestyle Project in Jenkins.
2.Configure and Build the Job for every 10 minutes.
3.Pass few of your builds and Fail few of your builds.
4.Check logs of your executed builds.

Git Operations
1.Create Repository in git with your terralogic credentials.
2.Push your source code into your repository.
3.Add README.md file and add your commands to execute your source code in local system.

Source code into Repositary using Git bash command:
C:/ProgramData/Jenkins/.jenkins/workspace - Jenkins Local Path:
This is the local path on your Jenkins server where the Jenkins workspace is located. It is the directory where Jenkins jobs are built and workspace data is stored.

https://github.com/Maryterralogic/Python_mesia.git - Repository Link:
This is the link to the remote GitHub repository you want to work with. It points to the "Python_mesia" repository under the GitHub account "Maryterralogic".

git config --global user.name "maryterralogic":
This command sets the global Git configuration for the username to "maryterralogic". It associates the specified username with Git commits.

git config --global user.email "mesia.mary@terralogic.com":
This command sets the global Git configuration for the user's email to "mesia.mary@terralogic.com". It associates the specified email with Git commits.

git config --global --add safe.directory C:/ProgramData/Jenkins/.jenkins/workspace:
This command adds the specified path (C:/ProgramData/Jenkins/.jenkins/workspace) to the list of safe directories in the global Git configuration. This step is optional and may be used to avoid accidental commits from Jenkins workspace.

git status:
This command displays the current status of the Git repository. It shows any changes made to tracked files and untracked files.

git add .:
This command stages all the changes in the current directory (including subdirectories) for the next commit. The changes will be included in the next commit snapshot.

git status:
After staging the changes, this command shows the status of the Git repository again. It allows you to review the staged changes before committing.

git commit -m "first commit":
This command creates a new commit in the Git history, saving the changes you staged in the previous step. The commit message, "first commit", is used to describe the changes made in this commit.

git remote add origin https://github.com/Maryterralogic/Python_mesia.git:
This command adds a new remote repository named "origin" with the provided URL (https://github.com/Maryterralogic/Python_mesia.git). This allows you to push your local commits to the remote repository.

git push origin master:
This command pushes your local commits to the "master" branch of the remote repository named "origin". The changes made in your local repository are now reflected in the GitHub repository.


