import sqlite3
import hashlib

def create_db():
    con = sqlite3.connect("em.db")

    cur = con.cursor()

    cur.execute("""CREATE TABLE "users" (
    "id" INTEGER,
    "fio" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)

    cur.execute("""CREATE TABLE "settings" (
    "id" INTEGER,
    "maximum_power" INTEGER NOT NULL,
    "id_user" INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("id_user") REFERENCES "users"("id")
    );
    """)

    cur.execute("""CREATE TABLE "electrical_appliances" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "power" INTEGER NOT NULL,
    "working_hours" INTEGER NOT NULL,
    "consumption" FLOAT NOT NULL,
    "id_user" INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("id_user") REFERENCES "users"("id")
    );
    """)

    email = "admin@gmail.com"
    fio = "Admin"
    password = hashlib.sha256(b"123456789").hexdigest()

    cur.execute(f"INSERT INTO users(fio, email, password) VALUES ('{fio}', '{email}', '{password}');")
    con.commit()

    cur.execute(f"INSERT INTO settings(maximum_power, id_user) VALUES (0, 1);")
    con.commit()

    cur.close()
    con.close()


if __name__ == "__main__":
    create_db()