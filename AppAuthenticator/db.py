import pyodbc

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
        result = cursor.execute('EXEC [dbo].[SPU_VALIDACION_CLIENTE] @apellido=?, @dni=?', apellido, dni).fetchval()
        if result is None:
            result = False
        else:
            print("Usuario validado")
    except Exception as e:
        print("Error en la consulta")
        print("ERROR:", e)
    finally:
        cursor.close()
        conexion.close()
    return result
    
def getValidatedCursos(dni, codigo, tipo):
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
        cursor = conexion.cursor()
        cursor.execute('EXEC [dbo].[SPU_VALIDACION_QUERY_CURSO] @dni=? @codigo @tipo', dni, codigo, tipo)
        result = cursor.fetchall()
    except Exception as e:
        print("Error en la busqueda del documento")
        print("ERROR:", e)
        result = False
    finally:
        cursor.close()
        conexion.close()
    return result