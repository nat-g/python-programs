#!/usr/bin/env python

def get_max_profit(prices_list):
	smin = prices_list[0]
	smax = prices_list[0]
	current_diff = 0
	max_diff = 0
	for i in prices_list:
		if i < smin:
			smin = i
			current_diff = smax - smin
			if current_diff > max_diff:
				max_diff = current_diff
		elif i > smax:
			smax = i
	
	return max_diff

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
t = get_max_profit(stock_prices_yesterday)
print t