





user = str(input("Ingresa un nombre de usuario"))
password = str(input("Ingresa la contraseña de tu cuenta"))
user = str.lower(user)

caracters_user = user.isalnum()#son true entra en el while#
caracters_password = password.isalnum()


#listas de usuarios y contraseñas#
lista_user = {"marcos" : "user", "daniel" : "user2", "yorgely" : "user3", "esteban" : "user4"}
lista_password = {"user" : "tazmania", "user2": "del1al10", "user3" : "1al10","user4" : "50125"}

#validadores de los disccionarios #
egt = lista_user.get(user)
etg = lista_password.get(egt)

#confirmacion de los values de user en diccionario#
value_user = lista_user.values()
value_user_confirm = egt in value_user

#confirmacion de los values de password en diccionario#
value_password_confirm = password == lista_password[egt]

print(value_password_confirm)

if value_user_confirm is True:
    if value_password_confirm is True:
        access = True
        print("Bienvenido")
    elif value_password_confirm is False:
        acces = False
        print("El usuario o la contraseña es incorrecta")

else:
    print("la cuenta no existe")
    acces = False
