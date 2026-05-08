import time

# ── Estado de los drones ──────────────────────────────
halcon = {'en_vuelo': False, 'x': 0.0, 'y': 0.0, 'altitud': 0.0, 'bateria': 100, 'orientacion': 0}

# ── Zonas declaradas ──────────────────────────────────
zonas = {'base': (0.0, 0.0), 'punto_a': (10.0, 5.0)}

# ── Misión: patrulla ────────────────────────────────────
def patrulla():
    # despegar halcon
    halcon['en_vuelo'] = True
    halcon['altitud'] = 1.0
    # mover halcon arriba 15
    halcon['altitud'] += 15
    # ir_a halcon -> punto_a
    halcon['x'], halcon['y'] = zonas['punto_a']
    # repetir 3 veces
    for _ in range(3):
        # girar halcon derecha 90°
        halcon['orientacion'] = (halcon.get('orientacion', 0) + 90) % 360
        # mover halcon adelante 5
        halcon['x'] += 5
    # si halcon.bateria < 20
    if halcon['bateria'] < 20:
        # ir_a halcon -> base
        halcon['x'], halcon['y'] = zonas['base']
    else:
        # esperar 10s
        time.sleep(10)
    # aterrizar halcon
    halcon['en_vuelo'] = False
    halcon['altitud'] = 0.0


# ── Punto de entrada ──────
if __name__ == '__main__':
    patrulla()