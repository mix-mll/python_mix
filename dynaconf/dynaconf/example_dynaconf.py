from config import settings

# settings.username == "admin"  # dot notation with multi nesting support
# settings.PORT == 9900  # case insensitive
# settings['password'] == "secret123"  # dict like access
# settings.get("nonexisting", "default value")  # Default values just like a dict
# settings.database.name == "mydb"  # Nested key traversing
# settings['database.schema'] == "main"  # Nested key traversing

print(settings.database.name)
print(settings.PORT)
print(settings.port)

print(settings.port)

print(settings.servers.beta)
print(settings.servers.alpha)

print(settings.password)
