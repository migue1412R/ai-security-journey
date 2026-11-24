def main():
    input_usuario = input("Introduce tu nombre de usuario: ")   
    input_ip = input("Introduce la IP: ")
    input_accion = input("Introduce la acción: ")
    print(formatear_evento(input_usuario, input_ip, input_accion))


def formatear_evento(usuario, ip, accion):
    return f"[{ip}] {usuario} -> {accion}"
    # [192.168.1.10] migue -> login_fallido
  

main()
