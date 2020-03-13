import uvicorn
import sqlalchemy
from src.routes import routes
from src.db import database, metadata
from starlette.applications import Starlette


engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)

app = Starlette(
    debug=True,
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
)

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        reload=True
    )
