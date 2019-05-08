import math
import pprint

def search_pythagorean():
	#ピタゴラス数の中で a,b,cの最大公約数が 1のものは，ある正の整数 m,nを用いて a=^m2−n^2,b=2mn,c=m^2+n^2
	cnt = 0
	n = 1
	m = 2
	pythagorean_triple = {}
	while cnt < 20:
		while n < m:
			divisor = n
			mod = 1
			while mod != 0: #ユークリッドの互除法
				#最大公約数gcd(greatest common divisor)を求める
				gcd = m
				mod = gcd % divisor
				gcd = divisor
				divisor = mod
			if gcd == 1: #gcdが1、すなわち互いに素
				if (m - n) % 2 == 1: #m-nが奇数
					a = m**2 - n**2
					b = 2 * m * n
					c = m**2 + n**2
				
					pythagorean_triple[cnt] = [a,b,c, ['m={}'.format(m), 'n={}'.format(n)]]
				
					cnt += 1

			n += 1
		
		n = 1
		m += 1
		

	return pythagorean_triple
			
def main():
	pprint.pprint(search_pythagorean())
	
if __name__ == '__main__':
	main()
