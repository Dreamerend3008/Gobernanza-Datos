import matplotlib.pyplot as plt

segmentos = ['Banca comercial', 'Banca de inversion', 'Seguros', 'Fondos de Pensiones', 'Otros']
valores = [62.4, 15.2, 12.8, 6.3, 3.3]

plt.figure(figsize=(10, 6))
plt.pie(valores, labels=segmentos, autopct='%1.1f%%', startangle=140)
plt.title('Distribución Porcentual de Ingresos - Bancolombia 2023', fontsize=16)
plt.axis('equal')

# Guardar la gráfica como imagen PNG
plt.savefig('grafica_bancolombia.png')