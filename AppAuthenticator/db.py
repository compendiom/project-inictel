import pyodbc
import pandas as pd

user= 'sa'
password= 'Inictel2024'
server='JUTRWS'
database='BD_GEDSYS'
    #'port': 1433

def connectDB():
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
        print("¡Se realizó la conexión a la base de datos de manera exitosa!")
        return conexion
    except Exception as e:
        print("¡Error al conectar en la base de datos!")
        print("ERROR:", e)
    finally:
        conexion.close()
    return False

def validateInfo(dni, apellido):
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
        cursor = conexion.cursor()
        cursor.execute('EXEC [dbo].[SPU_VALIDACION_CLIENTE] @apellido=?, @dni=?', apellido, dni)
        print(cursor.fetchval())
        if cursor.fetchval() is not None or cursor.fetchval() == " ":
            result = False
        else:
            result = cursor.fetchval()
    except Exception as e:
        print("Error en la consulta")
        print("ERROR:", e)
        result = False
    finally:
        cursor.close()
        conexion.close()
    return result
    
def getCursos(dni):
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
        cursor = conexion.cursor()
        cursor.execute('EXEC [dbo].[SPU_VALIDACION_LIST_CURSO] @dni=?', dni)
        result = cursor.fetchall()
    except Exception as e:
        print("Error en la busqueda de listado de cursos")
        print("ERROR:", e)
        result = False
    finally:
        cursor.close()
        conexion.close()
    return result