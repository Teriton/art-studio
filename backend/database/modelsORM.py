from typing import Annotated
import datetime
import enum
from typing import Annotated, Optional
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text, CheckConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from sqlalchemy import Enum as SQLEnum

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))] 
updateds_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate= datetime.datetime.utcnow
    )]

class Status(enum.Enum):
    active = "активный"
    unactive = "неактивный"
    canceled = "отмененный"

class PaymentMethod(enum.Enum):
    card = "карта"
    cash = "налик"

class MasterORM(Base):
    __tablename__= "masters"

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    specialization: Mapped[str]
    expirience: Mapped[int]
    bio: Mapped[str]

    workshops: Mapped[list["WorkshopORM"]] = relationship(
        back_populates="master"
    )

class WorkshopORM(Base):
    __tablename__ = "workshops"

    id: Mapped[intpk]
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id", ondelete="CASCADE"))
    technique_id: Mapped[int] = mapped_column(ForeignKey("techniques.id", ondelete="CASCADE"))
    title: Mapped[str]
    dificulty: Mapped[str]
    duration: Mapped[int]
    fee: Mapped[float]
    status: Mapped[Status] = mapped_column(SQLEnum(Status, name="status"))

    master: Mapped["MasterORM"] = relationship(
        back_populates="workshops"
    )

    technique: Mapped["TechniqueORM"] = relationship(
        back_populates="workshops"
    )

    sets_of_material: Mapped[list["SetOfMaterialORM"]] = relationship(
        back_populates="workshop"
    )

    sessions: Mapped[list["ScheduleORM"]] = relationship(
        back_populates="workshop"
    )

class TechniqueORM(Base):
    __tablename__ = "techniques"

    id: Mapped[intpk]
    name: Mapped[str]
    discription: Mapped[str]

    workshops: Mapped[list["WorkshopORM"]] = relationship(
        back_populates="technique"
    )

class SetOfMaterialORM(Base):
    __tablename__ = "setsOfMaterials"

    workshop_id: Mapped[int] = mapped_column(
        ForeignKey("workshops.id", ondelete="CASCADE"),
        primary_key=True,
        )
    material_id: Mapped[int] = mapped_column(
        ForeignKey("materials.id", ondelete="CASCADE"),
        primary_key=True,
        )
    quantity: Mapped[int]
    unit: Mapped[str]

    workshop: Mapped["WorkshopORM"] = relationship(
        back_populates="sets_of_material"
    )
 
    material: Mapped["MaterialORM"] = relationship(
        back_populates="set_of_material"
    )

    

class MaterialORM(Base):
    __tablename__ = "materials"

    id: Mapped[intpk]
    name: Mapped[str]
    discription: Mapped[str]
    cost: Mapped[float]
    type: Mapped[str]

    set_of_material: Mapped["SetOfMaterialORM"] = relationship(
        back_populates="material"
    )

class ScheduleORM(Base):
    __tablename__ = "schedule"

    id: Mapped[intpk]
    workshop_id: Mapped[int] = mapped_column(ForeignKey("workshops.id", ondelete="CASCADE"))
    date: Mapped[datetime.datetime]
    location: Mapped[str]
    numberOfSeats: Mapped[int]

    workshop: Mapped["WorkshopORM"] = relationship(
        back_populates="sessions",
    )

    orders: Mapped[list["OrderORM"]] = relationship(
        back_populates="session"
    )

class OrderORM(Base):
    __tablename__ = "orders"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id", ondelete="CASCADE"))
    date: Mapped[created_at]
    status: Mapped[Status] = mapped_column(SQLEnum(Status, name="status"))

    session: Mapped["ScheduleORM"] = relationship(
        back_populates="orders"
    )

    payment: Mapped["PaymentORM"] = relationship(
        back_populates="order"
    )


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]
    login: Mapped[str]
    psw: Mapped[str]
    admin: Mapped[bool] 

    payments: Mapped[list["PaymentORM"]] = relationship(
        back_populates="user"
    )


class PaymentORM(Base):
    __tablename__ = "payments"

    id: Mapped[intpk] 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"))
    status: Mapped[Status] = mapped_column(SQLEnum(Status, name="status"))
    fee: Mapped[float]
    payment_method: Mapped[PaymentMethod] = mapped_column(SQLEnum(PaymentMethod, name="paymentmethod"))

    user: Mapped["UserORM"] = relationship(
        back_populates="payments"
    )

    order: Mapped["OrderORM"] = relationship(
        back_populates="payment"
    )



