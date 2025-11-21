from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from database.orm import AsyncORM
from database import modelsDTO
from typing import Annotated
from models import Token
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token, get_current_active_user, get_current_active_user_login, get_token_from_request, password_hash

def create_fastapi_app():
    app = FastAPI(title="FastAPI")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5173"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
        
    @app.get("/workshopClosest", tags=["Мастерклассы"])
    async def get_closest_workshop():
        workshop = await AsyncORM.get_closest_workshop()
        return workshop
     
    @app.get("/workshops", tags=["Мастерклассы"])
    async def get_workshops(
        res: Annotated[str ,Depends(get_current_active_user_login)]
    ):
        workshops = await AsyncORM.get_workshops()
        return workshops
    
    @app.get("/workshop/{workshop_id}", tags=["Мастерклассы"])
    async def get_workshop_by_id(
        workshop_id: int,
    ):
        workshop = await AsyncORM.get_workshop_with_sessions(workshop_id)
        if workshop == None:
            return {"message":"workshop not found"}
        return workshop

    @app.get("/orders", tags=["Заказы"])
    async def get_orders(
        current_user: Annotated[str ,Depends(get_current_active_user)]
    ):
        orders = await AsyncORM.get_orders(current_user.id)
        return orders
    @app.get("/payments", tags=["Заказы"])
    async def get_payments(
        current_user: Annotated[str ,Depends(get_current_active_user)]
    ):
        payments = await AsyncORM.get_payments(current_user.id)
        return payments
    
    @app.get("/bookWorkshop", tags=["Мастерклассы"])
    async def book_session(
        res: Annotated[str ,Depends(get_current_active_user_login)]
    ):
        workshops = await AsyncORM.get_workshops()
        return workshops
    
    @app.get("/masters", tags=["Мастера"])
    async def get_masters():
        masters = await AsyncORM.get_all_masters()
        return masters
    
    @app.post("/token")
    async def login_for_acess_token(
        form_data: Annotated[OAuth2PasswordRequestForm,Depends()],
    ):
        user: modelsDTO.UserDTO | bool = await authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        acess_token_exprice = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        acess_token = create_access_token(data={"sub": user.login},expires_delta=acess_token_exprice ) # type: ignore
        # response = JSONResponse(jsonable_encoder(Token(access_token=acess_token,token_type="bearer")))
        response = JSONResponse({"ok": True})
        response.set_cookie(
            key="access_token",
            value=acess_token,
            expires=acess_token_exprice, # type: ignore
            httponly=True,
            samesite="lax"
        )
        return response

    @app.get("/login")
    async def login_test(login: str, psw: str):
        print(password_hash.hash(psw))
        if not password_hash.verify(psw, "$argon2id$v=19$m=65536,t=3,p=4$9EmBZZ/svu/BFoZLMwQ7sw$a2vZxkTGsd0vfdu/RbORlpgc8GEEsDOjPY0HBf3i9Og"):
            raise HTTPException(status_code=400, detail="User not found")
        user = await AsyncORM.get_user_by_login(login)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        return user
    
    @app.post("/logout")
    async def logout():
        response = JSONResponse({"ok": True})
        response.delete_cookie("access_token")
        return response
    
    @app.post("/signup")
    async def signup(user: modelsDTO.UserAddDTO):
        existing_user = await AsyncORM.get_user_by_login(user.login)
        if existing_user:
            raise HTTPException(status_code=400, detail="Login already registered")
        user.psw = password_hash.hash(user.psw)
        new_user = await AsyncORM.add_user(user)
        return new_user


    @app.get("/user/info")
    async def user_info(
        current_user: Annotated[modelsDTO.UserDTO,Depends(get_current_active_user)]
    ):
        return current_user

    @app.put("/user/updateInfo")
    async def update_user(
        updated_user: modelsDTO.UserAddDTO,
        current_user: Annotated[modelsDTO.UserDTO,Depends(get_current_active_user)]
    ):
        user = await AsyncORM.update_user_info(current_user.id, updated_user)
        return user
    
    @app.get("/sessionSeatsAvailable/{session_id}")
    async def session_seats_available(
        session_id: int
    ):
        session = await AsyncORM.get_avalable_seats(session_id)
        if session != None:
            return JSONResponse(
                {
                    "allSeats": session.numberOfSeats,
                    "occupiedSeats": len(session.orders)
                }
            )
        return JSONResponse(
                {
                    "allSeats": -1,
                    "occupiedSeats": -1
                }
            )

    @app.post("/bookSession")
    async def book_session_endpoint(
        session_id: int,
        current_user: Annotated[modelsDTO.UserDTO, Depends(get_current_active_user)]
    ):
        try:
            result = await AsyncORM.bookSession(session_id, current_user.id)
            print(result)
            return JSONResponse(
                {
                    "success": True,
                    "order_id": result["order_id"],
                    "payment_id": result["payment_id"],
                }
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Booking failed: {str(e)}")



    return app
