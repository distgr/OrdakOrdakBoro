# <img width="40" src="https://github.com/ThisIsMatin/OrdakOrdakBoro/raw/main/frontend/static/img/ordak_logo2.png" alt="OrdakOrdakBoro Logo"> [OrdakOrdakBoro!](#)
<img src='https://img.shields.io/badge/Testing-passing-green?logo=github' alt='' /> <img src='https://img.shields.io/badge/Python-ffd343?logo=python' alt='' /> <img src='https://img.shields.io/badge/Docker-blue?logo=Docker' alt='' /> <img src='https://img.shields.io/badge/MongoDB-3f3e42?logo=mongodb' alt='' /> <img src='https://img.shields.io/badge/Django-092e20?logo=Django' alt='' />

OrdakOrdakBoro is a persian fun project and a Google-based search engine that does not care about your privacy and stores your information and that of others.

Our policy is simple: OrdakOrdakBoro stores your searched information (such as device name, searched query, time/date of search and your IP in secret) and provides your information to everyone for 24 hours!

## Qucik setup
1. Rename the `example.env` file to `.env`
2. Make a secret key for the project and put it in .env
3. Create a volume in docker using `docker volume create {vol}`
4. Build the project using `docker-compose`
5. Run the project using `docker` and set the created volume to it

## Contributing
This project is under GNU GPLv3 license and contributing in this project has no special rules. This project uses MongoDb and Docker. If you have problems with Docker or other problems, you can change the database to a easier database (such as sqlite3).