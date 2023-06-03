from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar server:
# uvicorn users:app --reload
# uvicorn usersjson:app --reload


# ENTIDAD USER:
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


# Creamos lista usuarios:
users_list = [
    User(
        id=1, name="Jose", surname="Pascual", url="https://mouredev.com/python3", age=35
    ),
    User(id=2, name="Luis", surname="Ivarra", url="https://Ivarra.com/python3", age=25),
    User(
        id=3, name="Pedro", surname="Suarez", url="https://Suarez.com/python3", age=55
    ),
]
# users = [User()]


@app.get("/usersjson")
# Siempre que llamemos al servidor asimcronamente
async def usersjson():
    return [
        {
            "name": "Jose",
            "surname": "Pascual",
            "url": "https://mouredev.com/python3",
            "age": 35,
        },
        {
            "name": "Luis",
            "surname": "Ivarra",
            "url": "https://Ivarra.com/python3",
            "age": 25,
        },
        {
            "name": "Pedro",
            "surname": "Suarez",
            "url": "https://Suarez.com/python3",
            "age": 55,
        },
    ]


@app.get("/users")
# Siempre que llamemos al servidor asimcronamente
async def users():
    return users_list


# PATH
@app.get("/user/{id}")
# Siempre que llamemos al servidor asimcronamente
async def user(id: int):
    return search_user(id)


# QUERY
@app.get("/user/")
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El ususario ya existe"}
    else:
        users_list.append(user)



def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


# Para ejecutar en thunder client:
# ERROR:
# http://127.0.0.1:8000/userquery/?id=brais
# POR ID:
# http://127.0.0.1:8000/userquery/?id=1



