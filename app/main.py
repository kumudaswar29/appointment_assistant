from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.database import Base, engine

# Models
from app.models.user import User
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.availability import Availability

# Routers
from app.routers import auth, patients, doctors, appointments, ai, availability, users

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Appointment Assistant API")


# Middleware to hide actual server information
class RemoveServerHeaderMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        response = await call_next(request)

        # Remove existing server header
        if "server" in response.headers:
            del response.headers["server"]

        # Add custom hidden header
        response.headers["server"] = "SecureServer"

        return response


# Register middleware
app.add_middleware(RemoveServerHeaderMiddleware)


# Register routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(ai.router)
app.include_router(availability.router)


@app.get("/")
def home():
    return {"message": "AI Appointment Assistant API Running Successfully"}