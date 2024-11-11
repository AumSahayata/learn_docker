from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.person.person_data import data
from src.person.model import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Person])
async def get_all_people():
    return data


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_people(person_data: Person) -> dict:
    new_person = person_data.model_dump()

    data.append(new_person)
    return new_person


@router.get("/{id}")
async def get_person(id: int) -> dict:
    for person in data:
        if id == person["id"]:
            return person

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
    )


@router.patch("/{id}")
async def update_person(id: int, person_update_data:PersonUpdateModel) -> dict:
    
    for person in data:
        if id == person['id']:
            person['name'] = person_update_data.name
            person['phone'] = person_update_data.phone
            person['email'] = person_update_data.email
            person['region'] = person_update_data.region
            person['country'] = person_update_data.country
            
            return person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Person not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(id:int):
    
    for person in data:
        if id == person['id']:
            data.remove(person)
            
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Person not found")

