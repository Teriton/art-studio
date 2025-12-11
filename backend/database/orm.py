from database.database import async_engine, async_session_factory, Base
from database.modelsORM import (
    WorkshopORM, MasterORM, Status,
    TechniqueORM, SetOfMaterialORM, MaterialORM,
    ScheduleORM, UserORM, OrderORM, PaymentORM, PaymentMethod, PaymentStatus
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
                MasterORM(first_name="Vitaly", last_name="Antoshka", specialization="Танцы на стекле", expirience=30, bio="Покоритель подиумов и мастер боли. Любит чай с бергамотом.", image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.booska-p.com%2Fwp-content%2Fuploads%2F2014%2F11%2Fbrblockryder-reprends-hot-nigga-video-649.jpg&f=1&nofb=1&ipt=2ec66e194e9920b33e65d6ad0ff5de51a5640f5921e3385ae34954101bbab3c6"),
                MasterORM(first_name="Anton", last_name="Avl", specialization="Флиртология", expirience=32, bio="Профессор романтических наук. Может соблазнить даже Wi-Fi роутер.", image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F0c%2Fab%2Fe8%2F0cabe8036fe675e5bbfe1145c8f51e65.jpg&f=1&nofb=1&ipt=95dd68f1ebb3b5a680a18c90055b088ee8fa8b25e4818edc7a72577366ce9535"),
                MasterORM(first_name="Марго", last_name="Хрусталева", specialization="Мыть окна", expirience=12, bio="Крутая тётка, моет окна так, что птицы теряют ориентацию.", image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2Fd5%2Fb3%2Fb0%2Fd5b3b0c84c051d9e37dbaffb55d1b027.jpg&f=1&nofb=1&ipt=f4fbdf66696da46b6b991f9897a37e06c3d1a1a1087c17682766c5ce04282738"),
                MasterORM(first_name="Сергей", last_name="Пельменев", specialization="Кулинарный гипноз", expirience=20, bio="Готовит борщ, после которого люди начинают говорить по-французски.", image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffatboyjacked.com%2Fwp-content%2Fuploads%2F2023%2F09%2Foverweight-fat-man-sports-clothing-is-running-with-determination-striving-lose-fat-regain-vitality-ai-generated-scaled.jpg&f=1&nofb=1&ipt=5446cef89c1489d2f31cbad0612ccedf64b05a4ef80ece3f3cf72b7c3fa05406"),
                MasterORM(first_name="Люба", last_name="Звездная", specialization="Астропсихология", expirience=25, bio="Совмещает гороскопы с психоанализом. Знает, почему ты не отвечаешь на сообщения.", image=""),
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
                PaymentORM(user_id = 1, order_id = 1, status = PaymentStatus.unpaid ,fee =20.0, payment_method=PaymentMethod.card),
                PaymentORM(user_id = 1, order_id = 4, status = PaymentStatus.unpaid ,fee =20.0, payment_method=PaymentMethod.card)
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
            result_dto = [modelsDTO.MasterDTO.model_validate(row, from_attributes=True) for row in result_orm]
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
                status=PaymentStatus.unpaid,
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

    @staticmethod
    async def get_orders(user_id:int):
        async with async_session_factory() as session:
            stmt = (
                select(OrderORM)
                .options(joinedload(OrderORM.session).joinedload(ScheduleORM.workshop), joinedload(OrderORM.payment))
                .filter_by(user_id = user_id)
            )
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.OrderRelsDTO.model_validate(row, from_attributes=True) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto

    @staticmethod
    async def get_payments(user_id:int):
        async with async_session_factory() as session:
            stmt = (
                select(PaymentORM)
                .options(joinedload(PaymentORM.order).joinedload(OrderORM.session).joinedload(ScheduleORM.workshop))
                .filter_by(user_id = user_id)
            )
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.PaymentOrderDTO.model_validate(row, from_attributes=True) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto
        
    @staticmethod
    async def cancel_order(user_id: int, order_id: int) -> bool:
        async with async_session_factory() as session:
            # Находим платеж, принадлежащий пользователю и связанному с order_id
            stmt = (
                select(OrderORM)
                .where(
                    OrderORM.user_id == user_id,
                    OrderORM.id == order_id
                )
            )
            result = await session.execute(stmt)
            order = result.scalar_one_or_none()

            if order is None:
                return False  # Платёж не найден или не принадлежит пользователю

            await session.delete(order)
            await session.commit()
            return True
        

    @staticmethod
    async def get_payment_by_order(user_id: int, order_id: int) -> modelsDTO.PaymentDTO | None:
        async with async_session_factory() as session:
            stmt = (
                select(PaymentORM)
                .where(
                    PaymentORM.user_id == user_id,
                    PaymentORM.order_id == order_id
                )
            )
            result = await session.execute(stmt)
            result_orm = result.scalar_one_or_none()
            if not result_orm:
                return None
            print(f"{result_orm=}")
            result_dto = modelsDTO.PaymentDTO.model_validate(result_orm, from_attributes=True)
            print(f"{result_dto=}")
            return result_dto

    @staticmethod
    async def make_payment(user_id: int, order_id: int, payment_method: PaymentMethod) -> bool:
        async with async_session_factory() as session:
            # Находим платеж, принадлежащий пользователю и связанному с order_id
            stmt = (
                select(PaymentORM)
                .where(
                    PaymentORM.user_id == user_id,
                    PaymentORM.order_id == order_id
                )
                .with_for_update()  # Опционально: блокировка строки для избежания гонок
            )
            result = await session.execute(stmt)
            payment = result.scalar_one_or_none()

            if payment is None:
                return False  # Платёж не найден

            # Обновляем статус и способ оплаты
            payment.status = PaymentStatus.paid
            payment.payment_method = payment_method

            session.add(payment)
            await session.commit()
            return True
        
    @staticmethod
    async def get_users() -> list[modelsDTO.UserDTO]:
        async with async_session_factory() as session:
            stmt = select(UserORM)
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def delte_user(user_id: int) -> bool:
        async with async_session_factory() as session:
            user = await session.get(UserORM, user_id)
            
            if not user:
                return False
            
            await session.delete(user)
            await session.commit()
            return True
        
    @staticmethod
    async def get_workshops_admin() -> list[modelsDTO.WorkshopDTO]:
        async with async_session_factory() as session:
            stmt = select(WorkshopORM)
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.WorkshopDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def delte_master_admin(master_id: int) -> bool:
        async with async_session_factory() as session:
            master = await session.get(MasterORM, master_id)
            
            if not master:
                return False
            
            await session.delete(master)
            await session.commit()
            return True
        
    @staticmethod
    async def update_master_admin(master_id: int, master: modelsDTO.MasterAddDTO) -> bool:
        async with async_session_factory() as session:
            stmt = select(MasterORM).filter_by(id=master_id)
            res = await session.execute(stmt)
            master_orm = res.scalar_one_or_none()
            if not master_orm:
                return False
            
            master_orm.first_name = master.first_name
            master_orm.last_name = master.last_name
            master_orm.specialization = master.specialization
            master_orm.expirience = master.expirience
            master_orm.bio = master.bio
            master_orm.image = master.image

            await session.commit()

            return True
    
    @staticmethod
    async def add_master_admin(master: modelsDTO.MasterAddDTO):
        async with async_session_factory() as session:
            master_orm = MasterORM(
                first_name=master.first_name,
                last_name=master.last_name,
                specialization = master.specialization,
                expirience = master.expirience,
                bio = master.bio,
                image = master.image
            )
            session.add(master_orm)
            await session.commit()

            return True
        

    @staticmethod
    async def delte_workshop_admin(workshop_id: int) -> bool:
        async with async_session_factory() as session:
            workshop = await session.get(WorkshopORM, workshop_id)
            
            if not workshop:
                return False
            
            await session.delete(workshop)
            await session.commit()
            return True
        
    @staticmethod
    async def add_workshop_admin(workshop: modelsDTO.WorkshopAddDTO):
        async with async_session_factory() as session:
            workshop_orm = WorkshopORM(
                master_id = workshop.master_id,
                technique_id = workshop.technique_id,
                title = workshop.title,
                dificulty = workshop.dificulty,
                duration = workshop.duration,
                fee = workshop.fee,
                status = workshop.status
            )
            session.add(workshop_orm)
            await session.commit()

            return True
        
    @staticmethod
    async def get_techniques()  -> list[modelsDTO.TechniqueDTO]:
        async with async_session_factory() as session:
            stmt = select(TechniqueORM)
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.TechniqueDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def get_materials()  -> list[modelsDTO.MaterialDTO]:
        async with async_session_factory() as session:
            stmt = select(MaterialORM)
            res = await session.execute(stmt)
            result_orm = res.scalars().all()
            result_dto = [modelsDTO.MaterialDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def add_material_admin(material: modelsDTO.MaterialAddDTO):
        async with async_session_factory() as session:
            material_orm = MaterialORM(
                name = material.name,
                discription = material.discription,
                cost = material.cost,
                type = material.type

            )
            session.add(material_orm)
            await session.commit()
            await session.refresh(material_orm)
            result_dto = modelsDTO.MaterialDTO.model_validate(material_orm, from_attributes=True)

            return result_dto
        
    @staticmethod
    async def update_workshop_admin(workshop_id: int, workshop: modelsDTO.WorkshopAddDTO) -> bool:
        async with async_session_factory() as session:
            stmt = select(WorkshopORM).filter_by(id=workshop_id)
            res = await session.execute(stmt)
            workshop_orm = res.scalar_one_or_none()
            if not workshop_orm:
                return False
            
            workshop_orm.title = workshop.title
            workshop_orm.master_id = workshop.master_id
            workshop_orm.technique_id = workshop.technique_id
            workshop_orm.dificulty = workshop.dificulty
            workshop_orm.duration = workshop.duration
            workshop_orm.fee = workshop.fee
            workshop_orm.status = workshop.status

            await session.commit()

            return True
        
    @staticmethod
    async def add_set_of_material_admin(set_of_material: modelsDTO.SetOfMaterialRawDTO):
        async with async_session_factory() as session:
            set_of_material_orm = SetOfMaterialORM(
                workshop_id = set_of_material.workshop_id,
                material_id = set_of_material.material_id,
                quantity = set_of_material.quantity,
                unit = set_of_material.unit
            )
            session.add(set_of_material_orm)
            await session.commit()

            return True
        

    @staticmethod
    async def delte_set_of_material_admin(set_of_material: modelsDTO.SetOfMaterialRawDTO):
        async with async_session_factory() as session:
            set_of_material_orm = await session.get(
                SetOfMaterialORM,
                (set_of_material.workshop_id, set_of_material.material_id)
            )
            if not set_of_material_orm:
                return False
            
            await session.delete(set_of_material_orm)
            await session.commit()
            return True
        
    @staticmethod
    async def update_set_of_material_admin(set_of_material: modelsDTO.SetOfMaterialRawDTO) -> bool:
        async with async_session_factory() as session:
            set_of_material_orm = await session.get(
                SetOfMaterialORM,
                (set_of_material.workshop_id, set_of_material.material_id)
            )
            if not set_of_material_orm:
                return False
            
            set_of_material_orm.quantity = set_of_material.quantity
            set_of_material_orm.unit = set_of_material.unit

            await session.commit()

            return True
        
    @staticmethod
    async def add_session_admin(schedule: modelsDTO.ScheduleAddDTO):
        async with async_session_factory() as session:
            session_orm = ScheduleORM(
                workshop_id = schedule.workshop_id,
                date = schedule.date + timedelta(hours=3),
                location = schedule.location,
                numberOfSeats = schedule.numberOfSeats
            )
            session.add(session_orm)
            await session.commit()

            return True
        
    @staticmethod
    async def delte_session_admin(session_id: int) -> bool:
        async with async_session_factory() as session:
            session_orm = await session.get(ScheduleORM, session_id)
            
            if not session_orm:
                return False
            
            await session.delete(session_orm)
            await session.commit()
            return True
        
    @staticmethod
    async def update_session_admin(session_id: int, schedule: modelsDTO.ScheduleAddDTO) -> bool:
        async with async_session_factory() as session:
            stmt = select(ScheduleORM).filter_by(id=session_id)
            res = await session.execute(stmt)
            session_orm = res.scalar_one_or_none()
            if not session_orm:
                return False

            session_orm.date = schedule.date + timedelta(hours=3)
            session_orm.location =  schedule.location
            session_orm.numberOfSeats = schedule.numberOfSeats

            await session.commit()

            return True