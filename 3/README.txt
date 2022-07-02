Открыть консоль и перейти в папку rootserver
Прописать python3 -m http.server
Запустить скрипт python3 -i activation_script.py
Написать в интерпретаторе sys.path.append("http://localhost:8000")
Теперь можно импортить модуль и вызывать функицю: 
    import myremotemodule
    myremotemodule.foo()