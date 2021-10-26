from imgurpython import ImgurClient
import urllib.request
import timeit
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

def descarga_url_img(link):
    #print(link)
    # Con esto ya podemos obtener el corte de la url imagen
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]
    print(nombre_img, formato_img)
    url_local = "/Users/txpla/Desktop/Escuela/Concurrencia/Imagenes/{}.{}" #es la ruta local, y cambiara de acuerdo al equipo
    #Guardar nne local las imagenes
    urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
        
def imagenes(lista,cliente):
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    for imagen in imagenes:
        lista.append(imagen.link) #lista de imagenes

def cliente():
    secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
    id_cliente = "bfa0e227a1c5643"
    cliente = ImgurClient(id_cliente, secreto_cliente) # cliente
    return cliente

def useThreadPoolExecutor(): #creamos
    ejecucion = ThreadPoolExecutor(max_workers=len(lista))
    ejecucion.map(descarga_url_img,lista)

def usePool(): #creamos
    ejecucion = Pool(len(lista))
    ejecucion.map(descarga_url_img,lista)
    
def useSincron():
    for i in lista:
        descarga_url_img(i) #creamos
        
if __name__ == "__main__":
    lista = []
    client = cliente()
    imagenes(lista,client)
    print("Tiempo de descarga usando la descarga sincrona: {}".format(timeit.Timer(useSincron).timeit(number=1)))
    print("Tiempo de descarga usando Subprocesos ThreadPoolExecutor: {}".format(timeit.Timer(useThreadPoolExecutor).timeit(number=1)))
    print("Tiempo de descarga usando Multiprocesamiento Pool: {}".format(timeit.Timer(usePool).timeit(number=1)))