def mm_to_litres(depth_mm, area_m2):
    """Water volume in litres for a depth in mm over an area in square metres."""
    return depth_mm * area_m2
def litres_to_mm(litres, area_m2):
    """Depth in mm that a volume in litres makes over an area in square metres."""
    return litres / area_m2
def mm_to_m3_per_ha(depth_mm):
    """Cubic metres of water per hectare for a depth in mm (1 mm over 1 ha = 10 m3)."""
    return depth_mm * 10
if __name__ == "__main__":
    print("12 mm on 9600 m2 =", mm_to_litres(12, 9600), "litres")
    print("25 mm per hectare =", mm_to_m3_per_ha(25), "m3")
    print("500000 litres on 9600 m2 =", round(litres_to_mm(500000, 9600), 2), "mm")