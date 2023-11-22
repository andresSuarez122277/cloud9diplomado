import boto3

#crear funcion  para listar tablas de dynamodb
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)

#crear funcion para crear tabla de dynamodb
def crear_tabla(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=nombre_tabla,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    print("Tabla creada exitosamente")


#crear funcion para insertar un elemento a tabla dynamodb
def insertar_elementos(nombre_tabla, id, nombre, apellido, hobby):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.put_item(Item={
        'id': id,
        'nombre': nombre,
        'apellido': apellido,
        'hobby': hobby
    })
    print("Elemento insertado exitosamente")

#crear funcion para leer elementos de tabla dynamodb
def leer_elementos(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)

#crear funcion para eliminar un elemento de la tabla dynamodb mediante un campo
def eliminar_elementos(nombre_tabla, id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.delete_item(Key={'id': id})
    print("Elemento eliminado exitosamente")

#crear funcion para reconocer celebridad mediante imagen
def reconocer_celebridad(imagen):
    rekognition = boto3.client('rekognition')
    response = rekognition.recognize_celebrities(Image={'Bytes': imagen})
    print(response['CelebrityFaces'][0]['Name'])

opcion = 1

while opcion != 0:
    print("Ingrese la opcion que desee")
    print("1. Listar tablas de dynamodb de la cuenta")
    print("2. Crear nueva tabla")
    print("3. Insertar un elemento a la tabla")
    print("4. Leer elementos de la tabla")
    print("5. Eliminar un elemento de la tabla")
    print("6. Reconocer celebridad mediante imagen")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        listar_tablas()
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        crear_tabla(nombre_tabla)
    elif opcion == 3:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        iid = input("Ingrese el id del elemento: ")
        nombre = input("Ingrese el nombre : ")
        apellido = input("Ingrese el apellido: ")
        hobby = input("Ingrese el hobby: ")
        insertar_elementos(nombre_tabla, iid, nombre, apellido, hobby)
    elif  opcion == 4:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        leer_elementos(nombre_tabla)
    elif opcion == 5:
        nombre_tabla = input("Ingrese el nombre de la tabla: ")
        iid = input("Ingrese el id: ")
        eliminar_elementos(nombre_tabla, iid)
    elif opcion == 6:
        #convertir imagen a bytes
        with open('/home/ec2-user/environment/cloud9diplomado/imagen.jpg', 'rb') as f:
            imagen = f.read()
            reconocer_celebridad(imagen)
    elif opcion == 0:
        print("Saliendo...")
    else:
        print("Opcion no válida")

