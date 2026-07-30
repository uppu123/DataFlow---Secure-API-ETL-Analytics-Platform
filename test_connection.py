import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="Aaranya3112",
    host="db.dromgxiumpynbbncemwv.supabase.co",
    port=5432,
    dbname="postgres"
)

print("Connected successfully!")

conn.close()