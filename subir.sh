#/bin/bash
git add .
FECHA_ACTUAL=$(date +'%Y-%m-%d %H:%M:%S')
git commit -m "Actualizacion: $FECHA_ACTUAL"
git push origin main
