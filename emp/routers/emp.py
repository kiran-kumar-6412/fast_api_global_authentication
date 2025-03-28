from fastapi import APIRouter,Depends,status,HTTPException
from .. import database,schemas,Oauth2
from sqlalchemy.orm import Session
from ..crud import emp,user

router=APIRouter(
    tags=["Emp"]
)

get_db=database.get_db

@router.get("/empdata")
def emp_data(db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return emp.emp_list(db)

@router.post("/emp",status_code=status.HTTP_201_CREATED)
def create_emp(request:schemas.Emp,db:Session=Depends(get_db)):
    return emp.create_emp(request,db)


@router.get("/emp/{id}", response_model=schemas.Show_emp)
def emp_filter(id: int, db: Session = Depends(get_db)):
    return emp.filter_emp(db,id)  # Use emp_data instead of emp
    # return emp_data


@router.delete("/emp/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete(id,db:Session=Depends(get_db)):
    return emp.emp_delete(id,db)


@router.put("/empupdate/{id}")
def update(id,request1:schemas.Emp,db:Session=Depends(get_db)):
    return emp.emp_update(id,db,request1)
    
    
    