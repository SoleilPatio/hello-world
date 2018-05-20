//@version=3
study(title = "CLS: Test Pine", shorttitle="CLS TEST")

//========================================
//above ma200?
//========================================
ma20 = sma(close, 20)
r_above_ma20 = close > ma20 ? 1 : -1



//========================================
//KD > 80 or KD < 20
//========================================
smoothK = input(3, minval=1)
smoothD = input(3, minval=1)
lengthRSI = input(14, minval=1)
lengthStoch = input(14, minval=1)
src = input(close, title="RSI Source")
 
rsi1 = rsi(src, lengthRSI)
k = sma(stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = sma(k, smoothD)

//k>80 or k < 20
r_kd = k > 80? 1 : k < 20? -1 : 0

//is kd cross?
b_cross_kd = (k-d)*(k[1]-d[1]) <= 0 ? 1:0
//gold=-1 dead=1
gold_dead_cross = b_cross_kd ? ( (k > d)? -1 : 1 ) : 0
//gold cross when k < 20 or dead cross when k > 80
r_valid_cross = (r_kd*gold_dead_cross > 0 )? r_kd : 0

//========================================
//BB
//========================================
source = close
length = input(20, minval=1), mult = input(2.0, minval=0.001, maxval=50)
basis = sma(source, length)
dev = mult * stdev(source, length)
upper = basis + dev
lower = basis - dev

r_bb = high >= upper?1 : low <= lower?-1:0 

		
		
		
		
		
		
		
		
		
		
//========================================
//Fill color band
//========================================
fill(hline(1,linestyle=0), hline(-1,linestyle=0), color=#B4B2B6, transp=80)

// fill(hline(1), hline(2), color=blue, transp=80)
// fill(hline(-1), hline(-2), color=blue, transp=80)

// fill(hline(2), hline(3), color=green, transp=80)
// fill(hline(-2), hline(-3), color=green, transp=80)

fill(hline(3,linestyle=0), hline(4,linestyle=0), color=red, transp=80)
fill(hline(-3,linestyle=0), hline(-4,linestyle=0), color=red, transp=80)

//========================================
//Final Result
//========================================
result = r_above_ma20 + r_kd + r_valid_cross + r_bb
plot(result, title="result", linewidth=2, color=blue)
plot(r_above_ma20, title="r_above_ma20")
plot(r_kd, title="r_kd")
plot(r_valid_cross, title="r_valid_cross")
plot(r_bb, title="r_bb")




