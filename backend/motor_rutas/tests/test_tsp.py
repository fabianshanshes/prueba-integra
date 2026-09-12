import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from prototipo_ruta_ficticia import resolver_tsp


def test_tsp_devuelve_orden_valido():
    matriz = np.array([
        [0, 10, 20],
        [10, 0, 15],
        [20, 15, 0],
    ])
    orden, dist, tiempo = resolver_tsp(matriz)
    assert orden[0] == 0              # empieza en origen
    assert orden[-1] == 0             # cierra ciclo
    assert dist > 0