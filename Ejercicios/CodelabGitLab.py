'''
Desarrollar un script en python que permita consultar el número de proyectos
de los que es propietario un usuario concreto en GitLab, preentados por fecha de último actividad

GITLAB_API_URL = "https://gitlab.com/api/v4/"

'''
import operator

import requests

#URL de la api
url_base = 'https://gitlab.com/api/v4/'

#Definimos el nombre del usuario cuyos proyectos queremos acceder
usuario_propietario = 'jabiertxof'

# Construimos la URL completa para obtener la lista de proyectos del usuario
url = f'{url_base}users/{usuario_propietario}/projects'

# Realizamos la solicitud HTTP con el token de acceso en la cabecera de la solicitud
respuesta = requests.get(url)


# Comprobamos que la solicitud se haya realizado correctamente
if respuesta.status_code == 200:
    # Imprimimos la lista de proyectos del usuario
    proyectos = respuesta.json()
    sorted_json = sorted(proyectos, key=operator.itemgetter("last_activity_at"), reverse=True)
    for proyecto in sorted_json:
        print(proyecto['name'],proyecto['last_activity_at'])
else:
    print(f'Error al consultar los proyectos del usuario {usuario_propietario}: {respuesta.text}')