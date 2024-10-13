# Conversion d'une adresse IP décimale en binaire
def adresse_ip_bin(ip):
    parties = ip.split('.')
    bin_ip = ''
    for part in parties:
        bin_ip += '{:08b}'.format(int(part))
    return bin_ip

# Conversion d'une adresse IP binaire en décimale
def adresse_ip_dec(bin_ip):
    parties = [str(int(bin_ip[i:i+8], 2)) for i in range(0, 32, 8)]
    return '.'.join(parties)

#Calculer les informations d'une adresse IP à partir de son CIDR
def calcul_infos_ip(ip_cidr):
    ip, cidr = ip_cidr.split('/')
    cidr = int(cidr)
    
    # Calcul du masque de sous-réseau
    masque_bin = '1' * cidr + '0' * (32 - cidr)
    masque_dec = adresse_ip_dec(masque_bin)
    
    # Adresse réseau
    ip_bin = adresse_ip_bin(ip)
    adresse_reseau_bin = ip_bin[:cidr] + '0' * (32 - cidr)
    adresse_reseau = adresse_ip_dec(adresse_reseau_bin)
    
    # Adresse de diffusion
    adresse_diffusion_bin = ip_bin[:cidr] + '1' * (32 - cidr)
    adresse_diffusion = adresse_ip_dec(adresse_diffusion_bin)
    
    # Première et dernière adresse hôte
    premiere_ip_bin = adresse_reseau_bin[:-1] + '1'
    derniere_ip_bin = adresse_diffusion_bin[:-1] + '0'
    premiere_ip = adresse_ip_dec(premiere_ip_bin)
    derniere_ip = adresse_ip_dec(derniere_ip_bin)
    
    # Nombre total d'adresses IP
    nb_ips = 2**(32 - cidr)
    
    # Nombre d'adresses disponibles pour les hôtes (sans réseau ni diffusion)
    nb_hotes = nb_ips - 2
    
    # Affichage des informations
    print("Adresse IP:", ip + '/' + str(cidr))
    print("Masque de sous-réseau:", masque_dec)
    print("Adresse réseau:", adresse_reseau)
    print("Adresse de diffusion:", adresse_diffusion)
    print("Première adresse hôte:", premiere_ip)
    print("Dernière adresse hôte:", derniere_ip)
    print("Nombre total d'adresses:", nb_ips)
    print("Nombre d'hôtes disponibles:", nb_hotes)

#Demander à l'utilisateur d'entrer une adresse IP et un CIDR
def saisie_adresse_ip_cidr():
    return input("Entrez l'adresse IP avec son CIDR : ")


ip_cidr = saisie_adresse_ip_cidr()
calcul_infos_ip(ip_cidr)