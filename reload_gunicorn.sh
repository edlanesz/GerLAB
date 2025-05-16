#!/bin/bash

# Diretório a ser monitorado
MEDIA_DIR="media"

# Comando para recarregar o Gunicorn
RELOAD_COMMAND="kill -HUP $(cat /var/run/gunicorn.pid)"

# Monitora alterações nos arquivos de mídia e recarrega o Gunicorn
inotifywait -m -e close_write --format '%w%f' "$MEDIA_DIR" | while read FILE
do
    echo "File $FILE modified. Reloading Gunicorn..."
    $RELOAD_COMMAND
done
