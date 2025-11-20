from database.database import async_engine, async_session_factory, Base
from database.modelsORM import (
    WorkshopORM, MasterORM, Status,
    TechniqueORM, SetOfMaterialORM, MaterialORM,
    ScheduleORM, UserORM, OrderORM, PaymentORM, PaymentMethod
    )
from datetime import * # type: ignore
from sqlalchemy import select, func
from sqlalchemy.orm import joinedload, selectinload
from . import modelsDTO

class AsyncORM:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_starting_data():
        async with async_session_factory() as session:
            masters = [
                MasterORM(first_name="Vitaly", last_name="Antoshka", specialization="Танцы на стекле", expirience=30, bio="Покоритель подиумов и мастер боли. Любит чай с бергамотом."),
                MasterORM(first_name="Anton", last_name="Avl", specialization="Флиртология", expirience=32, bio="Профессор романтических наук. Может соблазнить даже Wi-Fi роутер."),
                MasterORM(first_name="Марго", last_name="Хрусталева", specialization="Мыть окна", expirience=12, bio="Крутая тётка, моет окна так, что птицы теряют ориентацию."),
                MasterORM(first_name="Сергей", last_name="Пельменев", specialization="Кулинарный гипноз", expirience=20, bio="Готовит борщ, после которого люди начинают говорить по-французски."),
                MasterORM(first_name="Люба", last_name="Звездная", specialization="Астропсихология", expirience=25, bio="Совмещает гороскопы с психоанализом. Знает, почему ты не отвечаешь на сообщения."),
            ]

            techniques = [
                TechniqueORM(name="Painting", discription="Use your arms to do somw fisting"),
                TechniqueORM(name="Волейбол", discription="Вкусно и грустно"),
                TechniqueORM(name="Масляная живопись", discription="Классическая техника живописи масляными красками"),
                TechniqueORM(name="Гончарное дело", discription="Работа с глиной на гончарном круге"),
                TechniqueORM(name="Аналоговая фотография", discription="Съемка на пленку и ручная проявка"),
                TechniqueORM(name="Батик", discription="Техника росписи по ткани с использованием резервирующего состава"),
                TechniqueORM(name="Каллиграфия", discription="Искусство красивого письма пером и тушью"),
                TechniqueORM(name="Лепка из глины", discription="Создание объемных фигур из глины ручным способом"),
                TechniqueORM(name="Акварельная живопись", discription="Техника живописи водорастворимыми красками"),
                TechniqueORM(name="Скульптура", discription="Создание объемных художественных произведений"),
                TechniqueORM(name="Графика", discription="Искусство рисунка карандашом, углем, тушью"),
                TechniqueORM(name="Пастель", discription="Рисование сухими и масляными пастельными мелками"),
            ]
            workshops = [
                WorkshopORM(master_id=1, technique_id=1, title="Perfaracia", dificulty="Bolno", duration=120, fee=120.0, status=Status.active),
                WorkshopORM(master_id=2, technique_id=2, title="Мячик бегает вертится крутитстя тебя пиздит", dificulty="Весело", duration=5, fee=99.0, status=Status.active),
                WorkshopORM(master_id=3, technique_id=3, title="Масляная живопись для начинающих", dificulty="Начальный", duration=180, fee=250.0, status=Status.active),
                WorkshopORM(master_id=4, technique_id=4, title="Гончарное искусство", dificulty="Средний", duration=240, fee=350.0, status=Status.active),
                WorkshopORM(master_id=5, technique_id=5, title="Фотография на пленку", dificulty="Продвинутый", duration=120, fee=200.0, status=Status.active),
                WorkshopORM(master_id=1, technique_id=6, title="Батик: роспись по шелку", dificulty="Средний", duration=210, fee=280.0, status=Status.active),
                WorkshopORM(master_id=2, technique_id=7, title="Каллиграфия пером", dificulty="Начальный", duration=90, fee=150.0, status=Status.active),
                WorkshopORM(master_id=3, technique_id=8, title="Семейный мастер-класс по лепке", dificulty="Легкий", duration=120, fee=180.0, status=Status.active),
                WorkshopORM(master_id=4, technique_id=9, title="Детская акварель", dificulty="Детский", duration=60, fee=100.0, status=Status.active),
                WorkshopORM(master_id=5, technique_id=10, title="Скульптура из проволоки", dificulty="Сложный", duration=300, fee=420.0, status=Status.canceled),
                WorkshopORM(master_id=1, technique_id=11, title="Продвинутая графика", dificulty="Продвинутый", duration=150, fee=320.0, status=Status.unactive),
            ]
            setsofmaterials = [
                SetOfMaterialORM(workshop_id=1, material_id=1, quantity=123, unit="shtuka"),
                SetOfMaterialORM(workshop_id=1, material_id=2, quantity=12, unit="shtuka"),
                SetOfMaterialORM(workshop_id=2, material_id=3, quantity=50, unit="shtuka"),
                SetOfMaterialORM(workshop_id=3, material_id=4, quantity=5, unit="nabor"),
                SetOfMaterialORM(workshop_id=3, material_id=5, quantity=10, unit="bank"),
                SetOfMaterialORM(workshop_id=4, material_id=6, quantity=25, unit="kg"),
                SetOfMaterialORM(workshop_id=4, material_id=7, quantity=1, unit="shtuka"),
                SetOfMaterialORM(workshop_id=5, material_id=8, quantity=36, unit="rulon"),
                SetOfMaterialORM(workshop_id=5, material_id=9, quantity=3, unit="bank"),
                SetOfMaterialORM(workshop_id=6, material_id=10, quantity=15, unit="meter"),
                SetOfMaterialORM(workshop_id=6, material_id=11, quantity=8, unit="shtuka"),
                SetOfMaterialORM(workshop_id=7, material_id=12, quantity=20, unit="shtuka"),
                SetOfMaterialORM(workshop_id=8, material_id=13, quantity=40, unit="kg"),
                SetOfMaterialORM(workshop_id=9, material_id=14, quantity=30, unit="shtuka"),
                SetOfMaterialORM(workshop_id=10, material_id=15, quantity=100, unit="meter"),
            ]

            materials = [
                MaterialORM(name="Kistochka", discription="Palka s volosami", cost=2.22, type="Atomnaya bomba"),
                MaterialORM(name="Sharik", discription="Ochen krugli", cost=3.44, type="Atomnaya bomba"),
                MaterialORM(name="Волейбольный мяч", discription="Стандартный волейбольный мяч", cost=45.50, type="Спортивный инвентарь"),
                MaterialORM(name="Набор масляных красок", discription="Базовый набор из 12 цветов", cost=120.0, type="Художественные материалы"),
                MaterialORM(name="Разбавитель для масляных красок", discription="Специальный растворитель", cost=25.0, type="Химия"),
                MaterialORM(name="Глина для лепки", discription="Обожженная глина 5кг", cost=15.75, type="Сырье"),
                MaterialORM(name="Гончарный круг", discription="Электрический гончарный круг", cost=2500.0, type="Оборудование"),
                MaterialORM(name="Фотопленка 35mm", discription="Черно-белая фотопленка", cost=8.90, type="Фотоматериалы"),
                MaterialORM(name="Проявитель для пленки", discription="Химический раствор", cost=12.30, type="Химия"),
                MaterialORM(name="Шелковая ткань", discription="Натуральный шелк для батика", cost=45.0, type="Текстиль"),
                MaterialORM(name="Резервирующий состав", discription="Состав для контуров в батике", cost=18.50, type="Химия"),
                MaterialORM(name="Каллиграфическое перо", discription="Перо с держателем", cost=15.0, type="Инструмент"),
                MaterialORM(name="Детская глина", discription="Безопасная глина для детей", cost=8.25, type="Сырье"),
                MaterialORM(name="Акварельные краски", discription="Набор детских акварельных красок", cost=35.0, type="Художественные материалы"),
                MaterialORM(name="Алюминиевая проволока", discription="Гибкая проволока для скульптур", cost=3.20, type="Металл"),
            ]
            schedules = [
                # Текущие даты
                ScheduleORM(workshop_id=1, date=datetime.now(), location="Шпэкляндия", numberOfSeats=21),
                ScheduleORM(workshop_id=1, date=datetime.now() + timedelta(minutes=120), location="Шпэкляндия", numberOfSeats=21),
                ScheduleORM(workshop_id=2, date=datetime.now() + timedelta(hours=3), location="Творческая мастерская", numberOfSeats=15),
                ScheduleORM(workshop_id=3, date=datetime.now() + timedelta(days=1), location="Арт-пространство", numberOfSeats=30),
                
                # Исторические даты
                ScheduleORM(workshop_id=1, date=datetime(2002, 8, 2, 16, 22, 2), location="Школьники", numberOfSeats=21),
                ScheduleORM(workshop_id=1, date=datetime(2002, 8, 2, 12, 22, 2), location="Школьники", numberOfSeats=21),
                ScheduleORM(workshop_id=2, date=datetime(2023, 5, 15, 14, 0, 0), location="Дворец культуры", numberOfSeats=25),
                ScheduleORM(workshop_id=3, date=datetime(2023, 6, 20, 11, 30, 0), location="Галерея искусств", numberOfSeats=18),
                
                # Будущие даты
                ScheduleORM(workshop_id=4, date=datetime(2024, 2, 15, 10, 0, 0), location="Центр современного искусства", numberOfSeats=20),
                ScheduleORM(workshop_id=5, date=datetime(2024, 3, 1, 16, 45, 0), location="Молодежный центр", numberOfSeats=35),
                ScheduleORM(workshop_id=6, date=datetime(2024, 3, 10, 13, 15, 0), location="Библиотека им. Ленина", numberOfSeats=12),
                ScheduleORM(workshop_id=7, date=datetime(2024, 4, 5, 9, 0, 0), location="Парк культуры", numberOfSeats=50),
                
                # Несколько расписаний в один день
                ScheduleORM(workshop_id=2, date=datetime(2024, 2, 20, 10, 0, 0), location="Творческая мастерская", numberOfSeats=15),
                ScheduleORM(workshop_id=2, date=datetime(2024, 2, 20, 14, 0, 0), location="Творческая мастерская", numberOfSeats=15),
                ScheduleORM(workshop_id=2, date=datetime(2024, 2, 20, 18, 0, 0), location="Творческая мастерская", numberOfSeats=15),
                
                # Выходные дни
                ScheduleORM(workshop_id=8, date=datetime(2024, 2, 17, 11, 0, 0), location="Семейный центр", numberOfSeats=40),
                ScheduleORM(workshop_id=9, date=datetime(2024, 2, 18, 15, 30, 0), location="Детский клуб", numberOfSeats=25),
            ]
            users = [
                UserORM(first_name="Piter",last_name="Pan", email="ghosha@sosal.da", phone_number="+1234", admin=False, login = "pidr", psw="$argon2id$v=19$m=65536,t=3,p=4$9EmBZZ/svu/BFoZLMwQ7sw$a2vZxkTGsd0vfdu/RbORlpgc8GEEsDOjPY0HBf3i9Og"),
                UserORM(first_name="Spack",last_name="Vlad", email="ghosha@sosal.da", phone_number="+1234", admin=False, login = "anton", psw="$argon2id$v=19$m=65536,t=3,p=4$9EmBZZ/svu/BFoZLMwQ7sw$a2vZxkTGsd0vfdu/RbORlpgc8GEEsDOjPY0HBf3i9Og"),
                UserORM(first_name="Ponchik",last_name="Ploski", email="ghosha@sosal.da", phone_number="+1234", admin=False, login = "zxc", psw="$argon2id$v=19$m=65536,t=3,p=4$9EmBZZ/svu/BFoZLMwQ7sw$a2vZxkTGsd0vfdu/RbORlpgc8GEEsDOjPY0HBf3i9Og"),
                UserORM(first_name="Admin",last_name="Admin", email="hui@sosal.da", phone_number="+1234", admin=True, login = "pidoras", psw="$argon2id$v=19$m=65536,t=3,p=4$9EmBZZ/svu/BFoZLMwQ7sw$a2vZxkTGsd0vfdu/RbORlpgc8GEEsDOjPY0HBf3i9Og"),
            ]                                                                                                                  
            orders = [
                OrderORM(user_id = 1, schedule_id = 1, status= Status.active ),
                OrderORM(user_id = 2, schedule_id = 1, status= Status.active ),
                OrderORM(user_id = 3, schedule_id = 1, status= Status.active ),
                OrderORM(user_id = 1, schedule_id = 2, status= Status.active ),
                OrderORM(user_id = 2, schedule_id = 2, status= Status.active ),
                OrderORM(user_id = 3, schedule_id = 2, status= Status.active ),
            ]
            payments = [
                PaymentORM(user_id = 1, order_id = 1, status = Status.active ,fee =20.0, payment_method=PaymentMethod.card)
            ]
            session.add_all(masters)
            session.add_all(techniques)
            session.add_all(workshops)
            session.add_all(materials)
            await session.flush()
            session.add_all(setsofmaterials)
            session.add_all(schedules)
            session.add_all(users)
            await session.flush()
            session.add_all(orders)
            session.add_all(payments)
            await session.commit()

    @staticmethod
    async def get_closest_workshop():
        async with async_session_factory() as session:
            stmt = (
                select(WorkshopORM)
                .options(joinedload(WorkshopORM.master))
                .join(ScheduleORM, WorkshopORM.id == ScheduleORM.workshop_id)
                .order_by(ScheduleORM.date)
                .limit(1)
            )
            res = await session.execute(stmt)
            result = res.scalar_one_or_none()
            if result is None:
                # no upcoming workshop found
                return None
            result_dto = modelsDTO.WorkshopMasterDTO.model_validate(result, from_attributes=True)
            # Return a plain dict to avoid returning ORM/Pydantic model instances directly to FastAPI
            # (this prevents accidental lazy-loading or serialization issues)
            return result_dto
        
    @staticmethod
    async def get_all_masters():
        async with async_session_factory() as session:
            stmt = select(MasterORM)
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.MasterDTO.model_validate(row, from_attributes=True).model_dump() for row in result_orm]
            return result_dto
        
    @staticmethod
    async def get_user_by_credentials(login: str, password: str) -> modelsDTO.UserDTO | None:
        async with async_session_factory() as session:
            stmt = (
                select(UserORM).filter_by(login = login, psw = password)
                    )
            res = await session.execute(stmt)
            result = res.scalar_one_or_none()
            if not result:
                return None
            result_dto = modelsDTO.UserDTO.model_validate(result, from_attributes=True)
            print(f"{result_dto=}")
            return result_dto
        
    @staticmethod
    async def get_user_by_login(login: str | None) -> modelsDTO.UserDTO | None:
        async with async_session_factory() as session:
            stmt = (
                select(UserORM).filter_by(login = login)
            )   
            res = await session.execute(stmt)
            result = res.scalar_one_or_none()
            if not result:
                return None
            result_dto = modelsDTO.UserDTO.model_validate(result, from_attributes=True)
            print(result_dto)
            return result_dto
        
    @staticmethod
    async def add_user(user_add_dto: modelsDTO.UserAddDTO) -> modelsDTO.UserDTO:
        async with async_session_factory() as session:
            user_orm = UserORM(
                first_name=user_add_dto.first_name,
                last_name=user_add_dto.last_name,
                email=user_add_dto.email,
                phone_number=user_add_dto.phone_number,
                admin=False,
                login=user_add_dto.login,
                psw=user_add_dto.psw
            )
            session.add(user_orm)
            await session.commit()
            await session.refresh(user_orm)
            user_dto = modelsDTO.UserDTO.model_validate(user_orm, from_attributes=True)
            return user_dto
        
    @staticmethod
    async def update_user_info(user_id: int, updated_user_dto: modelsDTO.UserAddDTO) -> modelsDTO.UserDTO | None:
        async with async_session_factory() as session:
            stmt = select(UserORM).filter_by(id=user_id)
            res = await session.execute(stmt)
            user_orm = res.scalar_one_or_none()
            if not user_orm:
                return None
            user_orm.first_name = updated_user_dto.first_name
            user_orm.last_name = updated_user_dto.last_name
            user_orm.email = updated_user_dto.email
            user_orm.phone_number = updated_user_dto.phone_number
            await session.commit()
            await session.refresh(user_orm)
            user_dto = modelsDTO.UserDTO.model_validate(user_orm, from_attributes=True)
            return user_dto
        
    @staticmethod
    async def get_workshops():
        async with async_session_factory() as session:
            stmt = (
                select(WorkshopORM)
                .options(joinedload(WorkshopORM.master), joinedload(WorkshopORM.technique))
                # .join(ScheduleORM, WorkshopORM.id == ScheduleORM.workshop_id)
                # .order_by(ScheduleORM.date)
            )
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.WorkshopRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto
        
    @staticmethod
    async def get_workshop_with_sessions(workshop_id: int):
        async with async_session_factory() as session:
            stmt = (
                select(WorkshopORM)
                .options(
                    joinedload(WorkshopORM.master),
                    joinedload(WorkshopORM.technique),
                    selectinload(WorkshopORM.sessions),
                    # eager-load sets_of_material and the related material to avoid lazy IO
                    selectinload(WorkshopORM.sets_of_material).joinedload(SetOfMaterialORM.material),
                )
                .filter_by(id =workshop_id)
            )
            res = await session.execute(stmt)
            result_orm = res.scalar_one_or_none()
            if not result_orm:
                return None
            print(f"{result_orm=}")
            result_dto = modelsDTO.WorkshopAllRelDTO.model_validate(result_orm, from_attributes=True)
            print(f"{result_dto=}")
            return result_dto
        
    @staticmethod
    async def get_avalable_seats(session_id: int) -> modelsDTO.ScheduleOrdersDTO | None:
        async with async_session_factory() as session:
            stmt = (
                select(ScheduleORM)
                .options(selectinload(ScheduleORM.orders))
                .filter_by(id = session_id)
            )
            res = await session.execute(stmt)
            result_orm = res.scalar_one_or_none()
            if not result_orm:
                return None
            print(f"{result_orm=}")
            result_dto = modelsDTO.ScheduleOrdersDTO.model_validate(result_orm, from_attributes=True)
            print(f"{result_dto=}")
            return result_dto
        
    @staticmethod
    async def bookSession(session_id: int, user_id: int) -> dict:
        async with async_session_factory() as session:
            stmt_schedule = (
                select(ScheduleORM)
                .options(
                    joinedload(ScheduleORM.workshop),
                    selectinload(ScheduleORM.orders)
                )
                .filter_by(id=session_id)
            )
            res_schedule = await session.execute(stmt_schedule)
            schedule_orm = res_schedule.scalar_one_or_none()
            print(f"SESSION: {schedule_orm}")
            
            if not schedule_orm:
                print(f"No available seats in schedule {session_id}")
                raise ValueError(f"Schedule with id {session_id} not found")
            
            # Check available seats
            occupied_seats = len(schedule_orm.orders)
            available_seats = schedule_orm.numberOfSeats - occupied_seats
            
            if available_seats <= 0:
                print(f"No available seats in schedule {session_id}")
                raise ValueError(f"No available seats in schedule {session_id}")

            # Get workshop fee
            workshop_fee = schedule_orm.workshop.fee
            
            # Create order and payment in single transaction
            order = OrderORM(
                user_id=user_id,
                schedule_id=session_id,
                date=datetime.now(),
                status=Status.active
            )
            session.add(order)
            await session.flush()  # Flush to get order.id without committing
            
            payment = PaymentORM(
                user_id=user_id,
                order_id=order.id,
                status=Status.active,
                fee=workshop_fee,
                payment_method=PaymentMethod.card 
            )

            session.add(payment)
            order_id = order.id
            await session.flush()   
            payment_id = payment.id
            await session.commit()
            
            return {
                # "order_id": order.id,
                # "payment_id": payment.id,
                "order_id": order_id,
                "payment_id": payment_id,
            }