def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'g1372000'
    app.config['MYSQL_DATABASE_DB'] = 'concesionaria'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['DEBUG'] = True


def sql_excluir_usuario(cursor, conn, idusuario):
    cursor.execute(f'delete from concesionaria.user where iduser = {idusuario}')
    conn.commit()
    cursor.close()
    conn.close()


def get_idlogin(cursor, conn, login, senha):
    # Executar o sql
    cursor.execute(f'select iduser from concesionaria.user where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()
    conn.close()
    if idlogin == None:
        return False
    else:
        return idlogin[0]


def incluir_cont(cursor, conn, login, senha):
    cursor.execute(f'insert into concesionaria.user (login, senha) values("{login}", "{senha}")')
    conn.commit()
    cursor.close()
    conn.close()


def get_id_imagens(cursor,conn):
    cursor.execute(f'select idcars, foto, vip from concesionaria.cars')
    id_imagens = cursor.fetchall()
    id_imagens = [list(x) for x in id_imagens]
    cursor.close()
    conn.close()
    return id_imagens


def excluir_carro(cursor,conn,idcars):
    cursor.execute(f'delete from concesionaria.cars where idcars = {idcars}')
    conn.commit()
    cursor.close()
    conn.close()




def criar_anuncio(cursor,conn,placa,modelo,marca,valor,vip,foto):
    cursor.execute(f'insert into concesionaria.cars (placa,modelo,marca,valor,vip,foto) values("{placa}", "{modelo}", "{marca}"'
                   f', "{valor}", "{vip}","{foto}")')
    conn.commit()
    cursor.close()
    conn.close()