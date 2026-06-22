from modulos.menu import menu
from modulos.archivos import cargar_canciones




lista_canciones = cargar_canciones()
print(r"""
===========================================================================
 __  __                                                      _____      
/\ \/\ \                                                 __ /\  __`\    
\ \ \_\ \      __     _ __    ___ ___      ___     ___  /\_\\ \ \/\ \   
 \ \  _  \   /'__`\  /\`'__\/' __` __`\   / __`\ /' _ `\\/\ \\ \ \ \ \  
  \ \ \ \ \ /\ \L\.\_\ \ \/ /\ \/\ \/\ \ /\ \L\ \/\ \/\ \\ \ \\ \ \\'\\ 
   \ \_\ \_\\ \__/.\_\\ \_\ \ \_\ \_\ \_\\ \____/\ \_\ \_\\ \_\\ \___\_\
    \/_/\/_/ \/__/\/_/ \/_/  \/_/\/_/\/_/ \/___/  \/_/\/_/ \/_/ \/__//_/

===========================================================================
""")

print(" Este programa sirve para almacenar tus canciones.\n¡Espero disfrutes esta pequeña prueba!")
menu(lista_canciones)

