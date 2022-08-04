
# Recipe Project

## Getting Started Notes:
* Look for "# todo, write some code here" to get started on some code.
  * I'd suggest starting with the models in the "models" folder. Feel free to add new classes if you need to!
  * I'd then work on the POST and GET endpoints under "controllers/recipies.py", revisiting the models as you need.
* Make sure to create a new branch and work there! Submit a PR when you're done. [Here's a Git cheat sheet.](https://education.github.com/git-cheat-sheet-education.pdf)  
* Run start.sh from a bash shell (Linux, Cygwin, Git Shell, etc.) to get things running.
* There's no real "UI" to this at the moment. This is primarily a backend project.
  * After starting the server using start.sh, take note of the address. If you copy and paste that address and add "/docs" onto the end of the domain name and port, you can see the "swagger" or docs page that will make testing things easier. (E.g., "http://127.0.0.1:8000/docs", but double check the port number.)
* There's a POST endpoint that exists, so you can kind of see how that works.
* [TinyDB](https://tinydb.readthedocs.io/en/latest/) is a simple DB implementation that hosts the DB in a local file used for this project. Not good for most production purposes, but workable for a simple project.
* [HTTP methods and their purposes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), you should be familiar with at least the usual 4 involved in create, read, update, delete (CRUD, for HTTP that's POST, GET, PUT, DELETE).

## Some Things to Note:
* This sample project doesn't support HTTPS, authentication, authorization. Feel free to add that, but it's a bit more of an advanced topic. Don't post any sensitive information with this or ask for sensitive information from users.
