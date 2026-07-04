import os
import sys

# Limitar hilos de OpenBLAS (evita problemas de recursos)
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'
os.environ['FLASK_DEBUG'] = 'false'

# Agregar el directorio actual al path de Python
sys.path.insert(0, os.path.dirname(__file__))

# Importar la aplicación Flask
from app import app as application