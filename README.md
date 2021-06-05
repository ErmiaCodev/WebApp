# WebApp

### It's A PowerFull Full Stack WebApp

#### For Front Side Used SSR of [NUXT.JS](https://nuxtjs.org)

#### For Back Side Used [Django](https://djangoproject.com)

It include CMS(For Making Blog),\
  Auth System(For registeration And Login), \
  Mail System (Compose & Inbox),\
  Bootstrap Design [(Learn More)](https://getbootstrap.com/)

## Deploying:
#### Using Nginx As WebServer WIth The Confs
[NGINX](https://github.com/GeekyChunk/WebApp/tree/main/WebServerCFG)
#
Using Gunicorn For Django Deamen
#
Using MP2 For Nuxt Deployment sample Conf In FrontEnd Directory

### TODO: 

- [X] Ruby Full App Manager
- [ ] Multi Material Layouts
- [ ] CMS System
- [X] Authentication system(Security Feautures)
- [ ] Mail System(Support, Contact)

### Rb Manager Tutorial

##### Setup
Coming Sooon
##### Developing Server
./manage.rb run
##### Deploying Smoke Test
./manage.rb start

### Requirments
NodeJs 16.2.0 (14.0.0 +)
NPM
Yarn
MP2
Python3
Django3.2.0
Django-cors-header
Pillow
Ngin

## Manually Setup (Wait For Ruby App If U dont wanna config manually)
* $ cd backend
* $ pip3 install -r requirements
* $ cd ..
* $ cd frontend
* $ yarn
* $ npm -g install pm2
* $ cp ecosystem.config.js.sample ecosystem.config.js
* $ vi ecosystem.config.js # Enter UR Information :D
* $ pm2 start # Smoke test
* $ pm2 stop [AppName]
* $ cd ..
* $ cd WebServerCFG
* $ sudo cp WebApp.sample /etc/nginx/site-available/WebApp # Or every name u wanna name it
* $ sudo nano /etc/nginx/site-available/WebApp # Complete That With UR infos such as static/media dir
#### WllDown Finished

## Read These Wikis
1. [Nginx](https://nginx.com/)
2. [Django](https://www.djangoproject.com/)
3. [Gunicorn](https://gunicorn.org/)
4. [Nodejs](https://nodejs.org/)
5. [Yarn](https://yarnpkg.com/)
6. [PM2](https://pm2.keymetrics.io/)
7. [Nuxt](https://nuxtjs.org/)
8. [Vue](https://vuejs.org/)