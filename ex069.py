print('{:^50}'.format('\033[1:33mEXERCICIO   069\033[m'))
maioridade = homens = mulhermenor = 0
while True:
    print('\033[1:31m<=>\033[m' * 15)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('\033[1:31m<=>\033[m' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if idade < 18 and sexo == 'F':
        mulhermenor += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    print('\033[1:32m-\033[m' * 30)

print('FIM DO PROGRAMA')
print('')
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homem(s) cadastrado')
print(f'Temos {mulhermenor} mulher com menos de 20 anos')