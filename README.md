# Template repository

Feel free to copy the template `README.md.sample` in your stack to create a new stack documentation.

Then to generate arguments tabs of the stack, you can use the `markdown-tabs-from-comments.py` script.

```
./extra/markdown-tabs-from-comments.py -f  ../my/file
```

This script will parse the specified file for all comments following this format :

```
#. variable_name (required): default_value1
#+ description: my description

#. variable_name2 (optional, str): foo
#+ description: We can specify the type of param after required or not.
#+  Also the long description
#+  On several lines indeed.

#. variable_name3: 
#+ description: you don't need default value, and can ignore required and type to get by default optional.
```

Feel free to include those kind of comments in your different variables files (terraform, pipeline, ansible, ...)


This should generate something like :

|Name|Description|Type|Default|Required|
|---|---|:---:|:---:|:---:|
|`variable_name`|description: my description|`-`|`default_value1`|`True`|
|`variable_name2`|description: We can specify the type of param after required or not. Also the long description On several lines indeed.|`str`|`foo`|`False`|
|`variable_name3`|description: you don't need default value, and can ignore required and type to get by default optional.|`-`|``|`False`|
