介绍

被西西河第一高楼弄得神魂颠倒，刚好有人要求脱水版，所以写了这个。我不特别精通python，写的东西可能不怎么好看，但是目前看来还可以用，继续改进中。

欢迎诸位河牛提意见建议或者指导或者帮助我改进。

实现

下载的脚本使用的是selenium，恐怕还要有firefox，没有估计改改代码用别的也行。
处理的脚本用的是lxml，用re找到时间日期然后sort。

现在，看懂并且手动实现了原网页的javascript，现在不需要用selenium了，用mechanize即可。
另外写了一个用来提取某个thread里面所有email地址并且输出的脚本getemails

下一步是弄一个flexible的gui，让没有任何兴趣改code的使用者能自己下载自己需要的文章。

Implementation Notes:
The original version used selenium to retrieve the dynamic webpages, and lxml to parse the webpage and regular expression to extract date/time to sort.

The current version implemented the javascript function to decode the page source, and thus no longer needs selenium.

A separate script to extract all the email addresses in one thread is also added.

Next step is to add a platform-independent GUI with more functionalities, such as retrieve all the posts in the whole website from the same author.