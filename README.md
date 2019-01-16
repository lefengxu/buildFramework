# buildFramework
一个利用Python构建iOS新项目的脚本

### 用途
快速搭建iOS新项目，快速搭建需要的文件目录。目前适用于MVC框架。

### 效果
利用Python脚本生成的文件目录。
![image](https://github.com/lefengxu/buildFramework/blob/master/buildFramework/images/files.png)

### 用法
①要有Python 环境

②主框架模块</br>
主要的框架模块放在buildArchitecture文件夹的build.json中
```
[
  {
    "name": "Modules"
  },
  {
    "name": "Base"
  },
  {
    "name": "Categories",
    "children": 
    [
      {
        "name": "Foundation"
      },
      {
        "name": "UIKit"
      }
    ]
  },
  {
    "name": "Marco"
  },
  {
    "name": "Utils"
  },
  {
    "name": "Vendors"
  },
  {
    "name": "Other"
  },
  {
    "name": "Helper"
  }
]

```
上述的主模块中，其中Modules不可更改，用于放业务逻辑。其他的可以根据个人习惯进行修改，需要内嵌文件夹时用children作为key值。

③业务模块</br>
构建一个业务需要的json，如下
```
[
  {
    "name": "Home"
  },
  {
    "name": "Making",
    "children": 
    [
      {
        "name": "MakingGIF"
      },
      {
        "name": "MakingName"
      },
      {
        "name": "MakingPic"
      }
    ]
  },
  {
    "name": "Search"
  },
  {
    "name": "Setting"
  }
]
```
name表示业务模块</br>
有内嵌时，使用children作为key值。</br>
【备注：MVC文件夹无需用加到children中，脚本会自动生成】

④使用方式</br>
1、cd到脚本所在文件</br>
2、执行脚本</br>
```Python build.py -i <业务文件.json>```</br>

3、所有生成的文件目录放在了buildArchitecture文件夹里</br>
