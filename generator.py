
def createModel(package, imports, klass, fields):
    model = modelTemplate.template
    model = replace(model, "package", package)
    model = replace(model, "imports", imports)
    model = replace(model, "class", klass)
    model = replace(model, "columns", fields)
    writeFile(project_name + "/models/" +
              toCamelCase(table, True)+".java", model)


def createDAO(entity):
    dao = repositoryTemplate.template
    dao = replace(dao, "model", toCamelCase(entity, True))
    dao = replace(dao, "package", schema['package'])
    writeFile(project_name + "/dao/" +
              toCamelCase(entity, True)+"Repository.java", dao)


def createController(entity):
    controller = controllerTemplate.template
    controller = replace(controller, "package", schema['package'])
    controller = replace(controller, "model", entity)
    controller = replace(controller, "model.cap", toCamelCase(entity, True))
    controller = replace(controller, "model.cu", entity.upper())
    controller = replace(controller, "model.small", toCamelCase(entity))
    writeFile(project_name + "/controller/" +
              toCamelCase(entity, True)+"Controller.java", controller)

def createService(entity):
    service = serviceTemplate.template
    service = replace(service, "package", schema['package'])
    service = replace(service, "model", entity)
    service = replace(service, "model.cap", toCamelCase(entity, True))
    service = replace(service, "model.cu", entity.upper())
    service = replace(service, "model.small", toCamelCase(entity))
    writeFile(project_name + "/service/" +
              toCamelCase(entity, True)+"Service.java", service)