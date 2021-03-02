# Spring CRUD Generator 2.0

> using this python script you can automate boring process of creating crud with model/controller/repository/service pattern in java with spring-boot

> this project is in beta phase. so fell free to report issues

## Installation
- clone this repository using `git clone https://github.com/HarvicesTechnologies/SpringCrudGenerator.git`
- Download & install  [python3](htttp://www.python.org/downloads/ "python3")
- open terminal on cloned repository folder.

## Usage
- this script need two files 1 for config and 1 for schema

##Config``
``here you can specify short codes that can be used in schema file.``


      "shortCodes": {
        "package": "com.company.project", // base package of your project
        ":str": "String", // you can use **:str** in schema file so it will be converted to **String**
        ":int": "Integer",
        ":typ": "type",
        ":rel": "relation",
        ":insb": "insertable",
        ":updb": "updatable",
        ":jc": "join_column",
        ":f": "false",
        ":t": "true",
        ":Date": "Date",
        ":nbl": "Nullable"
      }

------------


  in  shortcodes object **package** is required
  you can also use variable in side short code value.
>   ex :    :column":"@Column(name = \"${column}\")
  here ${column} is variable that take value from schema file.
>

### List Of Available Variables
- `column` returns current column name (system_mst)

- `column.var` returns current variable of column (systemMST)

  you can use transformers also
>   ex :   :column":"@Column(name = \"$camel{${column}}\")
  here $camel{} is transformer it transform value to camelCase

#### List Of Available Transformers
- `snake` transform value to snake_case

- `cap` transform value to CAPITALCASE

- `small` transform value to smallcase

- `camel`  transform value to camelCase
 
>  NOTE : script required ${VARIABLE | TANSFORMER} in this pattern
Order of execution
  
  you can find sample schema and config file under /sample folder