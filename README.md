# 股票分析系统 (Stock Analysis System)

一个基于Python的股票数据分析和可视化系统，支持多种数据源和龙虎榜查询功能。

## 项目简介

本项目提供了完整的股票数据获取、分析和可视化解决方案，包括：
- 通过API和数据库查询股票信息
- K线图绘制和技术分析
- 龙虎榜数据查询
- 同花顺热榜数据获取
- 数据库管理和更新

## 功能特性

### 📊 股票查询与可视化
- 支持股票代码和股票名称双向查询
- 实时K线图绘制
- 多种数据源支持（API + 数据库）

### 🏆 龙虎榜分析
- 查询个股是否在龙虎榜
- 获取详细龙虎榜数据
- 支持历史数据查询

### 🔥 热门股票追踪
- 同花顺热榜数据获取
- 热门股票实时监控
- 自动化数据更新

### 💾 数据管理
- MySQL数据库集成
- 自动化数据更新
- 数据清洗和维护

## 项目结构

```
├── api_search_draw.py      # API股票查询与绘图
├── db_search_draw.py       # 数据库股票查询与绘图
├── find_lhs.py            # 龙虎榜查询功能
├── ths_hot.py             # 同花顺热榜数据
├── db_connect.py          # 数据库连接配置
├── flush_db.py            # 数据库更新脚本
├── k_line.py              # K线图绘制工具
├── bash.sh                # 系统脚本
└── README.md              # 项目说明文档
```

## 核心模块说明

### 🔍 api_search_draw.py
通过API接口查询股票并绘制K线图
```python
api_search_code_draw(short_name)    # 通过股票名称查询并绘图
api_search_name_draw(stock_code)    # 通过股票代码查询并绘图
```

### 🗄️ db_search_draw.py
通过数据库查询股票并绘制K线图
```python
database_search_name_draw(short_name)  # 数据库名称查询
database_search_code_draw(stock_code)  # 数据库代码查询
```

### 🎯 find_lhs.py
龙虎榜数据查询与分析
```python
search_in_lh(stock_code)    # 查询股票是否在龙虎榜
find_lhb(stock_code)        # 获取龙虎榜详细数据
```

### 🌟 ths_hot.py
同花顺热榜数据处理
```python
main()                      # 主函数 - 获取同花顺热榜
code_draw(stock_code)       # 绘制指定股票K线图
```

### 🔗 db_connect.py
数据库连接管理
```python
db_connect()                # 建立数据库连接
```

### 🔄 flush_db.py
数据库维护与更新

### 📈 k_line.py
K线图绘制核心功能

## 安装要求

### 必需依赖
```bash
pip install pandas
pip install sqlalchemy
pip install pymysql
pip install matplotlib
pip install adata
```

### 数据库配置
- MySQL 数据库
- 配置数据库连接信息在 `db_connect.py`

## 快速开始

### 1. 环境配置
```bash
# 克隆项目
git clone https://github.com/Lambda-zhou/lhb.git
cd lhb

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据库设置
在 `db_connect.py` 中配置你的数据库连接信息：
```python
db_user = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_name = 'your_database'
```

### 3. 使用示例

#### 查询股票并绘制K线图
```python
from db_search_draw import database_search_draw

# 通过股票名称查询
database_search_draw("中信海直")
```

#### 查询龙虎榜数据
```python
from find_lhs import search_in_lh, find_lhb

# 查询是否在龙虎榜
result = search_in_lh("000099")

# 获取龙虎榜详细数据
lhb_data = find_lhb("000099")
```

#### 获取热门股票
```python
from ths_hot import main

# 获取同花顺热榜
main()
```

## 数据源

- **API数据源**: 通过adata库获取实时股票数据
- **数据库**: MySQL存储股票基础信息
- **同花顺**: 热门股票榜单数据

## 注意事项

1. **数据库连接**: 确保MySQL服务正常运行
2. **API限制**: 注意API调用频率限制
3. **数据更新**: 定期运行 `flush_db.py` 更新数据库
4. **网络连接**: 部分功能需要稳定的网络连接

## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- GitHub: [@Lambda-zhou](https://github.com/Lambda-zhou)
- 项目地址: https://github.com/Lambda-zhou/lhb

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！