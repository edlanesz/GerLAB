import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.cache import cache
import requests

# Configuração do logger
logging.basicConfig(level=logging.INFO)  # Configura o nível de log para INFO

# Define a classe para lidar com eventos de sistema de arquivos
class MediaChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:  # Se um diretório for criado, não faz nada
            return
        # Se um arquivo for criado dentro da pasta "media", atualize o cache
        if "media" in event.src_path:
            cache.clear()
            logging.info("Cache cleared")  # Adiciona um log para indicar que o cache foi limpo
            # Quando um arquivo de mídia é criado, solicite a reinicialização do Gunicorn
            logging.info("Requesting Gunicorn restart...")
            restart_gunicorn()

# Define o diretório a ser monitorado
MEDIA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')

def start_monitoring():
    event_handler = MediaChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, MEDIA_DIR, recursive=True)
    observer.start()
    logging.info("Monitoring media directory for changes...")

def restart_gunicorn():
    # Endpoint para reiniciar o Gunicorn
    gunicorn_restart_url = "http://localhost:9000/restart"
    try:
        response = requests.get(gunicorn_restart_url)
        if response.status_code == 200:
            logging.info("Gunicorn restart request sent successfully")
        else:
            logging.error(f"Failed to send Gunicorn restart request: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to send Gunicorn restart request: {str(e)}")

if __name__ == "__main__":
    start_monitoring()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        logging.info("Monitoring stopped")  # Adiciona um log para indicar que a monitoração foi interrompida
