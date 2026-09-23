
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#综合项目：零售销售数据可视化分析报告
#项目需求：基于模拟零售销售数据，完成完整的可视化分析，包含核心指标、趋势、品类、分布、关联、热力矩阵6大模块
#代码注释说明：凡是注释的代码，放开注释即可运行

#准备数据
np.random.seed(2026)
dates = pd.date_range("2026-01-01", "2026-06-30", freq="D")
categories = ["食品", "服装", "家电", "日用品", "美妆"]
regions = ["华东", "华南", "华北", "西南", "华中"]

#生成销售明细数据
sales_data = []
for date in dates:
    for region in regions:
        for category in categories:
            sales = np.random.randint(500, 5000)            #销售额
            orders = np.random.randint(20, 200)             #订单量
            profit = sales * np.random.uniform(0.15, 0.35)  #利润[0.15, 0.35)
            sales_data.append([date, region, category, sales, orders, profit])
df_sales = pd.DataFrame(sales_data, columns=["日期", "地区", "品类", "销售额", "订单量", "利润"])
# print(df_sales.head())

#开始
#===== 1.核心指标 =====
total_sales = df_sales["销售额"].sum()
total_orders = df_sales["订单量"].sum()
avg_price = total_sales/total_orders
month_growth = 0.085    #模拟环比数据

# print(f"总销售额：{total_sales:,d}元")
# print(f"总订单量：{total_orders:,}单")
# print(f"平均客单价：{avg_price:,.2f}元")
# print(f"月度环比增长率：{month_growth*100:.1f}%")

#===== 2.月度销售趋势 =====
# monthly_sales = df_sales.groupby(df_sales["日期"].dt.to_period("M"))["销售额"].sum().reset_index()
monthly_sales = df_sales.set_index("日期")["销售额"].resample("MS").sum().reset_index()
# monthly_sales["日期"] = monthly_sales["日期"].astype(str)
# monthly_sales["日期"] = monthly_sales["日期"].dt.strftime("%Y-%m-%d")
# print(monthly_sales.dtypes)

#画图
# fig = px.line(monthly_sales, x="日期", y="销售额", 
#               title="2026年上半年月度销售额趋势",
#               markers=True, text="销售额")
# fig.update_traces(texttemplate="%{text:,.0f}", textposition="top center")
# fig.show()

#===== 3.品类销售分析 =====
cate_sales = df_sales.groupby("品类")["销售额"].sum().reset_index()
cate_sales_sorted = cate_sales.sort_values("销售额", ascending=False)
# print(cate_sales)

# fig1 = px.pie(cate_sales, names="品类", values="销售额", hole=0.3, 
#               title="各品类销售额占比")
# fig1.update_layout(template="plotly_white")
# fig1.show()

# fig2 = px.bar(cate_sales_sorted, x="品类", y="销售额", text_auto=True, 
#               title="各品类销售额占比")
# fig2.update_layout(template="plotly_white")
# fig2.show()

#===== 4.分布分析 =====
# daily_sales = df_sales.groupby("日期")["销售额"].sum().reset_index()
# fig = px.histogram(daily_sales, x="销售额", nbins=20, marginal="box",  
#                    title="日销售额分布分析")
# fig.show()

# region_box = df_sales.groupby(["日期","地区"])["销售额"].sum().reset_index()
# fig = px.box(region_box, x="地区", y="销售额",
#              title="各地区日销售额分布箱线图")
# fig.show()

#===== 5.关联分析 =====
# fig = px.scatter(df_sales, x="销售额", y="利润", color="品类", 
#                  color_continuous_scale="Blues",
#                  trendline="ols", title="销售额与利润的关系")
# fig.update_layout(template="plotly_white")
# fig.show()

#===== 6.地区 品类的热力矩阵 =====
pivot_sales = df_sales.pivot_table(index="地区", columns="品类", values="销售额", aggfunc="sum")
# plt.figure(figsize=(16,8))
# sns.heatmap(pivot_sales, annot=True, fmt=",.0f", cmap="Blues", linewidths=0.5)
# plt.title("各地区分品类销售额热力图")
# plt.tight_layout()
# plt.show()

# print(pivot_sales.head())
# fig = px.density_heatmap(pivot_sales, color_continuous_scale="Viridis")
# fig.show()

# print(df_sales.head())
# plt.figure(figsize=(10,8))
# sns.barplot(df_sales.groupby("日期")["销售额"].sum().reset_index().head(), x="日期", y="销售额")
# plt.title("seaborn画柱状图")
# plt.tight_layout()
# plt.show()
