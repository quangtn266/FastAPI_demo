# Import all the models, so taht Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.user import User
from app.models.recipe import Recipe