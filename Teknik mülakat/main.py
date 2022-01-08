import re
metin = "Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you."
kelime = metin.split()
print (kelime)





ara = str("armour")
yenı= str("sheild")
cumle = re.sub(ara,yenı,metin)

print (cumle)
#istediğiniz gibi for/forech kullanımı ile yapamadım ancak bu yöntemle yapabildim. For/foreach üstünde çalışmaya devam ediyorum.
