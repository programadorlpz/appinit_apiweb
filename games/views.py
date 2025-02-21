import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import GameService

logger = logging.getLogger(__name__)

class IniciarBatallaView(APIView):
    def post(self, request):
        try:
            nombre1 = request.data.get('nombre1')
            nombre2 = request.data.get('nombre2')
            g_id = GameService().iniciar_batalla(nombre1, nombre2)
            return Response({'game_id': g_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MovimientoView(APIView):
    def post(self, request, game_id):
        try:
            jugador = request.data.get('jugador')
            movimiento = request.data.get('movimiento')
            r_id = GameService().registrar_movimiento(game_id, jugador, movimiento)
            return Response({'round': r_id}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
