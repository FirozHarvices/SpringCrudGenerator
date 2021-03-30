from templates import *
import os
from helper import *


def createModel(entity, package, imports, klass, fields):
    model = modelTemplate.template
    model = replace(model, "package", package)
    model = replace(model, "imports", imports)
    model = replace(model, "class", klass)
    model = replace(model, "columns", fields)

    baseModel = baseModelTemplate.template
    baseModel = replace(baseModel, "package", package)

    writeFile(PROJECT_NAME + "/model/" +
              toCamelCase(entity, True)+".java", model)

    # TODO : persist this while working with folder of schema
    writeFile(PROJECT_NAME + "/model/BaseModel.java", baseModel)


def createDAO(entity, package):
    dao = repositoryTemplate.template
    dao = replace(dao, "model", toCamelCase(entity, True))
    dao = replace(dao, "package", package)
    writeFile(PROJECT_NAME + "/dao/" +
              toCamelCase(entity, True)+"Repository.java", dao)


def createController(entity, package):
    controller = controllerTemplate.template
    controller = replace(controller, "package", package)
    controller = replace(controller, "model", entity)
    controller = replace(controller, "model.cap", toCamelCase(entity, True))
    controller = replace(controller, "model.cu", entity.upper())
    controller = replace(controller, "model.small", toCamelCase(entity))
    writeFile(PROJECT_NAME + "/controller/" +
              toCamelCase(entity, True)+"Controller.java", controller)


def createService(entity, package):
    service = serviceTemplate.template
    service = replace(service, "package", package)
    service = replace(service, "model", entity)
    service = replace(service, "model.cap", toCamelCase(entity, True))
    service = replace(service, "model.cu", entity.upper())
    service = replace(service, "model.small", toCamelCase(entity))
    writeFile(PROJECT_NAME + "/services/" +
              toCamelCase(entity, True)+"Service.java", service)


def createConstantsFile(entities, package):
    constants = constantsTemplate.template
    constants = replace(constants, "package", package)
    staticVars = ""
    for entity in entities:
        staticVar = constantsTemplate.static
        staticVar = replace(staticVar, "model.snake.uppper",
                            toUpperCase(entity))
        staticVar = replace(staticVar, "model.camel",
                            toCamelCase(entity) + "/")

        staticVars = staticVars + staticVar

    constants = replace(constants, "vars", staticVars)
    writeFile(PROJECT_NAME + "/Constants.java", constants)


def run(f, shortCodes, PROJECT_NAME, config):
    print("running : "+f)

    rawSchema = readFile(f, True)
    rawSchema = shortCodeParser(rawSchema, shortCodes)

    writeFile(PROJECT_NAME+"compiled/"+f+".json", rawSchema)

    schema = convertToJson(rawSchema, True)
    package = shortCodes["package"]
    entityNameArr = []

    for table, columns in schema['tables'].items():
        entityNameArr.append(table)
        classConfig = columns['config']

        imports = modelTemplate.imports

        imports = imports + \
            "\n".join(map(lambda x: 'import ' + x +
                          ";", classConfig['imports']))
        klass = modelTemplate.klass
        klass = replace(klass, "table", toSnakeCase(table))
        klass = replace(klass, "class", toCamelCase(table, True))
        klass = "\n".join(
            map(lambda x: ''+x, classConfig['annotations'])) + klass
        fields = ""
        for column, data in columns['columns'].items():

            field = modelTemplate.column
            field = arrayJoin(data['annotations'], "", "", "\n") + field
            field = replace(field, "column.var", toCamelCase(column))
            field = replace(field, "column", column)
            field = transform(field, "snake", toSnakeCase)
            field = transform(field, "cap", toUpperCase)
            field = transform(field, "small", toLowerCase)
            field = transform(field, "camel", toCamelCase)
            field = replace(field, "type", data['type'])

            if "join" in data:
                joinColumnId = modelTemplate.joinColumnId
                joinColumnId = replace(joinColumnId, "join", column)
                joinColumnId = replace(
                    joinColumnId, "join.camel.fc", toCamelCase(column))
                if "joinNullable" in data:
                    joinNullable = modelTemplate.notNull
                    joinNullable = replace(
                        joinNullable, "join.camel.fc", toCamelCase(column))
                    joinColumnId = joinNullable + joinColumnId
                # generate  join column
                field = field + joinColumnId

            fields += field
        createModel(table, package, imports, klass, fields)
        createDAO(table, package)
        createController(table, package)
        createService(table, package)
    # createConstantsFile(entityNameArr, package)
    print("generated schema for :"+f)


PROJECT_NAME = input("project name : ")
# PROJECT_NAME = "abc"

folderOrFile = input("do you have schema folder or file?\n1 = folder\n2 = file\nenter your choice : ")
# folderOrFile = "1"

if(folderOrFile == "2"):
    if(os.path.isfile("schema.json")):
        f = "schema.json"
    else:
        f = input("schema file path : ")
elif(folderOrFile == "1"):
    if(os.path.isdir("schema")):
        fpath = "schema"
    else:
        fpath = input("schema folder path : ")
else:
    print("invalid option")
    exit(1)

if(os.path.isfile("config.json")):
    configFilePath = "config.json"
else:
    configFilePath = input("config file path : ")

config = convertToJson(readFile(configFilePath, True), True)
shortCodes = config['shortCodes']

if(folderOrFile == "1"):
    dirpath, _, fyles = next(os.walk(fpath))
    for fyl in fyles:
        run(dirpath + "/" + fyl, shortCodes, PROJECT_NAME, config)
else:
    run(f, shortCodes, PROJECT_NAME, config)
