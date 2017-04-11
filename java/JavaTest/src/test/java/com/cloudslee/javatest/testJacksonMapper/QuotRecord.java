package com.cloudslee.javatest.testJacksonMapper;

public class QuotRecord extends BaseRecord {
	public Integer volume; // 成交股數
	public Integer deal; // 成交筆數
	public Float amount; // 成交金額
	public Float open_price; // 開盤價
	public Float top_price; // 最高價
	public Float low_price; // 最低價
	public Float close_price; // 收盤價
	public Float change; // 漲跌價差
	public Float final_reveal_buy_price; // 最後揭示買價
	public Integer final_reveal_buy_vol; // 最後揭示買量
	public Float final_reveal_sell_price; // 最後揭示賣價
	public Integer final_reveal_sell_vol; // 最後揭示賣量
	public Float PE; // 本益比

}
