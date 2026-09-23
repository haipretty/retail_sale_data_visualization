# 电信客户流失预测项目

## 项目简介

基于模拟电信客户数据，完成端到端机器学习建模全流程：数据加载 → 特征工程 → 数据预处理 → 逻辑回归 / 随机森林建模 → 模型评估 → 结果对比与特征重要性分析。

## 技术栈

- Python 3.x
- NumPy / Pandas
- Scikit-learn（Pipeline / ColumnTransformer / LogisticRegression / RandomForestClassifier）

## 功能特性

- ✅ **数据构建**：模拟 1000 条客户数据（月费、入网月数、客服呼叫次数、是否合约用户等），并按业务规则生成流失概率标签
- ✅ **数据划分**：train_test_split 分层抽样（stratify），保证训练集/测试集流失比例一致
- ✅ **预处理流水线**：ColumnTransformer 对数值列标准化（StandardScaler）、类别列独热编码（OneHotEncoder）
- ✅ **双模型对比**：逻辑回归 vs 随机森林，统一 Pipeline 封装
- ✅ **多维评估指标**：准确率、精确率、召回率、F1、AUC
- ✅ **特征重要性分析**：基于随机森林输出各特征对流失的贡献排序

## 核心设计

```
ColumnTransformer（数值标准化 + 类别独热编码）
        ↓
Pipeline（预处理 + 模型）
        ↓
逻辑回归  vs  随机森林 → 5 项指标对比
```

## 运行方式

```
python customer_churn_predict.py
```

## 学习收获

- 掌握了用 Pipeline + ColumnTransformer 把预处理和建模串成一条流水线，避免数据泄漏
- 理解了分层抽样（stratify）在类别不均衡场景下的作用
- 学会了从 Pipeline 中取出编码后的特征名（get_feature_names_out），对接 feature_importances_ 做可解释性分析
- 实践了分类模型的完整评估体系，理解精确率/召回率/AUC 各自的业务含义

## 关联项目

- 📊 [我的作品集主页](https://github.com/haipretty/portfolio)
- 📔 [学习轨迹与专项练习](https://github.com/haipretty/my_project)
