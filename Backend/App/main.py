from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.Modules.Authentication.router import(
    router as authentication_router
)
from App.Modules.Employees.router import router as employee_router

# from App.Core.database import test_database_connection #Importing The test_database_connection Function From The Database Module Which Will Be Used To Test The Database Connection.

# from pydantic import BaseModel #Importing The BaseModel Class From The Pydantic Library Which Will Be Used To Define The Request Body Model For The Insert Data Endpoint.

# class TestMessage(BaseModel): #Creating A Request Body Model For The Insert Data Endpoint Which Will Be Used To Validate The Incoming Request Body.
#     name: str #Defining A Single Field name Of Type String Which Will Be Used To Store The Name To Be Inserted Into The Test Table.

app = FastAPI(
    title="HRMS API",
    version="1.0.0"
) #Creating An Instance Of The FastAPI Class Whuich Will Be Used To Create The FastAPI Application.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health") #Creating A Health Check Endpoint Which Will Be Used To Check If The Application Is Running Successfully.
def health_check(): #health_check Function Is Used To Return A JSON Response Indicating That The Application Is Running Successfully.
    return{
        "status": "ok",
        "message": "The HRMS API Is Running Successfully"
    }

app.include_router(authentication_router)
app.include_router(employee_router)

# @app.get("/api/v1/health/database") #Creating A Health Check Endpoint Which Will Be Used To Check If The Database Is Connected Successfully.
# def database_health_check(): #database_health_check Function Is Used To Return A JSON Response Indicating That The Database Is Connected Successfully.
#     try:
#         test_database_connection()

#         return{
#                 "status": "ok",
#                 "message": "The Database Connected Successfully"
#             }
#     except Exception as e:
#         return{
#             "status": "error",
#             "message": f"Database Connection Failed: {str(e)}"
#         }

# @app.post("/api/v1/test/test-table") #Creating An Endpoint To Create A Test Table In The Database.
# def create_test_database_table():
#     try:
#         create_test_table()

#         return{
#                 "status": "ok",
#                 "message": "Test Table Created Successfully"
#             }
#     except Exception as e:
#         return{
#             "status": "error",
#             "message": f"Test Table Creation Failed: {str(e)}"
#         }

# @app.post("/api/v1/test/test-table/insert") #Creating An Endpoint To Insert Data Into The Test Table In The Database.
# def insert_data_into_test_table(data: TestMessage): #insert_data_into_test_table Function Is Used To Insert Data Into The Test Table In The Database. It Accepts A Request Body Of Type TestMessage Which Contains The Message To Be Inserted Into The Test Table.
#     try:
#         data_insertion_test_table(data.name)

#         return{
#                 "status": "ok",
#                 "message": "Data Inserted Into Test Table Successfully"
#             }
#     except Exception as e:
#         return{
#             "status": "error",
#             "message": f"Data Insertion Into Test Table Failed: {str(e)}"
#         }