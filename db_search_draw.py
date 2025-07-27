# 用数据库找股票名画k线图
# 推荐使用pandas方式
import adata
import pandas as pd
from k_line import draw_kline
from db_connect import db_connect


def database_search_name_draw(short_name):
    engine = db_connect()  # 获取数据库引擎
    query = "SELECT stock_code, short_name FROM all_stock WHERE short_name = %s"
    find_code = pd.read_sql_query(query, engine, params=(short_name,))
    if not find_code.empty:
        stock_code = find_code.iloc[0]['stock_code']
        print(f"股票代码是: {stock_code}")
        k_data = adata.stock.market.get_market_min(stock_code)
        draw_kline(k_data, stock_code)
        return stock_code
    else:
        print(f"未找到股票: {short_name}")
        return None


def database_search_code_draw(stock_code):
    engine = db_connect()  # 获取数据库引擎
    query = "SELECT stock_code, short_name FROM all_stock WHERE stock_code = %s"
    find_code = pd.read_sql_query(query, engine, params=(stock_code,))
    if not find_code.empty:
        short_name = find_code.iloc[0]['short_name']
        print(f"股票名称是: {short_name}")
        k_data = adata.stock.market.get_market_min(stock_code)
        draw_kline(k_data, stock_code)
        return short_name
    else:
        print(f"未找到股票: {stock_code}")
        return None