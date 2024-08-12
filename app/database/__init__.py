from .dao import HolderDAO
from .middleware import DatabaseMiddleware

Database = HolderDAO

__all__ = ["Database", "DatabaseMiddleware", "HolderDAO"]
