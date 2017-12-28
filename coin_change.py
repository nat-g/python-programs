#!/usr/bin/env python

def rec_coin1(target,coins):
	

	coin_min = target

	if target in coins:
		return 1

	else:
		for i in [c for c in coins if c<=target]:
			coin_num = 1 + rec_coin1(target-c,coins)

			if coin_num < coin_min:
				coin_min = coin_num

	return coin_min

print rec_coin1(10,[1,2,3,5])


def rec_coin2(target,coins):

	coin_final = target

	for coin in [ c for c in coins if c < target]:

		coin_num = 0

		if target%coin == 0:
			coin_num += target//coin

		else:
			coin_num += target//coin + rec_coin2(target%coin,coins)
			#print target//coin
			#print target%coin

		if coin_num < coin_final:
			coin_final = coin_num

	return coin_final

print rec_coin2(10,[1,3,5])



def rec_coin3(target,coins):

	coin_final = target

	for coin in [ c for c in coins if c < target]:

		coin_num = 0

		if target in coins:
			coin_num += 1

		else:
			coin_num = 1 + rec_coin3(target-coin,coins)

		if coin_num < coin_final:
			coin_final = coin_num

	return coin_final

print rec_coin2(10,[1,3,5])



