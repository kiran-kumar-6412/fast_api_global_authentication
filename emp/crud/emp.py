from ..repository import models
from ..repository import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException,status




def emp_list(db:Session):  #db type = Session
    emp=db.query(models.Emp).all()
    return emp

def create_emp(request:schemas.Emp,db:Session):
    new_emp=models.Emp(emp_name=request.emp_name,emp_phone=request.emp_phone,emp_age=request.emp_age)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp



def filter_emp(db: Session, id: int):
    emp = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with ID {id} not found")
    return emp


# def emp_delete(id:int,db:Session):
#     emp=db.query(models.Emp).filter(models.Emp.id==id)
#     if not emp.first():
#         raise HTTPException(status.HTTP_404_NOT_FOUND,f"emp with {id} not found on db")
#     emp.delete(synchronize_session=False)
#     db.commit()
#     return {f"deleted employee her id {id}"}


def emp_delete(id: int, db: Session):
    emp = db.query(models.Emp).filter(models.Emp.id == id).first()
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with ID {id} not found in the database")
    
    db.query(models.Emp).filter(models.Emp.id == id).delete(synchronize_session=False)
    db.commit()
    
    return {"message": f"Employee with ID {id} has been successfully deleted"}

def emp_update(id: int, db: Session, request1: schemas.Emp):
    emp_query = db.query(models.Emp).filter(models.Emp.id == id)
    emp = emp_query.first()
    
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with ID {id} not found")
    
    emp_query.update(
        {
            "emp_name": request1.emp_name,
            "emp_age": request1.emp_age
        }, synchronize_session=False
    )

    db.commit()
    db.refresh(emp)  # Refreshing to get the updated data
    
    return {"message": "Employee updated successfully", "updated_employee": emp}
