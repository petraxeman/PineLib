#import pinelib as pl
import pinelib.series as pls
import pinelib.math as plm

test_serie = pls.Serie([1, 2, 3, 4, 5])
print(test_serie)
print(test_serie[2])
print('Add S+S', test_serie + test_serie[2])
print('Add S+I', test_serie + 2)
print('Sub S-S', test_serie - test_serie[2])
print('Sub S-I', test_serie - 2)
print('FDiv S//S', test_serie // test_serie[2])
print('FDiv S//I', test_serie // 2)
print('TDiv S/S', test_serie / test_serie[2])
print('TDiv S/I', test_serie / 2)
print('Mul S*S', test_serie * test_serie[2])
print('Mul S*I', test_serie * 2)
print('Mod S%S', test_serie % test_serie[2])
print('Mod S%I', test_serie % 2)
print('Pow S**S', test_serie ** test_serie[2])
print('Pow S**I', test_serie ** 2)

print('First Serie:', pls.Serie([1, 2, 3, 4, 5]))
print('Second Serie:', pls.Serie([1, 1, 1, 1, 1, 1, 1, 1]))
print('Answer', pls.Serie([1, 2, 3, 4, 5]) + pls.Serie([1, 1, 1, 1, 1, 1, 1, 1]))
test_serie2 = pls.Serie([1, 1, 1, 1, 1, 1])
print('Before iadd:', test_serie2)
test_serie2 += test_serie
print('After iadd:', test_serie2)

print('\n\n\nMath:')
print(test_serie)
print('e = ', plm.e)
print('pi = ', plm.pi)
print('phi = ', plm.phi)
print('rphi = ', plm.rphi)
print(f'math.abs({test_serie.data * -1}) ->', plm.abs(test_serie * -1))
print(f'math.acos([0.0, 0.2, 0.4, 0.6, 0.8, 1]) ->', plm.acos(pls.Serie([0.0, 0.2, 0.4, 0.6, 0.8, 1])))
print(f'math.asin([0.0, 0.2, 0.4, 0.6, 0.8, 1]) ->', plm.asin(pls.Serie([0.0, 0.2, 0.4, 0.6, 0.8, 1])))
print(f'math.atan({test_serie.data}) ->', plm.atan(test_serie))
print(f'math.avg({test_serie.data}) ->', plm.avg(test_serie))
print(f'math.ceil() ->', plm.ceil(pls.Serie([0.0, 0.2, 0.4, 0.6, 0.8, 1])))
print(f'math.sum({test_serie.data}) ->', plm.sum(test_serie))
print(f'math.sqrt({test_serie.data}) ->', plm.sqrt(test_serie))
print(f'math.pow({test_serie.data}, 2) ->', plm.pow(test_serie, 2))
print(f'math.min({test_serie.data}) ->', plm.min(test_serie))
print(f'math.max({test_serie.data}) ->', plm.max(test_serie))
print(f'math.exp({test_serie.data}) ->', plm.exp(test_serie))
print(f'math.cos({test_serie.data}) ->', plm.cos(test_serie))
print(f'math.cos(math.abs{test_serie.data})) ->', plm.abs(plm.cos(test_serie)))