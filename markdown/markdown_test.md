This is an H1
=======
This is an H2
-------
# This is an H1
## This is an H2

### This is an H3

# [各種語法]
### 引言
> This is blockquote
> 2nd line of quote
>> 2nd-level quote
> quote ...
### List
* Red
    * aaa
    * bbb
* Green
    - aaa
    - bbb
* Blue
    + aaa
    + bbb
    1. aaa
    2. bbb
    3. ccc
    1986\. this is not numbered item
### Seperator
------------
************
### Link
* Link 1: URL
    * Here is the link [Google](https://www.google.com/ "Title")
* Link 2: local file
    * [Local](./another_link_file.md "file title")
        - file path cannot have space?
* Link 3: Tag (case-insesnsitive)
    * [Google][tag_id] ID is unique, and cas-insensitive
* Link 4: Default Tag
    * [Google][] link to google

#### Here is the reference Tag ID
[tag_id]: http://example.com/  "Optional Title Here"
[Google]: http://www.google.com



### 強調
1. *single asterisks*
2. _single underscores_
3. **double asterisks**
4. __double underscores__


### 程式碼
Use the `printf()` function.
``There is a literal backtick (`) here.``
A single backtick in a code span: `` ` ``
A backtick-delimited string in a code span: `` `foo` ``

### 圖片
![Alt text](./doraemon.jpg)
![Alt text](./doraemon.jpg "Optional title")

### 自動連結
<http://www.google.com>
<address@example.com>







