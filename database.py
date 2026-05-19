import psycopg2

conn = psycopg2.connect(
    database = "hoopiq",
    user = "souleymanebah",
    password = "",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()