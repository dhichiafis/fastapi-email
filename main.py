from fastapi import FastAPI,BackgroundTasks,Depends,Form
from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from pydantic import BaseModel
import uvicorn 


class EmailSchema(BaseModel):
    email:str 
    #message:str

conf =ConnectionConfig(
    MAIL_USERNAME='ochieng@gmail.com',
    MAIL_PASSWORD='password',
    MAIL_FROM='ochiengodhiambo56@gmail.com',
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)
app=FastAPI()


@app.post('/')
async def home():
    return {'message':'we are here createing and sending emails'}

html="""
<p>Thanks for using FastAPI-MAIL</p>
"""

def send_email(email:str,message:str):
    message=MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get('email'),
        body=html,
    )
    fm=FastMail(conf) 
    fm.send_message(message)
@app.post('/send/notifications/{email}')
async def send_notifications(
    background_tasks:BackgroundTasks,
    email:str,
    message:str=Form(...)):
    background_tasks.add_task(send_email,email,message)
    