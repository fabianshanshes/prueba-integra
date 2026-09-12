import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.filtros import filtrar_productos, sanitizar_filtros_crudos


def test_sanitizar_dict_vacio():
    assert sanitizar_filtros_crudos({}) == {}


def test_sanitizar_precio_numerico():
    r = sanitizar_filtros_crudos({"precio_max": 1500})
    assert r["precio_max"] == 1500


def test_sanitizar_precio_texto_se_descarta():
    r = sanitizar_filtros_crudos({"precio_max": "omision"})
    assert "precio_max" not in r


def test_filtrar_por_categoria():
    catalogo = [
        {"id": 1, "nombre": "Tomate", "precio": 990, "categoria": "verduras", "distancia_km": 1.0},
        {"id": 2, "nombre": "Leche",  "precio": 1190, "categoria": "lacteos", "distancia_km": 2.0},
    ]
    r = filtrar_productos(catalogo, {"categoria": "verduras"})
    assert len(r) == 1 and r[0]["nombre"] == "Tomate"