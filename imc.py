m = float(input("Masse (kg) : "))
t = float(input("taille (m) : "))
imc = m/t**2
#phrase = ""

if(imc<=16.5):
    phrase = "Dénutrition ou famine"
elif(imc<=18.5):
    phrase = "Maigreur"
elif(imc<=25):
    phrase = "Corpulence normale"
elif(imc<=30):
    phrase = "Surpoids"
elif(imc<=35):
    phrase = "Obésité modérée"
elif(imc<=40):
    phrase = "Obésité sévère"
else:
    phrase = "Obésité mrobide ou massive"

print("IMC : ", imc)
print(phrase)