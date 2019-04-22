import math
import pprint

def search_pythagorean():
	#ピタゴラス数の中で a,b,cの最大公約数が 1のものは，ある正の整数 m,nを用いて a=m2−n2,b=2mn,c=m2+n2
	cnt = 0
	start = 1
	second = 2
	pythagorean_triple = {}
	while cnt < 20:
		divisor = start
		mod = 1
		while mod != 0: #ユークリッドの互除法
			#最大公約数gcdを求める
			gcd = second
			mod = gcd % divisor
			gcd = divisor
			divisor = mod
		if gcd == 1: #最大公約数が1、すなわち互いに素
			if (second - start) % 2 == 1: #m-nが奇数
				a = second**2 - start**2
				b = 2 * second * start
				c = second**2 + start**2
				
				pythagorean_triple[cnt] = [a,b,c]
				
				cnt += 1
		second += 1
		start += 1
	return pythagorean_triple
			
def main():
	pprint.pprint(search_pythagorean())
	
if __name__ == '__main__':
	main()
