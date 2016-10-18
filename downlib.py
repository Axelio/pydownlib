import sys

PYTHON3 = True if sys.version_info.major > 2 else False

if PYTHON3:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen


def download_file(url, interruption=False):
    response = urlopen(url)
    # Trozos de 5 MB
    CHUNK = 1024 * 5120
    local_filename = url.split('/')[-1]
    with open(local_filename, 'wb') as f:
        cont = True
        while cont:
            chunk = response.read(CHUNK)
            if not chunk:
                break
            f.write(chunk)

            if interruption:
                # Nuevo trozo de archivo descargado. Desea contnuar?
                message = "It's a new chunk ({}MB). Continue? (Y/n): ".format(
                    CHUNK/1024/1024)
                message = input(message)
                if message == 'n':
                    cont = False


url = 'http://cdimage.debian.org/debian-cd/8.6.0/amd64/iso-cd/'
url = url + 'debian-8.6.0-amd64-CD-1.iso'
download_file(url)
# Con interrupcion:
# download_file(url, True)
