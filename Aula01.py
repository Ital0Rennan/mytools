import MYTOOLS

num_pi = int(input("De quantas casas decimais você deseja que seja apresentado o número pi? [<100]"))
num_e = int(input("De quantas casas decimais você deseja que seja apresentado o número neperiano? [<100]"))

print(MYTOOLS.pi_real(num_pi))
print(MYTOOLS.e_real(num_e))