from django.db import connection

class GameService:
    def iniciar_batalla(self, nombre1: str, nombre2: str) -> int:
        with connection.cursor() as cur:
            cur.execute("SELECT sp_iniciar_batalla(%s,%s)", [nombre1, nombre2])
            g_id = cur.fetchone()[0]
            return g_id

    def registrar_movimiento(self, game_id: int, jugador: str, movimiento: str) -> int:
        with connection.cursor() as cur:
            cur.execute("SELECT sp_registrar_movimiento(%s,%s,%s)", [game_id, jugador, movimiento])
            r_id = cur.fetchone()[0]
            return r_id
