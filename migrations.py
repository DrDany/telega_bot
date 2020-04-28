import sqlite3 as sql


if __name__ == "__main__":
    databaseFile = 'db.sqlite'
    sqlFile = 'init_script.sql'

    try:
        print("Opening DB")
        con = sql.connect(databaseFile)
        cursor = con.cursor()

        print("Reading initial Script...")
        scriptFile = open(sqlFile, 'r', encoding="utf-8")
        script = scriptFile.read()
        scriptFile.close()

        print("Running Script...")
        cursor.executescript(script)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Error execute migrations: ", e)
    finally:
        con.close()