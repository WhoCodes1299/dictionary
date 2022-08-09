ara = input("Aradığınız kelimeyi yazın: ")

trEN = {"Wellies": "Lastik çizme", "Winks": "Göz Kırpma", "Begs": "Dilenmek", "Count": "Saymak", "Proudly": "Onurlu",
        "Incentive": "Teşvik Etmek", "Suggest": "Önermek", "Impersonations": "Canlandırmak", "Registration": "Tescil",
        "Discuss": "Görüşmek", "Queries": "Sorgulamak", "Slice": "Dilim", "Take Good Care": "Kendine İyi Bak",
        "Creature": "Varlık"}

print("Anlamı: ", end=" ")
print(trEN.get(ara, "Bu kelime mevcut değil, yakında eklenecektir."))
