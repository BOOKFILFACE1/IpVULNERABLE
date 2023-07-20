import nmap
import requests

def check_service_version(service_url):
    try:
        response = requests.get(service_url)
        if response.status_code == 200:
            return response.text.strip()
        return "Error: No se pudo obtener la versión"
    except:
        return "Error: No se pudo conectar al servicio"

def check_vulnerabilities(service_name, service_version):
    # Aquí deberías consultar una base de datos de vulnerabilidades conocidas
    # para verificar si el servicio y su versión son vulnerables.
    # Dado que no podemos realizar esto en el ejemplo, simplemente imprimimos el resultado.
    print(f"Verificando vulnerabilidades para {service_name} - Versión: {service_version}")
    if "desactualizado" in service_version.lower():
        print("¡Vulnerable! Se encontró una versión desactualizada.")
    else:
        print("No se encontraron vulnerabilidades conocidas para esta versión.")

if __name__ == "__main__":
    ip = input("Ingrese la dirección IP a verificar: ")

    nm = nmap.PortScanner()
    nm.scan(ip, arguments="-T4 -F")  # Escaneo rápido de puertos

    vulnerable_services = {
        80: "http://localhost/version.txt",   # Ejemplo de URL para obtener la versión de un servicio HTTP
        3306: "http://localhost/version.txt"   # Ejemplo de URL para obtener la versión de un servicio MySQL
        # Puedes agregar más puertos y URLs para verificar otros servicios
    }

    print("\nResultado del análisis de puertos:")
    for port in nm[ip]['tcp']:
        print(f" - Puerto {port}: {nm[ip]['tcp'][port]['name']} - Estado: {nm[ip]['tcp'][port]['state']}")
        if port in vulnerable_services:
            version = check_service_version(vulnerable_services[port])
            check_vulnerabilities(nm[ip]['tcp'][port]['name'], version)
