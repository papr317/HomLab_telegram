"""
мини приложения по темам. логика 
"""

def call_homelab_app(action_name: str) -> str:
        # работоспособность сервера 
    if action_name == "status":
      
        return "тут будет мониторинг температуры, нагрузки и интернета ."
      
    # управление Docker-контейнерами
    elif action_name == "docker":
        return "Docker-контейнеры успешно управляются."
      
        # торрент-клиент для фильмов и сериалов
    elif action_name == "torrent":
        return "Торрент-клиент в разработке."
      
      
      # на случай ошибки 
    else:
      return "ТЫ ПРИЕМЫШЬ, КАК ТЫ ЭТО СДЕЛАЛ?"