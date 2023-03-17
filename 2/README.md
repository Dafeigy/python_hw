<p align="center">
    <img src="https://s2.loli.net/2023/03/17/lY5MZ2CUHxgISj6.png" alt="pyecharts logo" width=150 height=150 />
</p>
<h1 align="center">试题生成器</h1>
<p align="center">
    <em>基于turtle库的小学数学题生成器</em>
</p>


## 使用方法

配置项目文件夹的`config.json`文件，默认的文件中的四个key分别对应`=,-,×,÷`运算表达式的个数。配置完成后即可运行`main.py`：

```python
python3 main.py
```

得到渲染结果。鼠标单击渲染页面即可退出画面。

<img src="https://s2.loli.net/2023/03/16/7YsFXAnKmSMeGiW.png" alt="result" style="zoom: 50%;" />





## 代码架构

代码主要由`QA_pair`和`Paper`类构成，前者为四则运算算式的生成类，后者为基于`turtle`库的题目组织、可视化类。

### QA_pair类

在设计之初考虑到扩展性，因此在`QA_pair`类的设计之时考虑如下几种属性：

* `QA_pair.operater`:算式的操作符，输入为字符(串)类型。
* `QA_pair.numx`:算式的操作数，因题目限定要求故设定为整数类型。
* `QA_pair.able_flag`：算式的合法性。该属性是配合`QA_pair.check_available`方法使用的，通过自定义该方法即可生成符合要求的算式。

除此之外，还有`QA_pair.generate_A`和`QA_pair.generate_Q`两个函数，用于生成算式的字符串用于后续的`turtle.write`。

### Paper类

`Paper`类用于生成试卷。其输入为一个配置的字典`dict`，在后续的扩展中可以更好地接入与开发。 其主要有两个属性：`Paper.cfg`以及`Paper.data`。

* `Paper.cfg`：用于加载试卷的基础配置。在后续开发中，通过调整`json`文件内容即可完成对试卷的基本信息的配置。
* `Paper.data`：用于存放该试卷的试题内容。

除此之外，还有`Paper.generate_data`和`Paper.render_paper`两个方法。前者用于生成试卷的内容，包含题目与答案两部分；后者使用`turtle`库进行页面的渲染操作。

