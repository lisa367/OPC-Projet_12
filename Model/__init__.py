from .clients import create_table_clients
from .collaborateurs import create_table_collaborateurs, collaborateurs_colonnes
from .contrats import create_table_contrats
from .evenements import create_table_evenements
from .base import new_entry, new_entries, get_all


create_table_collaborateurs()
create_table_clients()
create_table_contrats()
create_table_evenements()

# print(get_all("collaborateurs"))
collaborateurs_db_content = get_all("collaborateurs")

if not collaborateurs_db_content:
    admin_data = ["admin", "admin", "Gestion", "administrateur", "admin@fauxmail.com"]
    new_entry("collaborateurs", collaborateurs_colonnes, admin_data)