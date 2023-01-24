# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_cars(**cars):
    if cars:
        for name, mark in cars.items():
            print(f"{name}: {mark}")
    else:
        return None


if __name__ == "__main__":
    print_cars(
        Toyota="Mark2", Nissan="Silvia", Mazda="RX-7",
        Honda="Civic", Tesla="CyberTruck", Porsche="Macan",
    )