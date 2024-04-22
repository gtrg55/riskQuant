from scipy.stats import norm
import math


def garman_kohlhagen_call(exchange_rate, strike, time_to_exp, r_usd, r_eur, iv):

    d1 = (math.log(exchange_rate / strike) + (r_usd - r_eur + iv ** 2 / 2) * time_to_exp) / (iv * math.sqrt(time_to_exp))

    d2 = d1 - iv * math.sqrt(time_to_exp)

    call_price = exchange_rate * math.exp(-r_eur * time_to_exp) * norm.cdf(d1) - strike * math.exp(-r_usd * time_to_exp) * norm.cdf(d2)

    return call_price



def delta(exchange_rate, strike, time_to_exp, r_usd, r_eur, iv):
    d1 = (math.log(exchange_rate / strike) + (r_usd - r_eur + iv ** 2 / 2) * time_to_exp) / (iv * math.sqrt(time_to_exp))
    delta = math.exp(-r_eur * time_to_exp) * norm.cdf(d1)
    return delta


def gamma(exchange_rate, strike, time_to_exp, r_usd, r_eur, iv):
    d1 = (math.log(exchange_rate / strike) + (r_usd - r_eur + iv ** 2 / 2) * time_to_exp) / (iv * math.sqrt(time_to_exp))
    gamma = norm.pdf(d1) * math.exp(-r_eur * time_to_exp) / (exchange_rate * iv * math.sqrt(time_to_exp))
    return gamma


def theta(exchange_rate, strike, time_to_exp, r_usd, r_eur, iv):
    d1 = (math.log(exchange_rate / strike) + (r_usd - r_eur + iv ** 2 / 2) * time_to_exp) / (
                iv * math.sqrt(time_to_exp))
    d2 = d1 - iv * math.sqrt(time_to_exp)

    theta_call = (-exchange_rate * norm.pdf(d1) * iv / (2 * math.sqrt(time_to_exp)) * math.exp(-r_eur * time_to_exp) -
                  r_usd * strike * math.exp(-r_usd * time_to_exp) * norm.cdf(d2) +
                  r_eur * exchange_rate * math.exp(-r_eur * time_to_exp) * norm.cdf(d1))

    return theta_call


def vega(exchange_rate, strike, time_to_exp, r_usd, r_eur, iv):
    d1 = (math.log(exchange_rate / strike) + (r_usd - r_eur + iv ** 2 / 2) * time_to_exp) / (iv * math.sqrt(time_to_exp))
    vega = exchange_rate * math.exp(-r_eur * time_to_exp) * norm.pdf(d1) * math.sqrt(time_to_exp)
    return vega






#input data
exchange_rate = 0.9387      # USD/EUR exchange rate
time_to_exp = 1             # time to expiration in years
r_usd = 0.055               # domestic risk-free rate
r_eur = 0.045               # foreign risk-free rate

#Call 90% ATM
strike_long_call = 0.8448   # strike price
iv_long_call = 0.0916       # implied volatility

#Call 110% ATM
strike_short_call = 1.03257 # strike price
iv_short_call = 0.0662      # implied volatility


long_call_price = garman_kohlhagen_call(exchange_rate, strike_long_call, time_to_exp, r_usd, r_eur, iv_long_call)
short_call_price = garman_kohlhagen_call(exchange_rate, strike_short_call, time_to_exp, r_usd, r_eur, iv_short_call)
delta_long_call = delta(exchange_rate, strike_long_call, time_to_exp, r_usd, r_eur, iv_long_call)
delta_short_call =delta(exchange_rate, strike_short_call, time_to_exp, r_usd, r_eur, iv_short_call) * (-1)
gamma_long_call = gamma(exchange_rate, strike_long_call, time_to_exp, r_usd, r_eur, iv_long_call)
gamma_short_call = gamma(exchange_rate, strike_short_call, time_to_exp, r_usd, r_eur, iv_short_call) *(-1)
theta_long_call = theta(exchange_rate, strike_long_call, time_to_exp, r_usd, r_eur, iv_long_call)
theta_short_call = theta(exchange_rate, strike_short_call, time_to_exp, r_usd, r_eur, iv_short_call)*(-1)
vega_long_call = vega(exchange_rate, strike_long_call, time_to_exp, r_usd, r_eur, iv_long_call)
vega_short_call = vega(exchange_rate, strike_short_call, time_to_exp, r_usd, r_eur, iv_short_call)*(-1)
print(f"Long call N1 price: {long_call_price:.5f}")
print(f"Short call N2 price: {short_call_price:.5f}")
print(f"Δ Long call N1 : {delta_long_call:.5f}")
print(f"Δ Short call N2 price: {delta_short_call:.5f}")
print(f"Γ Long call N1 price: {gamma_long_call:.5f}")
print(f"Γ Short call N2 price: {gamma_short_call:.5f}")
print(f"Θ Theta Long call N1: {theta_long_call:.5f}")
print(f"Θ Theta Short call N2: {theta_short_call:.5f}")
print(f"Vega Long call N1 : {vega_long_call:.5f}")
print(f"Vega Short call N2 : {vega_short_call:.5f}")
