# Mr Sedgwick Bot
### About
A Telegram bot that is able to store brief schedules of the weeks for the user.

### Programming details
* *Python*
* The *aiogram* library
* Ready for *docker*
* License *GPLv3* - you may copy, share, edit, redistribute the code,
but keep the license

### Dependencies
Managed with pip. Be sure to check out the Pipfile.

* Python v3.10 
* aiogram v2.18
* environs (any)

### Environment variables
You should create a .env file that looks like this:
```
ADMINS=111111111
BOT_TOKEN=1111111111:aaaaaaaaaabbbbbbbbbbcccccccccdddddd
IP=255.255.255.255
```
You can use "localhost" for the IP as well.

### Docker deploy
In the repository directory do:
```
vim .env # write envs into the file
mkdir db
docker build -t sedgwickbot:latest .
docker run -d --restart always --name bot -p 8080:8080 -v $PWD/db:/home/appuser/db sedgwickbot
```
