from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product, seller, login

app = FastAPI(
    title="Product API",
    description="Get details for all the products on our website",
    terms_of_service="http://www.vpano360.com",
    contact={
        "Developer name": "Boonruang Seedapunt",
        "Website": "https://www.vpano360.com",
        "email": "scubatoy@gmail.com"
    },
    license_info={
        "name": "vpano360",
        "url": "https://www.vpano360.com"
    },
    # docs_url='/documentation', redoc_url=None
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)

models.Base.metadata.create_all(engine)
