import datetime
from pydantic import BaseModel
from .modelsORM import Status

class WorkshopAddDTO(BaseModel):
    master_id: int
    technique_id: int
    title: str
    dificulty: str
    duration: int
    fee: float
    status: Status

class WorkshopDTO(WorkshopAddDTO):
    id: int

class WorkshopMasterDTO(WorkshopDTO):
    master: "MasterDTO"

class WorkshopTechniqueDTO(WorkshopDTO):
    technique: "TechniqueDTO"

class WorkshopRelDTO(WorkshopDTO):
    master: "MasterDTO"
    technique: "TechniqueDTO"

class WorkshopSetsOfMaterialDTO(WorkshopDTO):
    sets_of_materials: list["SetOfMaterialDTO"]

class WorkshopSessionsDTO(WorkshopDTO):
    sessions: list["ScheduleDTO"]

class WorkshopAllRelDTO(WorkshopDTO):
    master: "MasterDTO"
    technique: "TechniqueDTO"
    sets_of_material: list["SetOfMaterialDTO"]
    sessions: list["ScheduleDTO"]

class SetOfMaterialDTO(BaseModel):
    workshop_id: int
    material_id: int
    quantity: int
    unit:str 
 
    material: "MaterialDTO"

    

class MaterialAddDTO(BaseModel):
    name: str
    discription: str
    cost: float
    type: str

class MaterialDTO(MaterialAddDTO):
    id: int

class MaterialRelDTO(MaterialDTO):
    set_of_material: "SetOfMaterialDTO"

class TechniqueAddDTO(BaseModel):
    name: str
    discription: str

class TechniqueDTO(TechniqueAddDTO):
    id: int

class TechniqueWorkshopsDTO(TechniqueDTO):
    workshops: list["WorkshopDTO"]

class MasterAddDTO(BaseModel):
    first_name: str
    last_name: str
    specialization: str
    expirience: int
    bio: str

class MasterDTO(MasterAddDTO):
    id: int

class MasterWorkshopsDTO(MasterDTO):
    workshops: list["WorkshopDTO"]

class UserAddDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    login: str
    psw: str
    admin: bool

class UserDTO(UserAddDTO):
    id: int

class ScheduleAddDTO(BaseModel):
    workshop_id: int
    date: datetime.datetime
    location: str
    numberOfSeats: int

class ScheduleDTO(ScheduleAddDTO):
    id: int

class ScheduleWorkhopDTO(ScheduleDTO):
    workshop: "WorkshopDTO"

class ScheduleOrdersDTO(ScheduleDTO):
    orders: list["OrderDTO"]

class OrderAddDTO(BaseModel):
    user_id: int
    schedule_id: int
    date: datetime.datetime
    status: Status

class OrderDTO(OrderAddDTO):
    id: int

class OrderSession(OrderDTO):
    session: "ScheduleDTO"