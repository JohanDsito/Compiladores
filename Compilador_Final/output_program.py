import time

# ── Estado de los drones ──────────────────────────────
explorador = {'en_vuelo': False, 'x': 0.0, 'y': 0.0, 'altitud': 0.0, 'bateria': 100, 'orientacion': 0}

# ── Zonas declaradas ──────────────────────────────────
zonas = {'inicio': (0.0, 0.0), 'norte': (0.0, 50.0), 'sur': (0.0, -50.0)}

# ── Misión: recorrido ────────────────────────────────────
def recorrido():
    # despegar explorador
    explorador['en_vuelo'] = True
    explorador['altitud'] = 1.0
    # mover explorador arriba 30
    explorador['altitud'] += 30
    # ir_a explorador -> norte
    explorador['x'], explorador['y'] = zonas['norte']
    # esperar 3s
    time.sleep(3)
    # ir_a explorador -> sur
    explorador['x'], explorador['y'] = zonas['sur']
    # esperar 3s
    time.sleep(3)
    # ir_a explorador -> inicio
    explorador['x'], explorador['y'] = zonas['inicio']
    # aterrizar explorador
    explorador['en_vuelo'] = False
    explorador['altitud'] = 0.0


# ── Punto de entrada ──────────────────────────────────
if __name__ == '__main__':
    recorrido()