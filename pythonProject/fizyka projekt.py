import math
import numpy as np
import matplotlib.pyplot as plt
I_0 = 1.0
lambda_values = {
    'fioletowy': 400e-9,
    'niebieski': 470e-9,
    'zielony': 510e-9,
    'żółty': 570e-9,
    'czerwony': 700e-9
}
materials = {
    'azot': 1.0003,
    'tlen': 1.00027,
    'dwutlenek_wegla': 1.00045,
    'metan': 1.00038
}


def rayleigh_scattering_intensity(I_0, theta, R, n, lambda_wavelength, d):
    theta_rad = math.radians(theta)
    intensity = (I_0 * (1 + math.cos(theta_rad) ** 2) / (2 * R ** 2)) * \
                ((2 * math.pi / lambda_wavelength) ** 4) * \
                ((n ** 2 - 1) ** 2 / (n ** 2 + 2) ** 2) * (d ** 6 / 2)
    return intensity


def task_1():
    try:
        I_0 = float(input("Podaj początkową intensywność światła I_0: "))
        theta = float(input("Podaj kąt rozproszenia theta (w stopniach): "))
        R = float(input("Podaj odległość od cząstki R (w metrach): "))
        d_nm = float(input("Podaj średnicę cząsteczki d (w nanometrach): "))
        d = d_nm * 1e-9
        material = input("Wybierz materiał (azot, tlen, dwutlenek_wegla, metan): ").strip()

        if material in materials:
            n = materials[material]
        else:
            raise ValueError("Niepoprawny materiał")

        lambda_wavelength_nm = float(input("Podaj długość fali lambda (w nanometrach w zakresie 400-700): "))
        lambda_wavelength = lambda_wavelength_nm * 1e-9
        intensity = rayleigh_scattering_intensity(I_0, theta, R, n, lambda_wavelength, d)

        print(f"Intensywność światła rozproszonego: {intensity:.5e} W/m^2")
    except ValueError as e:
        print(f"Błąd wejściowy: {e}. Proszę spróbować ponownie.")


def task_2():
    print("\nZadanie 2: Wykres intensywności światła w funkcji długości fali")
    try:
        I_0 = float(input("Podaj początkową intensywność światła I_0: "))
        R = float(input("Podaj odległość od cząstki R (w metrach): "))
        material = input("Wybierz materiał (azot, tlen): ").strip().lower()
        theta = float(input("Podaj kąt rozproszenia theta (w stopniach): "))

        if material in materials:
            n = materials[material]
        else:
            raise ValueError("Niepoprawny materiał. Wybierz 'azot' lub 'tlen'.")
        d = 1e-9
        lambda_values = np.linspace(400e-9, 700e-9, 300)

        intensity_values = [
            rayleigh_scattering_intensity(I_0, theta, R, n, lambda_wavelength, d)
            for lambda_wavelength in lambda_values
        ]

        plt.figure(figsize=(8, 6))
        plt.plot(lambda_values * 1e9, intensity_values,
                 label=f"Rozproszenie dla {material.capitalize()} przy kącie {theta}°")
        plt.xlabel("Długość fali (nm)")
        plt.ylabel("Intensywność światła (W/m^2)")
        plt.title("Intensywność światła rozproszonego w funkcji długości fali")
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError as e:
        print(f"Błąd wejściowy: {e}. Proszę spróbować ponownie.")


def task_3():
    try:
        print("\nZadanie 3: Porównanie rozpraszania dla dwóch kolorów")

        color1 = input("Wybierz pierwszy kolor (fioletowy, niebieski, zielony, żółty, czerwony): ").strip()
        color2 = input("Wybierz drugi kolor (fioletowy, niebieski, zielony, żółty, czerwony): ").strip()

        if color1 not in lambda_values or color2 not in lambda_values:
            raise ValueError("Niepoprawny kolor. Wybierz z listy: fioletowy, niebieski, zielony, żółty, czerwony.")

        lambda1 = lambda_values[color1]
        lambda2 = lambda_values[color2]

        I_0 = 1.0
        R = 1.0
        theta = 90
        d = 1e-9
        n = materials['azot']

        intensity1 = rayleigh_scattering_intensity(I_0, theta, R, n, lambda1, d)
        intensity2 = rayleigh_scattering_intensity(I_0, theta, R, n, lambda2, d)

        if intensity1 > intensity2:
            print(f"{color1.capitalize()} ({lambda1 * 1e9:.0f} nm) jest silniej rozpraszany przez azot.")
        else:
            print(f"{color2.capitalize()} ({lambda2 * 1e9:.0f} nm) jest silniej rozpraszany przez azot.")
    except ValueError as e:
        print(f"Błąd wejściowy: {e}. Proszę spróbować ponownie.")


def task_4():
    try:
        d_nm = float(input("Podaj średnicę cząsteczki d (w nanometrach): "))
        d = d_nm * 1e-9
        material = input("Wybierz materiał (azot, tlen, dwutlenek_wegla, metan): ").strip()

        if material in materials:
            n = materials[material]
        else:
            raise ValueError("Niepoprawny materiał")

        lambda_wavelength = 500e-9
        theta = 90
        R = 1.0
        I_0 = 1.0
        intensity = rayleigh_scattering_intensity(I_0, theta, R, n, lambda_wavelength, d)
        print(f"Intensywność światła rozproszonego dla cząsteczki {material}: {intensity:.5e} W/m^2")
    except ValueError as e:
        print(f"Błąd wejściowy: {e}. Proszę spróbować ponownie.")


def main():
    print("Wybierz zadanie (1-4):")
    print("1 - Oblicz intensywność światła")
    print("2 - Narysuj wykres I w funkcji θ")
    print("3 - Porównaj rozpraszanie dla dwóch kolorów")
    print("4 - Wyświetl intensywność rozproszenia dla wybranego materiału")

    try:
        task = int(input("Wybierz zadanie: "))
        if task == 1:
            task_1()
        elif task == 2:
            task_2()
        elif task == 3:
            task_3()
        elif task == 4:
            task_4()
        else:
            print("Niepoprawny wybór zadania")
    except ValueError as e:
        print(f"Błąd: {e}. Proszę spróbować ponownie.")


if __name__ == "__main__":
    main()
