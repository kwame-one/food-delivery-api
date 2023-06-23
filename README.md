## FOOD DELIVERY API

---

### Software Requirements

1. Python 3.9.6
2. MySQL Server

---

### Instructions
1. Clone the repository
2. Make a copy of **.env.example** in the root directory and save it as **.env in the root directory**
3. Configure the database name and password in the **.env** file as below
```dotenv
DB_HOST=
DB_USER=
DB_PORT=
DB_PASSWORD=
DB_NAME=
APP_ENV=local
APP_DEBUG=True
SECRET_KEY=any_random_str
JWT_SECRET_KEY=any_random_str
```
4. Open alembic/alembic.ini file and update necessary values in the line below
```ini
sqlalchemy.url = mysql://your_db_username:your_db_password@your_db_host:your_db_port/your_db_name
```
---

### Commands
Open a terminal in the project's root directory and run the following commands 
1. Create a virtual environment
```shell
python -m venv path_to_virutal_env
```
2. Activate virtual environment
Unix
```shell
source path_to_virutal_env/bin/activate 
```
Windows (command prompt)
```shell
source path_to_virutal_env\bin\activate.bat
```
3. Install dependencies
```shell
pip install -r requirements.txt
```
4. Run migrations
```shell
cd alembic 
alembic upgrade head
cd ..
```
5. Seed data
```shell
flask seed db
```
6. Run application
```shell
flask run
```
---

### API Documentation
1. Click [here](http://localhost:8000/api/documentation) to view the API documentation

---

### Sample Credentials
1. Email: ***super@admin.com***, Password: ***password***
2. All restaurant registrations approved have a default password of ***password***

